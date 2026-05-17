# battle.py - Savaş mekaniklerini yöneten modül
import random

class Battle:
    def __init__(self, player, enemy, stage_name=""):
        self.player = player
        self.enemy = enemy
        self.stage_name = stage_name
        self.turn_count = 0
        self.battle_log = []
        self.combo_count = 0  # Oyuncunun üst üste yaptığı başarılı saldırıları sayar

    def start_battle(self):
        print(f"\n  {'='*43}")
        print(f"  SAVAŞ: {self.player.name}  vs  {self.enemy.name}")
        print(f"  BÖLGE: {self.stage_name if self.stage_name else 'Bilinmiyor'}")
        print(f"  {'='*43}\n")

        while self.player.is_alive() and self.enemy.is_alive():
            self.turn_count += 1
            
            # --- BÖLÜM 4: LANETLİ KALE BONUSU (1. Tur Başlangıç Kalkanı) ---
            if self.turn_count == 1 and "LANETLİ KALE" in self.stage_name.upper():
                self.player.temp_shield = 3
                print("\n  🏰 [ÇEVRESEL BONUS] Lanetli Kalenin kadim ruhları sana +3 Kalkan sağladı!")

            self.show_turn_status()
            result = self.player_turn()

            if result == "fled":
                return "fled"

            if self.enemy.is_alive():
                if getattr(self.enemy, 'stunned', False):
                    print(f"\n  {self.enemy.name} felçli olduğu için bu turu pas geçiyor!")
                    self.enemy.stunned = False  
                    continue
                if result == "failed_flee":
                    self.enemy_turn(damage_multiplier=1.5)
                else:
                    self.enemy_turn()

        return self.end_battle()
   
    def player_turn(self):
        used_item_this_turn = False
     
        while True: 
            print(f"\n  --- Senin Turun (Tur {self.turn_count}) ---")
            print("  1. Saldır")
            print("  2. Savun")
            print("  3. Envanter")
            print("  4. Kaç")

            choice = input("  Seçim yap (1-4): ").strip()
            if choice not in ["1", "2", "3", "4"]:
                print("  Geçersiz seçim!")
                continue

            if choice == "1":
                # Kombo sayısını artır
                self.combo_count += 1

                # Her kombo puanı kritik vurma şansını %15 artırır (Maksimum %60 şans)
                crit_chance = min(self.combo_count * 15, 60)

                # Kritik vuruş kontrolü (0 ile 100 arası zar atılır)
                is_crit = random.randint(1, 100) <= crit_chance

                damage = self.player.attack()

                if is_crit:
                 damage = damage * 2  # Kritik vuruş hasarı ikiye katlar!
                 print(f"\n  🔥 [KRİTİK VURUŞ] 🔥 COMBO! Müthiş bir zamanlama!")
                elif self.combo_count > 1:
                 print(f"  ⚔️ [KOMBO x{self.combo_count}] Saldırı serisi devam ediyor...")
                
                # --- ÇEVRESEL SALDIRI BONUSLARI (DOĞRU YERİ) ---
                # BÖLÜM 2: KARANLIK MAĞARA BONUSU
                if "KARANLIK MAĞARA" in self.stage_name.upper():
                    maagara_bonusu = random.randint(0, 5)
                    damage += maagara_bonusu
                    print(f"  [ÇEVRESEL BONUS] Mağara yankısı darbeni güçlendirdi! (+{maagara_bonusu} Ek Hasar)")

                # BÖLÜM 3: ZEHİRLİ BATAKLIK BONUSU
                elif "ZEHIRLI BATAKLIK" in self.stage_name.upper():
                    damage += 2
                    print("  [ÇEVRESEL BONUS] Bataklığın zehirli gazları saldırına +2 Zehir Hasarı ekledi!")

                # BÖLÜM 5: KARANLIK KULE BONUSU
                elif "KARANLIK KULE" in self.stage_name.upper():
                    damage += 4
                    print("   [ÇEVRESEL BONUS] Karanlık Kulenin büyü enerjisi saldırına +4 Kaos Hasarı ekledi!")

                actual = self.enemy.take_damage(damage)
                msg = f"  {self.player.name} saldırdı! {self.enemy.name} {actual} hasar aldı."
                print(msg)
                self.battle_log.append(msg)
                break
                
            elif choice == "2":
                self.combo_count = 0  # Saldırı serisi bozuldu, kombo sıfırlanır.
                self.player.defend()
                self.battle_log.append(f"  {self.player.name} savunma yaptı.")
                break
                
            elif choice == "3":
                self.combo_count = 0  # Saldırı serisi bozuldu, kombo sıfırlanır.
                if used_item_this_turn:
                    print("  [UYARI] Bir tur içinde sadece 1 adet eşya kullanabilirsiniz! Lütfen saldırın veya savunun.")
                else:        
                    inv_result = self.use_inventory()
                    if inv_result == "no_items":
                        print("  Envanterde kullanılabilir item yok!")
                    elif inv_result == "back":
                        continue  
                    elif inv_result == "used":
                        used_item_this_turn = True
                continue  
        
            elif choice == "4":
                self.combo_count = 0  # Saldırı serisi bozuldu, kombo sıfırlanır.
                if random.random() < 0.5:
                    print("  Başarıyla kaçtın!")
                    self.battle_log.append(f"  {self.player.name} kaçtı!")
                    return "fled"
                else:
                    print("  Kaçamadın! Düşman öfkelendi ve daha güçlü saldıracak!")
                    self.battle_log.append(f"  {self.player.name} kaçamadı.")
                    return "failed_flee"

        return "continue"

    def use_inventory(self):
        if not self.player.inventory.has_items():
            return "no_items"
        self.player.inventory.show()
        while True:
            choice = input("  Kullanmak istediğin item numarası (0=geri): ").strip()
            if choice == "0":
                return "back"
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(self.player.inventory.items):
                    item = self.player.inventory.items[idx]
                    if item.uses > 0:
                        item.use(self.player, self.enemy)
                        self.player.inventory.remove_empty()
                        return "used"
            print("  Geçersiz seçim!")

    def enemy_turn(self, damage_multiplier=1):
        raw_damage = self.enemy.attack()
        
        # --- BÖLÜM 1: KARANLIK ORMAN BONUSU (Savunma Kontrolü Doğru Yeri) ---
        if self.player.is_defending:
            if "KARANLIK ORMAN" in self.stage_name.upper():
                raw_damage = int(raw_damage * 0.35)
                print(f"   [ÇEVRESEL BONUS] Orman gölgelerinde gizlendin! Gelen hasar %65 azaledı.")
            else:
                raw_damage = int(raw_damage * 0.50)

        if raw_damage == 0:
            msg = f"  {self.enemy.name} saldırdı ama {self.player.name} bu atağı tamamen savuşturdu! (0 Hasar)"
            print(msg)
            self.battle_log.append(msg)
            return

        final_damage = int(raw_damage * damage_multiplier)
        actual_dmg = self.player.take_damage(final_damage)
        
        if damage_multiplier > 1:
            msg = f"  {self.enemy.name} öfkeyle saldırdı! {self.player.name} {actual_dmg} hasar aldı!"
        else:
            msg = f"  {self.enemy.name} saldırdı! {self.player.name} {actual_dmg} hasar aldı."
        print(msg)
        self.battle_log.append(msg)

    def show_turn_status(self):
        print(f"\n  {'─'*43}")
        print(f"  TUR {self.turn_count}")
        self.player.show_stats()
        self.enemy.show_stats()
        print(f"  {'─'*43}")

    def end_battle(self):
        print(f"\n  {'='*43}")
        if self.player.is_alive():
            print(f"  KAZANDIN! {self.enemy.name} yenildi!")
            self.player.gain_xp(self.enemy.get_xp_reward())
            return "win"
        else:
            print(f"  KAYBETTİN! {self.player.name} yenildi...")
            return "lose"