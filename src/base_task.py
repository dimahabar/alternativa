from abc import ABC, abstractmethod


class BaseTask(ABC):


    @abstractmethod
    def new_task(cls, *args, **kwargs):
        pass