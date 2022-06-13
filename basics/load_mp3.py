from pydub import AudioSegment

audio = AudioSegment.from_wav("mouaz_new.wave")

# increase the volume by 6dB

audio = audio + 6

audio = audio * 2 

audio = audio.fade_in(2000)

audio.export("converted.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("converted.mp3")

print("Converted succesfully!")