# instagram_cekilis_bot

Bu program instagram'da çekilişlere otomatik katılmayı sağlar. 

İnstagram çekilişlerine katılmak için genellikle yapılması gereken işlemler:

+ Çekiliş yapan sayfayı takip etmek
+ Gönderiyi beğenmek
+ Açıklama kısmında hashtag(#)lenmiş sayfaları takip etmek
+ Gönderide belirtilen sayıda arkadaşını yorumlarda etiketlemek

Bu program bu rutin işlemlerin hepsini otomatik yapmayı sağlar. Bu sayede instagramdaki çekilişlerin neredeyse tamamına hızlıca katılınabilir. 
Ayrıca yorumlara sadece emoji atılmasını isteyen çekilişler için otomatik emoji atma özelliği de vardır.


# Ön Hazırlıklar

+ requirements.txt içinde yazan Instagram_API kütüphanesinin 1.0.2 sürümünü ve bu kütüphanenin gerekliliklerini kurun.
+ hesap_kullanici.txt nin ilk satırına çekilişlere katılmak istediğiniz hesabınızın kullanıcı adını; 2. satırına bu hesabın şifresini yazın.
+ isimler_kullanici.txt nin her satrınına yorumlara etiketliyeceğiniz kullanıcıların isimlerini her ismin başına @ işareti koyarak yazın.
+ ikili_isimler_kullanici.txt nin her satrınında 2 kullanıcı ismi (@ ile başlayan) olmalıdır. Bu isimler 2şer kişi etiketlenmesini isteyen çekilişler için kullanılacaktır.
+ uclu_isimler_kullanici.txt nin her satırında 3 kullanıcı ismi (@ ile başlayan) olmalıdır. Bu isimler 3er kişi etiketlenmesini isteyen çekilişler için kullanılacaktır.


Artık cekilis.py'ı çalıştırabilirsiniz. Program çalıştığında sizden bir komut girmenizi isteyecek.

# Kullanım

ilk programı (cekilis.py) çalıştırın. Sonra "basla" komutunu girin. Bu komut sayesinde hesabınızda o an takip ettiğiniz tüm sayfaların verisi kaydedilir. Bunu yaptıktan sonra Instagram'a girip
katılmak istediğiniz çekilişlerin sayfalarını takip edin ve bu sayfalardaki çekiliş gönderilerini beğenin. Bu işlemi tamamladıktan sonra programa geri dönüp "bitir" komutunu girin 
Bu komut ile birlikte o anki takip ettiğiniz hesapların verisi alınır. Eski ve yeni veri karşılaştırılıp aradaki farktan yeni takip ettiğiniz (yani çekilişine katılmak istediğiniz 
hesaplar belirlenir ve ekrana yazılır. Bu hesapların çekilişine katılmak istediğin hesaplar olduğundan emin olduktan sonra "posts" komutunu girmelisin. Bu komut sayesinde hesaplardaki 
çekilişe katılacağın gönderiler (beğendiğin gönderiler) tespit edilir ve ekrana ayrıntıları yazılır. Bundan sonra "katil" komudu ile tüm bu çekilişlere otomatik katılma işlemi başlar. 
Bu işlem etiketlenen kişi sayısına ve katılınan çekiliş sayısına bağlı olarak birkaç dakika sürebilir.


# Ekstra özellikler

Çok nadir de olsa bazı çekilişler katılmak için sadece yorumlara emoji atılmasını ister.  Bu çekilişlere çok sayıda emoji ile katılmak için "emoji" komutu kullanılabilir. Kullanım 
kısmında açıklanan aşamaları yapın. Yanlızca son aşamada "katil" komutunu kullanmak yerine "emoji" komutunu kullanın.
