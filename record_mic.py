import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
FRAMES_PER_BUFFER = 3200

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=FRAMES_PER_BUFFER)

print("* start recording")

frames = []

for i in range(0, int(RATE / FRAMES_PER_BUFFER * RECORD_SECONDS)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
audio.terminate()

obj = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
obj.setnchannels(CHANNELS)
obj.setsampwidth(audio.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b''.join(frames))
obj.close()