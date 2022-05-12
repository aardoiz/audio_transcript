from pydub import AudioSegment

song = AudioSegment.from_wav("yay.wav")
s_name = 'yay'

times = int(song.duration_seconds/30)

for i in range(1,times+2):
    print(i)
    if i == times+1:
        new = song[(i-1)*30*1000:]
        new.export(f"{s_name}_{i}.wav", format="wav")
        continue
    new = song[(i-1)*30*1000:i*30*1000]
    new.export(f"{s_name}_{i}.wav", format="wav")