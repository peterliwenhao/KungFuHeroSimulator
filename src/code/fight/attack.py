
class AttackStatus:
    def __init__(self, damage_dealt=0, internal_energy_absorbed=0, damage_reflected=0, hp_absorbed=0, internal_energy_used=0, hp_used=0,opponent_internal_energy_used=0, opponent_hp_recovered=0):
        self.damage_dealt = damage_dealt  # 对对手造成的伤害
        self.internal_energy_absorbed = internal_energy_absorbed  # 吸取的内息
        self.damage_reflected = damage_reflected  # 伤害反弹
        self.hp_absorbed = hp_absorbed  # 吸取的气血
        self.internal_energy_used = internal_energy_used  # 消耗的内息
        self.hp_used = hp_used  # 消耗的内息
        self.opponent_internal_energy_used = opponent_internal_energy_used  # 对手消耗的内息
        self.opponent_hp_recovered = opponent_hp_recovered  # 对手补充的气血

    def to_report(self, attacker_nickname, defender_nickname):
        report_lines = []
        if self.damage_dealt > 0:
            report_lines.append(f"{attacker_nickname}对{defender_nickname}造成了{self.damage_dealt}点伤害")
        if self.internal_energy_used > 0:
            report_lines.append(f"{attacker_nickname}消耗了额外{self.internal_energy_used}点内息吸收了另外{self.opponent_hp_recovered}点伤害")
        if self.hp_absorbed > 0:
            report_lines.append(f"{attacker_nickname}吸取了{self.hp_absorbed}点气血")
        if self.internal_energy_absorbed > 0:
            report_lines.append(f"{attacker_nickname}吸取了{self.internal_energy_absorbed}点内息")
        if self.damage_reflected > 0:
            report_lines.append(f"但{attacker_nickname}收到了{defender_nickname}的内息反镇，受到了{self.damage_reflected}点伤害")

        # 将各句子组合成报告
        report = "，".join(report_lines) + "。"
        return report
    
    def change_health(self):
        # 计算攻击者的净气血和内息改变值
        attacker_net_hp_change = self.hp_absorbed - self.damage_reflected - self.hp_used
        attacker_net_internal_energy_change = self.internal_energy_absorbed - self.internal_energy_used

        # 计算防御者的净气血和内息改变值
        defender_net_hp_change = - self.damage_dealt
        defender_net_internal_energy_change = -self.opponent_internal_energy_used

        return attacker_net_hp_change, attacker_net_internal_energy_change, defender_net_hp_change, defender_net_internal_energy_change

    def __str__(self):
        return (f"AttackStatus(Damage Dealt: {self.damage_dealt}, "
                f"Internal Energy Absorbed: {self.internal_energy_absorbed}, "
                f"Damage Reflected: {self.damage_reflected}, "
                f"HP Absorbed: {self.hp_absorbed}, "
                f"Internal Energy Used: {self.internal_energy_used})")


