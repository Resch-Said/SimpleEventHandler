import threading


class SimpleEventHandler:
    def __init__(self):
        self._events = {}
        self._lock = threading.Lock()

    def add_event(self, event_name, callback):
        with self._lock:
            if event_name not in self._events:
                self._events[event_name] = []
            self._events[event_name].append(callback)

    def remove_event(self, event_name, callback):
        with self._lock:
            if event_name in self._events:
                self._events[event_name].remove(callback)

    def trigger_event(self, event_name, *args, **kwargs):
        with self._lock:
            if event_name in self._events:
                for callback in self._events[event_name]:
                    callback(*args, **kwargs)