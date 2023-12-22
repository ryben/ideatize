from abc import ABC

from core.BaseSubscriber import BaseSubscriber


class BasePublisher(ABC):
    subscribers: list[BaseSubscriber]

    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer: BaseSubscriber):
        self.subscribers.append(observer)

    def unsubscribe(self, observer: BaseSubscriber):
        self.subscribers.remove(observer)

    def publish_to_observers(self, new_stuff):
        for subscriber in self.subscribers:
            subscriber.on_get_update(new_stuff)
