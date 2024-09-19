# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class SubABC(ABC):

    @abstractmethod
    def set_sub_method(self):
        pass
