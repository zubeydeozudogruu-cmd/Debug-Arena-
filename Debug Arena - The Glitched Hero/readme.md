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

### 13- Stun Mekaniği Entegrasyonu
* **Dosya Adı ve Satır Aralığı:** 'item.py' (L28-L31)
* **Hatanın Sebebi:** Eşya türleri arasında tanımlı olan "stun" (felç) etkisi için ayrılan kod bloğu boş bırakıldığı (pass) için, oyuncu bu eşyayı kullandığında düşman üzerinde hiçbir kontrol etkisi (Crowd Control) oluşmuyordu. Bu durum oyunun strateji derinliğini eksiltiyordu.
* **Nasıl Çözdünüz:** stun bloğu içerisine, parametre olarak gelen enemy nesnesinin felç durumunu (is_stunned) aktif hale getiren mantıksal atama yapıldı. Böylece eşya kullanıldığında düşmanın bir tur boyunca işlem yapamaz hale gelmesi sağlandı ve kullanıcıya bilgilendirme mesajı eklendi.

---

### 14- Envanter Kapasite Genişletme Mekanizması
* **Dosya Adı ve Satır Aralığı:** 'inventory.py'
* **Hatanın Sebebi:** Seviye atlama gibi durumlarda ödül olarak verilmesi planlanan envanter genişletme özelliği (expand_slot) boş bırakıldığı (pass) için oyuncu gelişse bile eşya taşıma sınırı başlangıç değerinde takılı kalıyordu.
* **Nasıl Çözdünüz:** expand_slot metodu içerisinde self.max_slots değişkeni bir birim artırılacak şekilde güncellendi. Bu sayede karakterin gelişimine paralel olarak envanter kapasitesinin de dinamik olarak artırılmasına olanak sağlayan altyapı oluşturuldu.

---

### 15- Kaçılan Düşmanların Sağlık Durumu Senkronizasyonu
* **Dosya Adı ve Satır Aralığı:** 'game.py'
* **Hatanın Sebebi:** Oyuncu savaştan kaçtığında, enemy.current_hp = enemy.max_hp ataması yapıldığı için düşmanın canı tamamen doluyordu. Bu durum, oyuncunun verdiği hasarın boşa gitmesine ve "takip edilme" mekaniğinin adaletsizleşmesine neden oluyordu.
* **Nasıl Çözdünüz:** Düşmanın canını tam kapasiteye eşitleyen kod satırı kaldırıldı.Düşman objesi mevcut current_hp değeriyle fled_enemies kuyruğuna eklendi; böylece tekrar karşılaşıldığında hasar almış haliyle dönmesi sağlandı.

---

### 16- Modüler Sınıf Etkileşimleri ve İçe Aktarma Yönetimi
* **Dosya Adı ve Satır Aralığı:** 'game.py' 
* **Hatanın Sebebi:** Oyunun ana döngüsünü yöneten Game sınıfı; Character, Enemy ve Battle gibi diğer temel sınıflara ihtiyaç duyuyordu. Gerekli içe aktarma (import) işlemleri tamamlanmadığı için sistem bu sınıfları tanıyamıyor ve "NameError" vererek başlatılamıyordu.
* **Nasıl Çözdünüz:** character, enemy, battle ve data modüllerinden ilgili sınıflar ve veri yapıları (CHAPTERS) from .modül_adı import Sınıf yapısı kullanılarak projeye dahil edildi. Bu sayede sınıflar arası iletişim sağlanarak oyunun modüler yapısı işlevsel hale getirildi.

---

---

### 17- Stun (Felç) Durumunu Sıfırlama
* **Dosya Adı ve Satır Aralığı:** 'enemy.py'
* **Hatanın Sebebi:** Düşman bir kez felç (stunned) edildiğinde, bu durumu normale döndürecek bir mantık bulunmadığı için oyunun geri kalanı boyunca saldıramaz halde kalıyordu. Bu durum, stratejik bir avantajı oyunun dengesini bozan bir hataya dönüştürüyordu.
* **Nasıl Çözdünüz:** attack metodu içerisinde, düşman felç etkisinden dolayı sıfır hasar döndürdüğü turda self.stunned değişkeni tekrar False yapılacak şekilde güncellendi. Böylece felç etkisinin sadece bir tur sürmesi sağlandı.

---

### 18- Dinamik ve Değişken Düşman Hasar Hesaplaması
* **Dosya Adı ve Satır Aralığı:** 'enemy.py'
* **Hatanın Sebebi:** Saldırı fonksiyonu varsayılan olarak sabit 0 değerini döndürdüğü için düşmanlar oyuncuya hasar veremiyordu. Ayrıca hasarın hep aynı kalması oyunun strateji ve zorluk katmanını zayıflatıyordu.
* **Nasıl Çözdünüz:** random.randint(-1, 3) fonksiyonu kullanılarak düşmanın temel hasarına rastgele bir sapma eklendi. Hesaplanan değerin negatif çıkma ihtimaline karşı max(0, ...) kontrolü eklenerek düşmanın oyuncuyu yanlışlıkla iyileştirmesi engellendi.

---

### 19- Düşman Yaşam Döngüsü ve Ölüm Kontrolü
* **Dosya Adı ve Satır Aralığı:** 'enemy.py'
* **Hatanın Sebebi:** is_alive fonksiyonu her zaman True döndürdüğü için düşmanın canı sıfıra inse bile ölü kabul edilmiyordu. Bu durum, bitmeyen savaş döngülerine ve oyunun ilerleyememesine neden oluyordu.
* **Nasıl Çözdünüz:** Fonksiyon, sabit True yerine self.current_hp > 0 mantıksal ifadesini döndürecek şekilde revize edildi. Böylece canı tükenen düşmanın sistem tarafından doğru şekilde "ölü" olarak algılanması sağlandı.

---

### 20- Negatif Can (HP) Taşma Hatası
* **Dosya Adı ve Satır Aralığı:** 'character.py' 
* **Hatanın Sebebi:** self.current_hp -= damage satırı, karakter çok büyük bir darbe aldığında can değerinin eksilere (örneğin -15/100) düşmesine neden oluyordu. Kod patlamasa bile arayüzde kötü bir görüntü oluşturur.
* **Nasıl Çözdünüz:** Hasar düşüldükten sonra self.current_hp = max(0, self.current_hp) kontrolü ile canın sıfırın altına inmesi engellendi.

---

### 21- Savunma Pozisyonunun Aktif Edilmemesi
* **Dosya Adı ve Satır Aralığı:** 'character.py' 
* **Hatanın Sebebi:** defend fonksiyonu hala sadece ekrana yazı yazdırıyor. self.is_defending değişkeni True yapılmadığı için, take_damage fonksiyonundaki %50 az hasar alma mantığı asla tetiklenmiyor. Yani karakterin savunma seçmesi hala tamamen işlevsiz.
* **Nasıl Çözdünüz:** defend fonksiyonunun gövdesine self.is_defending = True ataması eklenerek, oyuncu savunma yaptığında bu durumun arka planda da aktifleşmesi sağlandı.

---

### 22- Eşya Kullanım Adedi (Uses) Azaltma Eksikliği
* **Dosya Adı ve Satır Aralığı:** 'item.py'
* **Hatanın Sebebi:** Eşyalar başarıyla tetiklenip etkileri karaktere aktarılmasına rağmen, nesnenin self.uses değişkeni güncellenmiyordu. Bu durum, envanterdeki tüketilebilir malzemelerin sınırsız kullanılmasına yol açarak oyun dengesini bozuyordu.
* **Nasıl Çözdünüz:** Eşya etki bloklarının hemen çıkışına, return True ifadesinden önce self.uses -= 1 satırı eklenerek her başarılı kullanımda eşya miktarının doğru bir şekilde eksilmesi sağlandı.

---

### 23- Kural Dışı Boş Menü Gösterim Sıralaması
* **Dosya Adı ve Satır Aralığı:** 'battle.py'
* **Hatanın Sebebi:** Oyun kurallarına göre "Envanterde kullanılabilir item yoksa sistem uyarı vermeli ve menüyü açmamalıdır" şartı bulunmaktadır. Fakat mevcut use_inventory fonksiyonunda önce self.player.inventory.show() çağrılarak boş envanter tablosu ekrana basılıyor, doluluk kontrolü ise bu çizimden sonra yapılıyordu. Bu durum yarışma senaryosunu doğrudan ihlal ediyordu.
* **Nasıl Çözdünüz:** has_items() kontrol satırı fonksiyonun en başına (çanta görünümü ekrana çizilmeden öncesine) alındı. Böylece eğer çanta boşsa fonksiyon ekrana hiçbir şey basmadan anında "no_items" sinyaliyle süreci engelledi.

---

### 24- Sabit Boş Çanta Kontrolü ve Kilitlenme Sorunu
* **Dosya Adı ve Satır Aralığı:** 'inventory.py'
* **Hatanın Sebebi:** inventory.py içindeki has_items fonksiyonu, oyuncunun çantası tamamen boş olsa bile her koşulda statik olarak return True döndürüyordu. Savaş esnasında envanter boşken "3" tuşuna basıldığında battle.py çantada eşya olduğunu sanıyor, ancak içeride listelenecek eşya bulamadığı için ekrana boş bir tablo çizip sistemin kısır bir döngüye girmesine veya kilitlenmesine sebep oluyordu.
* **Nasıl Çözdünüz:** return True ifadesi silindi. Yerine envanter listesinin güncel doluluk oranını dinamik olarak denetleyen ve eğer envanter boşsa doğrudan False üreten return len(self.items) > 0 mantığı kuruldu.

---

### 25- Adaletsiz Sıra Kaybı ve Tur Döngüsü Açığı
* **Dosya Adı ve Satır Aralığı:** 'battle.py'
* **Hatanın Sebebi:** Orijinal oyun kurallarında "Oyuncu çantasını açıp kullandığında veya kapattığında hamle sırasını kaybetmez" emredilmektedir. Ancak mevcut kod yapısında oyuncu envanterden "0" tuşuna basıp vazgeçtiğinde ("back") veya başarıyla bir eşya kullandığında ("used"), kod bu durumları yakalayamıyordu. Bloktan çıkıp doğrudan fonksiyon sonundaki return "continue" satırına ulaştığı için oyuncu daha aksiyon alamadan tur hakkı bedavaya düşmana geçiyordu.
* **Nasıl Çözdünüz:** elif choice == "3": (Envanter) bloğunun en sonuna, if kontrolünün dışına çıkacak şekilde bir continue komutu yerleştirildi. Böylece oyuncu envanterde ne yaparsa yapsın sırasını kaybetmeden yeniden ana savaş menüsünün (1. Saldır, 2. Savun...) başına yönlendirildi.

---

### 26- Başlangıç Eşya Verisinin Tanımlanmamış Olması
* **Dosya Adı ve Satır Aralığı:** 'data.py'
* **Hatanın Sebebi:** Kılavuzda oyuncunun oyuna 2 kullanımlık temel İksir (+30 HP) ile başlaması gerektiği emredilmiştir. Ancak dosyada sadece 2-5 seviye arası ödüller tanımlanmış, başlangıç eşyasının şablonu unutulmuştur. Bu durum envanterin boş kalmasına veya karakter oluşturulurken sistemin çökmesine sebep oluyordu.
* **Nasıl Çözdünüz:** Dosyaya adı "İksir", tipi "heal", değeri 30 ve kullanım hakkı 2 olan STARTING_ITEMS listesi eklenerek başlangıç veri modeli kılavuza uygun hale getirildi.

---


### 27- Geçerli Girdi Kontrolünde Erken Döngü Kırılması
* **Dosya Adı ve Satır Aralığı:** 'battle.py'
* **Hatanın Sebebi:** Kullanıcı geçerli bir menü numarası (1-4) girdiğinde, kod eylemleri gerçekleştirmeden önce break komutu ile döngüyü kırıyordu. Bu yüzden if/elif bloklarındaki asıl mekanikler (Saldır, Savun) bypass ediliyor ve oyuncu hiçbir şey yapamadan tur sırası düşmana geçiyordu.
* **Nasıl Çözdünüz:** Erken break yapısı kaldırıldı. Girdinin doğruluğu sağlandıktan sonra, eylemlerin (Saldırı ve Savunma) tamamlanmasının ardından döngünün kırılması (break) sağlandı. Envanter seçeneğinde ise sıranın kaybolmaması için continue akışı korundu.

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

