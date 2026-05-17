# enemy.py - Düşman karakterlerini temsil eden modül
import random

class Enemy:
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
            self.stunned = False  # TODO: Saldırı gerçekleştikten sonra, düşmanın felç durumunu (stunned) normale döndür.
            return 0
           
        return self.damage + random.randint(-1, 3)  # TODO: (-1 ile +3 aralığında) rastgele bir hasar değeri hesapla ve döndür.
    def take_damage(self, damage):
        # KILAVUZ UYUMU: Alınan gerçek hasar hesaplanır ve güvenle döndürülür.
        old_hp = self.current_hp
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
            
        actual_damage = old_hp - self.current_hp
        return actual_damage  # Geriye ham hasarı değil, gerçekte azalan canı döndürüyoruz.

    def is_alive(self):
        return self.current_hp > 0 

    def get_xp_reward(self):
        return self.xp_reward

    def show_stats(self):
        print(f"  [{self.name}] HP: {self.current_hp}/{self.max_hp} | Level: {self.level}")
