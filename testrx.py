from rx import create

class State():
    def __init__(self) -> None:
        self.topics = {}

    def update_topic(self, topic: str, data):
        self.topics[topic] = data
    
    def get_topic(self, topic : str):
        return self.topics[topic]


def test_observable(observer, scheduler):
    observer.on_next("Hello")
    observer.on_error("Error")
    observer.on_completed()

source = create(test_observable)

source.subscribe()