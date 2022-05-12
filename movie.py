import moviepy.editor as mp

video_name = r'yay'
video_format = r'mkv'

myclip = mp.VideoFileClip(f"{video_name}.{video_format}")
myclip.audio.write_audiofile(f"{video_name}.wav")