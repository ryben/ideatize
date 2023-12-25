from abc import ABC, abstractmethod


class BaseSubscriber(ABC):

    @abstractmethod
    def on_get_update(self, new_stuff):
        pass


