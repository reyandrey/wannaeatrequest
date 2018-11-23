# -*- coding: utf-8 -*-
from pycnic.core import WSGI, Handler

class Andrew(Handler):

    def post(self):

        response = {
            "username": self.request.data["username"],
            "timestamp": self.request.data["timestamp"],
            "coordinate2D": {"latitude": self.request.data["coordinate2D"]["latitude"],
                             "longtitude": self.request.data["coordinate2D"]["longtitude"]
                             }
        }

        with open('log', 'a') as log:
            log.write(str(response) + u'\n')

        return response


class app(WSGI):
    routes  = [('/', Andrew())]
