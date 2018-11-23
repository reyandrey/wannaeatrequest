# wannaeatrequest

first terminal:
<br>$ pip install pycnic
<br>$ sudo apt-get gunicorn
<br>$ cd /home/user/wannaeatrequest/
<br>$ gunicorn --bind localhost:8080 andrew:app

<br>second terminal:
<br>$ python2.7
<br>> import requests
<br>> r = requests.post('http://localhost:8080/', json = {'username': 'mazafaka', 'timestamp': '2018-10-10 00:00:00', 'coordinate2D': {"latitude": 'test_latitude', "longtitude": 'test_longitutde'}})

<br>log:
<br>{'username': 'mazafaka', 'timestamp': '2018-10-10 00:00:00', 'coordinate2D': {"latitude": 'test_latitude', "longtitude": 'test_longitutde'}}

