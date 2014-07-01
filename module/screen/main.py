from collections import deque


class Screens(object):
    '''Views container, deque keeps last limited views'''
    history = deque(maxlen=20)
    _instance = None

    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(Screens, self).__new__(self, *args, **kwargs)
        return self._instance
