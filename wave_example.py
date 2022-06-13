import wave
obj = wave.open("mouaz.wav", "rb")
# rb = read and binary 

print("number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame", obj.getframerate())
print("number of frames", obj.getnframes())
print("paramaters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)

obj.close()

obj_new = wave.open("mouaz_new.wav", "wb")
# wb = WRITE BINARY MODE

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()
