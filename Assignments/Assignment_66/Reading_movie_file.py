import subprocesssound_program = "C:\Program Files\Windows Media Player\wmplayer.exe"
#sound_file = "C:\Users\Public\Music\Sample Music\Kalimba.mp3"
#sound_file = "D:\py_programs\Assignments\Assignment_66\Sample Videos\Wildlife.wmv"
sound_file = "D:\py_programs\Assignments\Assignment_66\Wildlife.wmv"
print "Playing video successfull.."
subprocess.call([sound_program, sound_file])
