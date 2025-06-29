import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from elevenlabs import generate, save, set_api_key
from elevenlabs import voices, Voice, VoiceSettings
import tempfile
from config import ELEVENLABS_API_KEY
import whisper
from pydub import AudioSegment

class ElevenLabsSpeechToText:
    def __init__(self):
        """ElevenLabs API anahtarını ayarla"""
        set_api_key(ELEVENLABS_API_KEY)
        self.sample_rate = 44100
        self.channels = 1
        
    def record_audio(self, duration=5, filename="recorded_audio.wav"):
        """
        Mikrofon ile ses kaydı yapar
        
        Args:
            duration (int): Kayıt süresi (saniye)
            filename (str): Kaydedilecek dosya adı
            
        Returns:
            str: Kaydedilen dosyanın yolu
        """
        print(f"{duration} saniye ses kaydı başlıyor... Konuşmaya başlayın!")
        
        # Ses kaydı
        recording = sd.rec(int(duration * self.sample_rate), 
                          samplerate=self.sample_rate, 
                          channels=self.channels, 
                          dtype=np.int16)
        sd.wait()
        
        # Dosyaya kaydet
        wav.write(filename, self.sample_rate, recording)
        print(f"Ses kaydı tamamlandı: {filename}")
        
        return filename
    
    def text_to_speech(self, text, voice_name="Rachel", output_file="output.mp3"):
        """
        Metni sese çevirir
        
        Args:
            text (str): Sese çevrilecek metin
            voice_name (str): Kullanılacak ses adı
            output_file (str): Çıktı dosyası adı
            
        Returns:
            str: Oluşturulan ses dosyasının yolu
        """
        try:
            # Mevcut sesleri listele
            available_voices = voices()
            
            # Belirtilen sesi bul
            selected_voice = None
            for voice in available_voices:
                if voice.name == voice_name:
                    selected_voice = voice
                    break
            
            if not selected_voice:
                print(f"'{voice_name}' sesi bulunamadı. Varsayılan ses kullanılıyor.")
                selected_voice = available_voices[0]
            
            # Ses oluştur
            audio = generate(
                text=text,
                voice=selected_voice,
                model="eleven_multilingual_v2"
            )
            
            # Dosyaya kaydet
            save(audio, output_file)
            print(f"Ses dosyası oluşturuldu: {output_file}")
            
            return output_file
            
        except Exception as e:
            print(f"Ses oluşturma hatası: {e}")
            return None
    
    def list_available_voices(self):
        """Mevcut sesleri listeler"""
        try:
            available_voices = voices()
            print("\nMevcut sesler:")
            for i, voice in enumerate(available_voices, 1):
                print(f"{i}. {voice.name} ({voice.labels.get('accent', 'N/A')})")
            return available_voices
        except Exception as e:
            print(f"Ses listesi alınamadı: {e}")
            return []

    def mp3_to_text(self, mp3_path, model_name="base"):
        """
        MP3 dosyasını metne çevirir (speech-to-text)
        Args:
            mp3_path (str): MP3 dosyasının yolu
            model_name (str): Whisper model adı (tiny, base, small, medium, large)
        Returns:
            str: Çözümlenen metin
        """
        try:
            # MP3'ü WAV'e çevir
            audio = AudioSegment.from_mp3(mp3_path)
            wav_path = mp3_path + ".wav"
            audio.export(wav_path, format="wav")
            # Whisper ile transkripte et
            model = whisper.load_model(model_name)
            result = model.transcribe(wav_path)
            text = result["text"]
            print(f"\nÇözümlenen metin:\n{text}")
            return text
        except Exception as e:
            print(f"Dönüşüm hatası: {e}")
            return None

def main():
    """Ana program"""
    stt = ElevenLabsSpeechToText()
    
    print("=== ElevenLabs Speech-to-Text Uygulaması ===")
    print("1. Mevcut sesleri listele")
    print("2. Metni sese çevir")
    print("3. Çıkış")
    print("4. MP3 dosyasını metne çevir")
    
    while True:
        choice = input("\nSeçiminizi yapın (1-4): ")
        
        if choice == "1":
            stt.list_available_voices()
            
        elif choice == "2":
            text = input("Sese çevrilecek metni girin: ")
            if text.strip():
                voice_name = input("Ses adını girin (varsayılan: Rachel): ").strip() or "Rachel"
                output_file = input("Çıktı dosyası adını girin (varsayılan: output.mp3): ").strip() or "output.mp3"
                
                stt.text_to_speech(text, voice_name, output_file)
            else:
                print("Geçerli bir metin girin!")
                
        elif choice == "3":
            print("Program sonlandırılıyor...")
            break
            
        elif choice == "4":
            mp3_path = input("Metne çevrilecek MP3 dosyasının yolunu girin: ").strip()
            if mp3_path:
                stt.mp3_to_text(mp3_path)
            else:
                print("Geçerli bir dosya yolu girin!")
            
        else:
            print("Geçersiz seçim! Lütfen 1-4 arasında bir sayı girin.")

if __name__ == "__main__":
    main() 