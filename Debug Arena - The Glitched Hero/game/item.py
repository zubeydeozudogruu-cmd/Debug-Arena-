# item.py - Oyun içi eşyaların tanımlandığı modül
import random

def use_mystery_box(player):
    dice = random.randint(1, 3)
    
    if dice == 1:
        # Harika Zar: Büyük İyileşme
        heal_amount = 40
        player.hp = min(player.hp + heal_amount, player.max_hp)
        return f"🎲 Şanslı Zar 1 Geldi! Kadim bir şifa enerjisi yayıldı ve +{heal_amount} HP kazandın!"
        
    elif dice == 2:
        # Güç Zarı: Geçici Hasar Buff'ı
        player.damage += 10  # Bir sonraki saldırı için hasarı kalıcı veya geçici artırır
        return f"🎲 Şanslı Zar 2 Geldi! Silahın kırmızı bir alevle kaplandı, Hasarın +10 ARTTI!"
        
    elif dice == 3:
        # Kötü Zar: Büyü Geri Tepmesi
        backfire_damage = 15
        player.hp = max(player.hp - backfire_damage, 1) # Oyuncuyu öldürmesin diye en az 1 HP kalır
        return f"💥 Şanslı Zar 3 Geldi! Kutu elinde patladı! {backfire_damage} hasar aldın!" 
    
class Item:
    def __init__(self, name, item_type, effect_value, uses=1):
        self.name = name
        self.item_type = item_type   # "heal" | "attack_boost" | "shield" | "stun"
        self.effect_value = effect_value
        self.uses = uses

    def use(self, character, enemy=None):
        if self.uses <= 0:
            print(f"  {self.name} tükendi!")
            return False

        if self.item_type == "heal":
            if character.current_hp >= character.max_hp:
               print(f"  Canın zaten tamamen dolu! {self.name} boşa harcanmadı.")
               return False
            before = character.current_hp
            character.current_hp = min(character.current_hp + self.effect_value, character.max_hp)
            healed = character.current_hp - before
            print(f"  {self.name} kullanıldı! +{healed} HP kazandın.")
            

        elif self.item_type == "attack_boost":
            character.temp_damage_boost += self.effect_value
            print(f"  {self.name} kullanıldı! Sonraki saldırı +{self.effect_value} hasar alır.")
            

        elif self.item_type == "shield":
            character.temp_shield += self.effect_value
            print(f"  {self.name} kullanıldı! {self.effect_value} hasara karşı kalkan aktif.")
            

        elif self.item_type == "stun":
            enemy.stunned = True
            print(f"  {self.name} kullanıldı! {enemy.name} felç oldu.")
            pass
        self.uses -= 1
        return True
    

    def __str__(self):
        type_labels = {
            "heal": "İyileşme",
            "attack_boost": "Saldırı Güçlendirme",
            "shield": "Kalkan",
            "stun": "Felç"
            }
        label = type_labels.get(self.item_type, self.item_type)
        return f"{self.name}  [{label}]  (x{self.uses})"
