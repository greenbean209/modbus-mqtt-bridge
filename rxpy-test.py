import time
from rx.subject import Subject

subject_test = Subject()

state = {}

def update_state(payload):
    key = payload['key']
    value = payload['value']
    state[key] = value


subject_test.subscribe(update_state)


while True:
    current_time = time.time()
    payload = {'key': 'time', 'value': current_time}
    subject_test.on_next(payload)
    print(state)
    time.sleep(5)
