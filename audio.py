from pydub import AudioSegment
import speech_recognition as sr

# 音声ファイルを変換
audio_path = "6.m4a"
audio = AudioSegment.from_file(audio_path)
audio.export("converted_audio.wav", format="wav")

# 音声ファイルを文字起こし
recognizer = sr.Recognizer()
with sr.AudioFile("converted_audio.wav") as source:
    audio_data = recognizer.record(source)

# Google Web Speech APIを使って音声をテキストに変換
try:
    text = recognizer.recognize_google(audio_data, language="ja-JP")
    print(text)
except sr.UnknownValueError:
    print("音声を認識できませんでした。")
except sr.RequestError as e:
    print(f"音声認識サービスにアクセスできませんでした; {e}")
