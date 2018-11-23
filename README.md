# wannaeatrequest

first terminal:
$ pip install pycnic
$ sudo apt-get gunicorn
$ cd /home/user/wannaeatrequest/
$ gunicorn --bind localhost:8080 andrew:app

second terminal:
$ python2.7
> import requests
> r = requests.post('http://localhost:8080/', json = {'username': 'mazafaka', 'timestamp': '2018-10-10 00:00:00', 'coordinate2D': {"latitude": 'test_latitude', "longtitude": 'test_longitutde'}})

log:
{'username': 'mazafaka', 'timestamp': '2018-10-10 00:00:00', 'coordinate2D': {"latitude": 'test_latitude', "longtitude": 'test_longitutde'}}

