from abc import ABC


class BaseSubscriber(ABC):

    def on_get_update(self, new_stuff):
        pass


