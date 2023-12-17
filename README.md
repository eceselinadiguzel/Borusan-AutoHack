# Borusan-AutoHack
# Trafikte Makas Atma Tespit Sistemi
## Proje Hakkında
Bu proje, trafikte tehlikeli ve yasa dışı makas atma hareketlerini tespit etmek üzere tasarlanmıştır. Python ve Arduino kullanılarak geliştirilen bu sistem, ivme verilerini işleyerek riskli sürüş davranışlarını algılar ve sesli bir uyarı mekanizması ile sürücüyü uyarır.

## Özellikler
**Python Scripti:** Rastgele ivme verileri üretir ve bu verileri görselleştirir.
**Arduino Sketch'i:** MPU6050 ivmeölçer sensöründen alınan verileri işler ve makas atma hareketlerini tespit eder.
**Sesli Uyarı Sistemi:** Tehlikeli hareket algılandığında, buzzer aracılığıyla uyarı verir.
## Kurulum
### Gereksinimler
1. Python 3.x
2. Arduino IDE
3. Arduino Uno veya benzeri bir mikrokontrolör
4. MPU6050 ivmeölçer sensörü
5. Buzzer
### Python Ortamının Kurulumu
+ Python'un en son sürümünü Python'un resmi web sitesinden indirip kurun.
+ Gerekli Python kütüphanelerini kurmak için terminal veya komut istemcisinde şu komutu çalıştırın:
`pip install matplotlib`
### Arduino Ortamının Kurulumu
+ Arduino IDE'yi indirip kurun.
+ Arduino'yu bilgisayarınıza bağlayın ve Arduino IDE'de doğru portu seçin.
+ MPU6050 ivmeölçer sensörünü ve buzzer'ı Arduino'ya bağlayın.
### Kullanım
+ Python scriptini çalıştırarak rastgele ivme verileri üretin ve görselleştirin.
+ Arduino sketch'ini Arduino IDE üzerinden mikrokontrolöre yükleyin.
+ Seri monitörü açarak MPU6050'dan gelen verileri ve makas atma tespitlerini gözlemleyin.
## Geliştirici Notları
+ Bu proje, temel bir prototip olup, gerçek dünya koşullarında daha fazla test ve geliştirmeye ihtiyaç duyar.
+ MPU6050 sensöründen gelen veriler, gerçek trafik koşullarında makas atma hareketlerini tespit etmek için daha karmaşık algoritmalar gerektirebilir.
+ Projenin güvenilirliğini ve doğruluğunu artırmak için ek sensörler ve gelişmiş veri işleme teknikleri üzerinde çalışılabilir.
## Ekip
Ekibimiz; Doruk Aydoğan, TED Üniversitesi Yazılım Mühendisliği son sınıf öğrencisi; Yücel Çimtay, Dr. Öğr. Üyesi, TED Üniversitesi Bilgisayar Mühendisliği Bölümü öğretim üyesi; ve Ece Selin Adıgüzel, TED Üniversitesi Bilgisayar Mühendisliği son sınıf öğrencisi olarak, trafikte makas atma gibi riskli sürüş davranışlarını tespit edebilecek teknolojik çözümler geliştirmek için kendi alanlarımızdaki bilgi ve deneyimleri birleştirdik.

Projemizin başarılı bir şekilde geliştirilmesi ve uygulanması için emek veren herkese teşekkür ederiz. Bu projeye katkıda bulunmak ve geliştirmeye yardımcı olmak isteyenler projenin GitHub sayfasını ziyaret edebilirler.
