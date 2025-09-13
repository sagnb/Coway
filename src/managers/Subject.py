class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer_callable):
       self._observers.append(observer_callable) 

    def unsubscribe(self, observer_callable):
        self._observers.remove(observer_callable)

    def notify(self, data):
        for obs in self._observers:
            obs(data)
