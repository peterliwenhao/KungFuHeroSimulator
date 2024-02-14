from abc import ABC, abstractmethod

# CharacterBuff抽象基类定义
class CharacterBuff(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def change_info(self, character_info):
        pass

    @abstractmethod
    def change_health(self, character_health):
        pass

    @abstractmethod
    def calculate_end_time(self, character_info, current_time):
        pass