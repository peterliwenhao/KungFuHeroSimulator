from abc import ABC, abstractmethod
from collections import defaultdict, deque

class CharacterBuffStatus(ABC):
    def __init__(self, buff, end_time):
        self.buff = buff
        self.end_time = end_time  # Buff结束时间

    def change_info(self, character_info):
        return self.buff.change_info(character_info)

    def change_health(self, character_health):
        return self.buff.change_health(character_health)

class CharacterHealth:
    def __init__(self, max_hp, max_internal_energy, current_hp=None, current_internal_energy=None):
        # 如果未提供当前值，则初始化为上限
        self.current_hp = current_hp if current_hp is not None else max_hp
        self.max_hp = max_hp
        self.current_internal_energy = current_internal_energy if current_internal_energy is not None else max_internal_energy
        self.max_internal_energy = max_internal_energy
        self.is_dead = False  # 角色是否死亡

    def __str__(self):
        return f"CharacterHealth(Current HP: {self.current_hp}/{self.max_hp}, Current Internal Energy: {self.current_internal_energy}/{self.max_internal_energy}, Is Dead: {self.is_dead})"

    def check_alive(self):
        """检查角色是否存活，如果已经死亡，则抛出异常。"""
        if self.is_dead:
            raise ValueError("Cannot perform any action on a dead character.")

    def update_status(self):
        """更新角色的生存状态和上限检查。"""
        if self.current_hp <= 0:
            self.is_dead = True
            self.current_hp = 0
        else:
            self.is_dead = False
            self.current_hp = min(self.current_hp, self.max_hp)

        self.current_internal_energy = min(self.current_internal_energy, self.max_internal_energy)

    def change_hp(self, amount):
        """修改气血值，正数为恢复，负数为受到伤害。"""
        self.check_alive()
        if not self.is_dead:
            self.current_hp += amount
            self.update_status()

    def change_internal_energy(self, amount):
        """修改内息值，正数为恢复，负数为消耗。"""
        self.check_alive()
        if not self.is_dead:
            self.current_internal_energy += amount
            self.update_status()


class CharacterStatus:
    def __init__(self, character_info, character_health):
        self.character_info = character_info
        self.character_health = character_health
        self.buffs = deque()  # 使用双端队列存储buff
        self.buffs_by_end_time = defaultdict(list)  # 使用字典存储结束时间和buff的映射

    def add_buff(self, buff):
        self.buffs.append(buff)
        self.buffs_by_end_time[buff.end_time].append(buff)

    def remove_buff(self, current_time):
        for buff in self.buffs_by_end_time[current_time]:
            self.buffs.remove(buff)  # 从buff队列中移除
        del self.buffs_by_end_time[current_time]  # 从字典中移除这个时间点的条目

    def calculate_current_info(self):
        current_info = self.character_info
        for buff in self.buffs:
            current_info = buff.apply(current_info)
        return current_info

    def __str__(self):
        current_info = self.calculate_current_info()
        return f"CharacterStatus(Current Info: {current_info}, Health: {self.character_health})"