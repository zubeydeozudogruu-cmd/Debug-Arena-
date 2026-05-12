# DEBUG ARENA YARIŞMASI: The Glitched Hero

**Tarih:** 11 Mayıs (10:00) - 17 Mayıs (23:59) 2026

---

## 📌 Yarışma Hakkında
**Türkiye Yapay Zeka Topluluğu** bünyesinde düzenlenen **Debug Arena**, yarışmacıların halihazırda var olan ancak teknik bütünlüğü bozulmuş bir yazılım projesini analiz ederek, içerisindeki hataları (bug) onarmalarını amaçlayan bir hata ayıklama (debugging) yarışmasıdır. Amacınız, size verilen bozuk kod tabanını proje kurallarına sadık kalarak tamamen çalışır hale getirmektir.

---

## 📁 Dosya Hiyerarşisi
```text
  main.py              → Oyunun tek başlangıç noktası. Başka iş yapmaz.
  game/
  ├── __init__.py      → game/ klasörünü Python paketi olarak tanımlar. İçi boştur.
  ├── data.py          → Tüm sabit veriler burada. Bölüm bilgileri, level ödülleri.
  ├── item.py          → Tek bir eşyayı temsil eder ve kullanım mantığını taşır.
  ├── inventory.py     → Oyuncunun çantasını yönetir. Item bilmez, slot bilir.
  ├── character.py     → Oyuncu karakteri. Tüm stat ve aksiyonlar burada.
  ├── enemy.py         → Düşman karakteri. Karakterden bağımsız, daha sade.
  ├── battle.py        → İki karakter arasındaki tek savaşı yönetir.
  └── game.py          → Tüm bölümleri sırayla oynatır, oyunun ana akışıdır.
```

---

## 🚀 Nasıl Çalıştırılır?
Bu proje standart hiçbir ek kütüphaneye ihtiyaç duymaz. Bilgisayarınızda **Python 3** yüklü olması yeterlidir.

Size verilen klasörün (`Debug Arena - The Glitched Hero/`) içinde terminal açarak aşağıdaki komutu çalıştırın:

```bash
python main.py
```

> **Not:** Python komutunun çalışmaması durumunda `python3 main.py` komutunu deneyin.

---

## 🎮 Oyunun Sistem Mantığı ve Teorik Altyapısı (DİKKATLE OKUYUNUZ!)
Sistem içerisindeki "Mantık Hataları (Logic Bugs)" salt kod denenerek onarılamaz! Karşılaştığınız sorunların orijinal oyun kurallarına göre nasıl çalışması gerektiğini bilmezseniz, getireceğiniz "patch" çözümleri geçersiz (hardcoded) sayılacaktır. Aşağıdaki kural seti oyunun orijinal matematiksel modelini tanımlar:

### 1. Savaş ve Hasar Matematiği (En Kritik Bölüm)
- **Saldırı (Attack):** Saldırı gücü sabit değildir! Karakterin hasar formülü şu şekildedir: `Temel Hasar + Rastgele Değer (0-5) + Geçici Güçlendirme Buff'ı`. Eğer yetenek veya eşyadan gelen bir "Geçici Güçlendirme" varsa (Örn: Saldırı Tozu), bu buff eklendikten sonra **mutlaka sıfırlanmalıdır** (tek kullanımlık olmalıdır).
- **Savunma (Defend):** Kullanıcı "Savun" komutunu seçtiğinde, ilgili savuma bayrağı aktifleşir ve o tur alınacak hasar **YARI YARIYA (%50)** düşürülür. Ardından bu bayrak sıfırlanmalıdır.
- **Kalkan (Shield):** "Demir Kalkan" çalıştırılırsa, gelen hasar *ilk olarak* kalkanın gücünden düşer, arta kalan hasar oyuncuya yansır. Kalkan hasarı sönümledikten sonra **Sıfırlanmalıdır (Kalıcı bir ölümsüzlük veya koruma zırhı yaratılamaz)**.
- **HP Kontrolleri (Bounds Check):** Oyunun doğası gereği hem düşman hem karakter HP (Can) havuzu **ASLA 0'ın altına düşmemeli** (negatif olmamalı) ve 0'a sabitlenmelidir.

### 2. Eşyalar ve Envanter Döngüsü
- **Tüketim Limitleri:** Bir eşya kullanıldığında kullanım sayısı  mutlak suretle **1 adet eksilmelidir**.
- **Boş Çanta Kontrolü:** Eğer oyuncunun envanterinde kullanım hakkı (`uses > 0`) olan hiçbir eşya kalmadıysa, sistem "Envanterde kullanılabilir item yok!" uyarısı vermeli ve menüyü açmamalıdır.
- **Felç Etkisi (Stun):** Eşya kullanılarak düşman uyuşturulduğunda, düşmanın o tur hasarı 0 olmalı ve saldırı atlandıktan sonra durum sıfırlanarak düşman normale dönmelidir.
- **Tur Önceliği:** Oyuncu çantasını (Envanter) açıp kullandığında/kapattığında, hamle sırasını **kaybetmez**. Yani iksir içtiğinizde, sistem size "Tekrar saldırmak veya savunmak için" komut sormalı, düşman sistem boşluğundan faydalanıp aniden size (bedavaya) hasar vurmamalıdır!
- **Erişilebilir Eşyalar ve Seviyeleri:** Oyunda kullanılan eşyalar seviye atladıkça belirli bir sırayla oyuncunun envanterine eklenir. Oyuncu maceraya 2 kullanımlık **İksir** (+30 HP) ile başlar. Sonrasında kazanacağı seviye ödülleri şunlardır:
  - **Level 2:** Güçlü İksir (İyileşme - +50 HP yeniler)
  - **Level 3:** Saldırı Tozu (Saldırı Güçlendirme - Sonraki vuruşunuza +8 Hasar ekler)
  - **Level 4:** Demir Kalkan (Kalkan - Gelen hasarın ilk 20 birimini tamamen emer)
  - **Level 5:** Uyuşturma Ruhu (Felç - Düşmanı 1 tur boyunca felç ederek saldırmasını engeller)

### 3. Kaçma ve Karşılaşma (Flee Mechanics)
- **Cezalı Durum:** Eğer kaçış başarısız olursa, düşman oyuncudan bir intikam hamlesi olarak hasar çarpanını (multiplier) 1.5 kat artırıp tekil bir saldırı yapar.
- **Geri Dönüş (Encounter):** Bir düşmandan başarılı şekilde kaçarsanız, o bölümün (chapter) son eşleşmesinde aynı düşman oyuncuyu tekrar bulup karşısına çıkar. Ancak bu geri dönüşte düşman **canı (HP) fullenmiş olarak gelmemelidir!** En son ilk savaştan "yaralı kaçtığınız" anki HP değeri ne ise, %100 aynı HP ile mücadeleye devam ettirmelidir.

### 4. Deneyim (XP) ve Karakter İlerlemesi
Bir bölüm tamamlandığında oyuncu XP sınırını aşar ve seviye (level) atlar. Tüm seviye geçiş özellikleri **AYNI ANDA** kurgulanmalıdır:
- **XP Sıfırlama:** Toplanmış olan XP tutarı tamamen **SIFIRLANIR (0 olur)** ve bir sonraki seviye için tabandan birikmeye başlar (Sıfırlanmazsa bir kere level atlayan sonsuz döngüye girip tekrar tekrar atlar).
- **Can Yenileme:** Karakterin Max HP değeri 20 birim artar ve anlık canı (current HP) bu **yeni maksimum değere** şarj edilmelidir.
- **Güç Artışı:** Karakterin taban saldırı gücü (damage) kalıcı olarak 2 artar.
- **Kapasite:** Çantanın sınır taşıma kapasitesi (+1 slot) genişlemeli ve seviye ödülü envantere eklenmelidir.

### 5. Düşman Mantığı ve Durum Yönetimi
- **Ölüm Kontrolü:** Canı 0 veya altına düşen bir düşman anında "yenilmiş" sayılmalı ve savaş sonlanmalıdır.
- **Felç (Stun) Etkisi:** Düşman felç edildiğinde o tur hasar veremez. Bu tur atlandıktan sonra düşman **normale dönmeli** ve bir sonraki tur saldırabilmelidir.

---

## ⚠️ Yarışma Kuralları
1. **Orijinalite:** Sınıf (Class) yapılarını, dosya isimlerini veya ana oyun döngüsünü tamamen baştan kendi bildiğiniz gibi yazmak ZORUNLU OLMADIKÇA yasaktır. Amaç bozulanı orijinal mantığıyla onarmaktır.
2. **Raporlama Zorunluluğu:** Bulup düzelttiğiniz her hata, bu README dosyasının alt kısmındaki şablona DOLDURULMALIDIR! Sadece kodda onarılan ama burada bahsedilmeyen hatalar kopya/şüpheli işlem şüphesiyle geçersiz sayılır.

---

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

## 🌟 EKLENEN BONUS ÖZELLİKLER (İsteğe Bağlı)
*Oyundaki hataları başarıyla ayıkladıktan sonra projeye kendi yaratıcı kodlarınızı eklemekte özgürsünüz! Yaptığınız ekstra geliştirmeleri jüriye buradan tanıtabilirsiniz.*

**🎯 Ekstra Puan Getirebilecek Geliştirme Fikirleri (İlham Almanız İçin):**
- **Loot (Ganimet) Sistemi:** Öldürülen düşmanların üzerinden rastgele eşya (İksir, Güçlendirme) düşmesi.
- **Kritik Vuruş Şansı:** Karakterin saldırılarında %10 ihtimalle normalin 2 katı (Kritik) hasar çıkarması.
- **Özel Yetenekler (Skills):** Savaşta belli turlarda geri sayımı dolan (Cooldown) ateş topu vb. özel bir vuruş yeteneği.
- **Dükkan (Shop/Tüccar):** Yaratıklardan düşen altınlarla bölüm geçişlerinde envantere eşya alınabilen bir sistem.
- **Birim Testleri (Unit Tests):** Kodunuzun doğruluğunu kanıtlamak için `unittest` veya `pytest` kullanarak fonksiyonlara test yazılması (Profesyonel bir yazılımcı dokunuşu!).

### Bonus Özellik 1: [Özelliğin Adı]
* **Nasıl Çalışıyor:** (Eklediğiniz özelliğin oyun içinde ne işe yaradığını kısaca açıklayıp, varsa çalışma mantığını belirtin.)
* **Dosya ve Konum Bilgisi:** 
    * **Yeni Dosya ise:** Dosya Adı ve Kullanıldığı Yerler
    * **Mevcut Dosya ise:** Dosya Adı, Satır Aralığı ve Diğer Geçtiği Yerler

---

> **💡 Yarışma İpucu:** 
> Kodun içinde her hata için bir `TODO` etiketi bulunmayabilir. Bazı mantık hatalarını bulmak için yukarıdaki **"Oyunun Sistem Mantığı"** bölümünü rehber edinmeli ve kodun bu kurallara uyup uymadığını bizzat test ederek (oyunu oynayarak) keşfetmelisiniz.
