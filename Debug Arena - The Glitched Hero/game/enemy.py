# enemy.py - Düşman karakterlerini temsil eden modül
import random

class Enemy:
    # TODO: Nesne başlatıcı (constructor) içindeki eksik parametreleri tanımla
    def __init__(self, name, hp, damage, xp_reward ,level=1):
        self.name = name
        self.level = level
        self.max_hp = hp
        self.current_hp = hp
        self.damage = damage
        self.xp_reward = xp_reward
        self.stunned = False

    def attack(self):
        if self.stunned:
           # TODO: Felç etkisi altındaki düşman saldırısını atladığında, bir sonraki tur için felç durumunu (stunned) normale döndür.
            print(f"  {self.name} felç! Bu tur saldıramadı.")
            return 0
        return 0  # TODO: (-1 ile +3 aralığında) rastgele bir hasar değeri hesapla ve döndür.

    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
        return damage

    # TODO: Düşmanın mevcut can puanını (current_hp) kontrol ederek canlılığını belirle. Eğer can puanı 0'a eşit veya düşükse düşman ölü olarak kabul edilmeli.
    def is_alive(self):
        return True 

    def get_xp_reward(self):
        return self.xp_reward

    def show_stats(self):
        print(f"  [{self.name}] HP: {self.current_hp}/{self.max_hp} | Level: {self.level}")
