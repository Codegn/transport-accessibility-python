from abc import ABC, abstractmethod

class OridesRepository(ABC):

    @abstractmethod
    def get_from_file(self):
        pass

    @abstractmethod
    def process(self):
        pass