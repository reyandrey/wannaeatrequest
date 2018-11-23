# wannaeatrequest

first terminal:
<br>```$ pip install pycnic
$ sudo apt-get gunicorn
$ cd /home/user/wannaeatrequest/
$ gunicorn --bind localhost:8080 andrew:app```

<br>second terminal:
<br>```$ python2.7
> import requests
> r = requests.post('http://localhost:8080/', json = {'username': 'mazafaka', 'timestamp': '2018-10-10 00:00:00', 'coordinate2D': {"latitude": 'test_latitude', "longtitude": 'test_longitutde'}})```

<br>log:
```{'username': 'mazafaka', 'timestamp': '2018-10-10 00:00:00', 'coordinate2D': {"latitude": 'test_latitude', "longtitude": 'test_longitutde'}}```
