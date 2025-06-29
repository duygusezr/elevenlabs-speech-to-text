# ElevenLabs Speech-to-Text Uygulaması

Bu proje, ElevenLabs API kullanarak metin-ses dönüşümü yapan bir Python uygulamasıdır.

## Özellikler

- ElevenLabs API ile yüksek kaliteli ses sentezi
- Mevcut sesleri listeleme
- Metni sese çevirme
- Çoklu dil desteği

## Kurulum

1. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

2. API anahtarınızı `config.py` dosyasında ayarlayın:
```python
ELEVENLABS_API_KEY = "your_api_key_here"
```

## Kullanım

Uygulamayı çalıştırmak için:
```bash
python speech_to_text.py
```

### Menü Seçenekleri

1. **Mevcut sesleri listele**: ElevenLabs'te mevcut olan tüm sesleri gösterir
2. **Metni sese çevir**: Girilen metni seçilen ses ile sese çevirir
3. **Çıkış**: Uygulamayı sonlandırır

### Örnek Kullanım

```
=== ElevenLabs Speech-to-Text Uygulaması ===
1. Mevcut sesleri listele
2. Metni sese çevir
3. Çıkış

Seçiminizi yapın (1-3): 2
Sese çevrilecek metni girin: Merhaba, bu bir test mesajıdır.
Ses adını girin (varsayılan: Rachel): Rachel
Çıktı dosyası adını girin (varsayılan: output.mp3): test.mp3
Ses dosyası oluşturuldu: test.mp3
```

## Dosya Yapısı

- `speech_to_text.py`: Ana uygulama dosyası
- `config.py`: API anahtarı yapılandırması
- `requirements.txt`: Gerekli Python kütüphaneleri
- `README.md`: Bu dosya

## Notlar

- ElevenLabs API anahtarınızı güvenli tutun
- Ses dosyaları MP3 formatında kaydedilir
- Çoklu dil desteği için `eleven_multilingual_v2` modeli kullanılır

## Hata Giderme

Eğer ses oluşturma sırasında hata alırsanız:
1. API anahtarınızın doğru olduğundan emin olun
2. İnternet bağlantınızı kontrol edin
3. ElevenLabs hesabınızda yeterli kredi olduğundan emin olun 