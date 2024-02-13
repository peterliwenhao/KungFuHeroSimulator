
class CharacterInfo:
    def __init__(self, hp_limit, internal_energy_limit, attack_min, attack_max, defense, armor_penetration, hit_rate,
                 dodge_rate, critical_rate, break_rate, anti_critical, anti_break, critical_damage_bonus,
                 damage_reflection, true_damage_reflection_reduction, damage_reduction, hp_steal_ratio,
                 internal_energy_steal_ratio, life_steal_reduction, final_damage_increase, final_damage_reduction,
                 additional_direct_damage, speed):
        self.hp_limit = hp_limit  # 气血上限
        self.internal_energy_limit = internal_energy_limit  # 内息上限
        self.attack_min = attack_min  # 最小攻击力
        self.attack_max = attack_max  # 最大攻击力
        self.defense = defense  # 防御
        self.armor_penetration = armor_penetration  # 破甲
        self.hit_rate = hit_rate  # 命中率
        self.dodge_rate = dodge_rate  # 闪避率
        self.critical_rate = critical_rate  # 暴击率
        self.break_rate = break_rate  # 破击率
        self.anti_critical = anti_critical  # 抗暴击
        self.anti_break = anti_break  # 抗破击
        self.critical_damage_bonus = critical_damage_bonus  # 附加暴击造成伤害
        self.damage_reflection = damage_reflection  # 伤害反弹
        self.true_damage_reflection_reduction = true_damage_reflection_reduction  # 真实反弹伤害减免
        self.damage_reduction = damage_reduction  # 伤害减免
        self.hp_steal_ratio = hp_steal_ratio  # 气血吸取比例
        self.internal_energy_steal_ratio = internal_energy_steal_ratio  # 内息吸取比例
        self.life_steal_reduction = life_steal_reduction  # 降低对手吸血
        self.final_damage_increase = final_damage_increase  # 最终伤害提升
        self.final_damage_reduction = final_damage_reduction  # 受到最终伤害降低
        self.additional_direct_damage = additional_direct_damage  # 附加直接伤害
        self.speed = speed  # 速度

    def __str__(self):
        return f"Character(Hp Limit: {self.hp_limit}, Internal Energy Limit: {self.internal_energy_limit}, " \
               f"Attack: {self.attack_min}-{self.attack_max}, Defense: {self.defense}, " \
               f"Armor Penetration: {self.armor_penetration}, Hit Rate: {self.hit_rate}%, " \
               f"Dodge Rate: {self.dodge_rate}%, Critical Rate: {self.critical_rate}%, " \
               f"Break Rate: {self.break_rate}%, Anti-Critical: {self.anti_critical}%, " \
               f"Anti-Break: {self.anti_break}%, Critical Damage Bonus: {self.critical_damage_bonus}%, " \
               f"Damage Reflection: {self.damage_reflection}%, True Damage Reflection Reduction: {self.true_damage_reflection_reduction}%, " \
               f"Damage Reduction: {self.damage_reduction}, HP Steal Ratio: {self.hp_steal_ratio}%, " \
               f"Internal Energy Steal Ratio: {self.internal_energy_steal_ratio}%, Life Steal Reduction: {self.life_steal_reduction}%, " \
               f"Final Damage Increase: {self.final_damage_increase}%, Final Damage Reduction: {self.final_damage_reduction}%, " \
               f"Additional Direct Damage: {self.additional_direct_damage}, Speed: {self.speed})"



class CharacterStatus:
    def __init__(self, max_hp, max_internal_energy, current_hp=None, current_internal_energy=None):
        # 如果未提供当前值，则初始化为上限
        self.current_hp = current_hp if current_hp is not None else max_hp
        self.max_hp = max_hp
        self.current_internal_energy = current_internal_energy if current_internal_energy is not None else max_internal_energy
        self.max_internal_energy = max_internal_energy
        self.is_dead = False  # 角色是否死亡

    def __str__(self):
        return f"CharacterStatus(Current HP: {self.current_hp}/{self.max_hp}, Current Internal Energy: {self.current_internal_energy}/{self.max_internal_energy}, Is Dead: {self.is_dead})"

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
            if self.current_hp > self.max_hp:
                self.current_hp = self.max_hp

        if self.current_internal_energy > self.max_internal_energy:
            self.current_internal_energy = self.max_internal_energy

    def receive_damage(self, damage):
        self.check_alive()
        self.current_hp -= damage
        self.update_status()

    def heal(self, healing_amount):
        self.check_alive()
        if not self.is_dead:
            self.current_hp += healing_amount
            self.update_status()

    def use_energy(self, amount):
        self.check_alive()
        self.current_internal_energy -= amount
        if self.current_internal_energy < 0:
            self.current_internal_energy = 0
        self.update_status()

    def recover_energy(self, amount):
        self.check_alive()
        self.current_internal_energy += amount
        self.update_status()
