from flask import (
    render_template as render,
    request, 
    redirect, 
    send_from_directory
)
from tinydb import TinyDB, Query
from dashboard import server as app
import os
import pathlib
import json, requests
from data import location
#设备ID
deviceId = "638884917"
APIKey = "HNGpdEZ=9hr2PRxQHwQkf3p9cJU="
headers = {'api-key': APIKey}

# 基本设置
url = "http://api.heclouds.com/devices/"+deviceId+"/datastreams"

session = {'username': ''}

app_path = str(pathlib.Path(__file__).parent.resolve())
db_path = os.path.join(app_path, os.path.join("data", "db.json"))

db = TinyDB(db_path, sort_keys=True, indent=4, separators=(',', ': '))
usr = db.table('users')


@app.errorhandler(404)
def page_not_found(e):
    return render('error.html')


@app.route('/assets/<path:path>', methods=['GET'])
def send_assets(path):
    return send_from_directory('assets', path)


@app.route('/data/<path:path>', methods=['GET'])
def send_data(path):
    return send_from_directory('data', path)


@app.route('/', methods=['GET'])
@app.route('/signin', methods=['GET'])
def signin():
    return render('signin.html')


@app.route('/signup', methods=['GET'])
def signup():
    return render('signup.html')


@app.route('/signout', methods=['GET'])
def signout():
    return redirect('/')


@app.route('/signin', methods=['POST'])
def do_signin():
    User = Query()
    users = usr.search(User.name == request.form['username'])
    if not users:
        return render('signin.html', text='Wrong username or password')
    user = users[0]
    if user['password'] != request.form['password']:
        print(user['password'], request.form['password'])
    session['username'] = user['name']
    return redirect('dashboard')


@app.route('/signup', methods=['POST'])
def do_signup():
    User = Query()
    users = db.search(User.name == request.form['username'])
    if len(users) > 0:
        text = 'Such user have already exists'
        return render('signup.html', text=text)
    usr.insert({
        'name' : request.form['username'],
        'email': request.form['email'],
        'password': request.form['password']
    })
    return redirect('/')


### 自己的 代码 用于显示轨迹 ###
### 锦城湖
@app.route('/show_JCH_track', methods=['GET'])
def show_JCH_track():

    data = location.data_JCH
    center = location.center_JCH

    
    return render('show_track.html',data = data, center = center)


@app.route('/show_TFGC_track', methods=['GET'])
### 天府广场
def show_TFGC_track():
    data = location.data_tianfu
    center = location.center_tianfu

    return render('show_track.html',data = data, center = center)


@app.route('/show_CD_track', methods=['GET'])
# 川大
def show_CD_track():
    # data = [
    #     [116.478935,39.997761],
    #     [116.478939,39.997825],
    #     [116.478912,39.998549],
    #     [116.478912,39.998549],
    #     [116.478998,39.998555],
    #     [116.478998,39.998555],
    #     [116.479282,39.99856]
    #     ]

    data = location.data_CD
    center = location.center_CD

    
    return render('show_track.html',data = data, center = center)

@app.route('/show_latest_location', methods=['GET'])
### 显示最新的定位数据
def show_latest_location():
    # data = [119.48047, 32.786118,]
    print('进来了....')
    r = requests.get(url, headers=headers)

    params = json.loads(r.text)
    print('params=',params)
    current_value = params.get('data')[0].get('current_value')
    lon = current_value.get('lon')
    lat = current_value.get('lat')

    data = [lon,lat]
    print('最新的坐标是',data)

    return render('show_latest_location.html',data = data, center = data)


if __name__ == '__main__':
    app.run(debug=True, port=8050)
