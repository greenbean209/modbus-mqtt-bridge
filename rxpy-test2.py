import time
from rx.subject import Subject

subject_test = Subject()

class State():
    def __init__(self) -> None:
        self.value = {}

    def update(self, payload):
        key = payload['key']
        value = payload['value']
        self.value[key] = value


state = State()

subject_test.subscribe(state.update)


while True:
    current_time = time.time()
    payload = {'key': 'time', 'value': current_time}
    subject_test.on_next(payload)
    print(state.value)
    time.sleep(5)
