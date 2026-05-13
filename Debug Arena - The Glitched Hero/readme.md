# DEBUG ARENA YARIŞMASI: The Glitched Hero

## 🛠️ ÇÖZÜLEN HATALAR FORMU
> *Lütfen bulduğunuz ve düzelttiğiniz hataları aşağıdaki şablona uygun olarak ekleyiniz.*

### 1- Eksik Sözdizimi Karakteri (Missing Colon)
* **Dosya Adı ve Satır Aralığı:** `battle.py` (L94)
* **Hatanın Sebebi:** def enemy_turn(self, damage_multiplier=1) satırının sonunda : (iki nokta üst üste) eksik. Python'da fonksiyon, döngü ve koşul bloklarının başlangıcında bu karakterin bulunması zorunludur. Aksi halde SyntaxError oluşur.
* **Nasıl Çözdünüz:** Fonksiyon imzasının sonuna : karakteri eklenerek blok başlatıldı.

---

### 2-Kapatılmamış Parantez Hatası (Unclosed Parenthesis)
* **Dosya Adı ve Satır Aralığı:** 'character.py' (L78-L80)
* **Hatanın Sebebi:** print( fonksiyonu açılmış ancak kapanış parantezi ) yazılmamıştı. Bu durum Python’da syntax hatasına neden oluyordu.Python, parantez kapanana kadar kodun devam ettiğini sanır.
* **Nasıl Çözdünüz:** 78. satır ve çevresindeki tüm parantez aç-kapat eşleşmeleri kontrol edilerek eksik olan ) karakteri eklendi.

---

### 3-Tamamlanmamış Karakter Dizisi (Unterminated String Literal)
* **Dosya Adı ve Satır Aralığı:** 'character.py' (L78-L80)
* **Hatanın Sebebi:** f-string içerisinde açılan çift tırnak (") kapatılmadığı için Python string yapısını tamamlayamıyordu.Oyun arayüzü karakter bilgilerini basmaya çalıştığı anda sistem donar ve kapanır.
* **Nasıl Çözdünüz:** f-string ifadesinin sonuna eksik olan " işareti eklenerek metin bloğu sonlandırıldı.

---

### 4-Komut Ayırma Hatası (Statements Separation Error)
* **Dosya Adı ve Satır Aralığı:** 'character.py' (L78-L80)
* **Hatanın Sebebi:** Bir önceki hatadan (tırnağın kapanmaması) dolayı Python, 80. satırı  birbirine girmiş tek bir bozuk komut gibi algılıyor.Kod hiyerarşisi bozulduğu için Character sınıfı düzgün yüklenemez ve oyun daha başlatılamadan durur.
* **Nasıl Çözdünüz:** Satır sonuna tırnak ve parantez kapatma ") eklenerek her bir komutun kendi satırında bağımsız çalışması sağlandı.

---

### 5- Geçersiz Parametre Tanımı (Ellipsis Syntax Error)
* **Dosya Adı ve Satır Aralığı:** 'enemy.py' (L6)
* **Hatanın Sebebi:** __init__ fonksiyonu içerisinde parametre listesi yerine üç nokta (...) kullanılmış.Bu hata, düşman nesnesinin (Object) oluşturulmasını tamamen engeller. Oyun bir düşmanla karşılaşmaya çalıştığı anda "SyntaxError" vererek kapanır.
* **Nasıl Çözdünüz:** ... yerine self, name, hp, damage, xp_reward parametreleri eklenerek fonksiyon imzası geçerli hale getirildi.

---

### 6- Sözlük (Dictionary) İçinde Eksik Virgüller
* **Dosya Adı ve Satır Aralığı:** 'item.py' (L37-L42)
* **Hatanın Sebebi:** type_labels isimli sözlük (dictionary) tanımlanırken her bir anahtar-değer çiftinin arasına virgül (,) konulmamış.Envanterinizi açmaya çalıştığınızda veya bir eşyanın ismini ekranda görmek istediğinizde oyun anında çöker.
* **Nasıl Çözdünüz:** Her satırın sonuna virgül eklenerek sözlük yapısı düzeltilir.

---

### 7- Envanter Kullanımı Sonrası Hamle Sırası Kaybı
* **Dosya Adı ve Satır Aralığı:** 'battle.py' (L32-L61)
* **Hatanın Sebebi:** Orijinal kodda oyuncu envanterini açıp bir eşya kullandığında , fonksiyon doğrudan return "continue" mesajı gönderiyordu. Bu durum, oyuncu eşya kullandıktan sonra henüz saldırmamış olmasına rağmen sıranın otomatik olarak düşmana geçmesine neden oluyordu. Bu da oyun kurallarındaki "Envanter kullanımı tur kaybettirmez" maddesini bozuyordu.
* **Nasıl Çözdünüz:** player_turn fonksiyonundaki menü seçim kısmı geniş bir while True döngüsü içerisine alındı."Envanter" seçeneği (choice == "3") sonuna continue komutu eklendi. Böylece eşya kullanımı sonrası fonksiyon kapanmak yerine döngü başına dönerek oyuncuya tekrar hamle seçme hakkı tanınmış oldu.

---

### 8- Hatalı Döngü Kapsamı ve Koşul Bloğu (If) Hizalama Hatası
* **Dosya Adı ve Satır Aralığı:** 'battle.py' (L32-L61)
* **Hatanın Sebebi:** Karakterin envanter kullanımından sonra hamle yapabilmesini sağlamak amacıyla eklenen while True: döngüsü, fonksiyon tanımının dışına yazılmıştır.while döngüsü fonksiyonun üzerinde kaldığı için altındaki if/elif seçim blokları döngü kapsamından çıkmış ve "bağımsız/sahipsiz kod" (Unexpected Indentation) durumuna düşmüştür.if choice == "3" bloğu altındaki continue komutu, kendisini kapsayan bir döngü bulamadığı için Python tarafından geçersiz sayılmıştır. Bu yapısal bozukluk oyunun battle.py modülünün yüklenmesini tamamen engellemekteydi.
* **Nasıl Çözdünüz:** Fonksiyon hiyerarşisi baştan düzenlenmiştir. while True: döngüsü def player_turn(self): fonksiyonunun içerisine taşınmıştır. Ardından, kullanıcı seçimlerini kontrol eden tüm if, elif ve else blokları bu döngünün içine girecek şekilde hiyerarşik olarak hizalanmıştır. Bu sayede continue komutu döngü ile tekrar ilişkilendirilmiş ve kodun teknik bütünlüğü sağlanmıştır.

---

### 9- Hatalı Hasar Hesaplama Mantığı
* **Dosya Adı ve Satır Aralığı:** 'character.py' (L23-L26)
* **Hatanın Sebebi:** attack metodu sabit 0 döndürdüğü için karakter hasar veremiyordu. Ayrıca geçici hasar artışlarının (temp_damage_boost) kullanıldıktan sonra sıfırlanması kuralı uygulanmamıştı.
* **Nasıl Çözdünüz:** temel hasar + rastgele değer (0-5) + geçici boost formülüyle güncellendi. Hesaplama sonrası temp_damage_boost sıfırlanarak hasarın tek seferlik olması sağlandı ve toplam değer döndürüldü. 

---

### 10- Seviye Atlama Sonrası XP Sıfırlama Mekanizması
* **Dosya Adı ve Satır Aralığı:** 'character.py' (L54)
* **Hatanın Sebebi:** Karakter seviye atladığında mevcut XP puanı sıfırlanmıyordu. Bu durum, karakterin bir sonraki seviye eşiğine ulaştığı anda kazandığı her yeni puanda tekrar tekrar seviye atlama döngüsüne girmesine neden oluyordu.
* **Nasıl Çözdünüz:** Seviye artışı gerçekleştikten sonra self.xp değeri 0'a eşitlenerek ilerleme sisteminin her seviye için baştan başlaması ve tutarlı çalışması sağlandı.

---

### 11- Statik Maksimum Can (Max HP) Havuzu Sorunu
* **Dosya Adı ve Satır Aralığı:** 'character.py' (L55)
* **Hatanın Sebebi:** Seviye atlama mekanizmasında karakterin hasarı artarken max_hp sabit kalıyordu. Bu durum, oyunun ilerleyen aşamalarında düşmanlar güçlenirken oyuncunun dayanıklılığının başlangıç seviyesinde kalmasına ve oyun dengesinin bozulmasına yol açıyordu.
* **Nasıl Çözdünüz:** level_up fonksiyonuna max_hp artış protokolü eklendi. Karakterin seviye atladığı her seferinde maksimum canı belirli bir oranda artırılacak şekilde güncellendi.

---

### 12- Oyun Motoru Başlatma ve Hata Yönetimi
* **Dosya Adı ve Satır Aralığı:** 'main.py' 
* **Hatanın Sebebi:** Projenin giriş noktasında Game sınıfı import edilmemişti ve oyunu başlatacak ana mekanizma kurulmamıştı. Ayrıca, çalışma anında oluşabilecek hataları yakalayacak bir güvenlik katmanı bulunmuyordu.
* **Nasıl Çözdünüz:** Game sınıfı import edilerek oyun nesnesi oluşturuldu. Tüm başlatma süreci bir try-except bloğuna alınarak olası çökmelere karşı hata yönetimi sağlandı. if __name__ == "__main__": kontrolü eklenerek sistemin güvenli bir şekilde tetiklenmesi sağlandı.

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 'item.py' (L28-L31)
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

### 3- [Hatanın Konusu]
* **Dosya Adı ve Satır Aralığı:** 
* **Hatanın Sebebi:** 
* **Nasıl Çözdünüz:** 

---

