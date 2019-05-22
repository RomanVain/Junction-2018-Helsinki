import numpy as np
import pyaudio
import json
import apiai
import requests
import urllib.request
import wave
import soundfile as sf
import time
from random import randrange
import pyttsx3
from array import array
import speech_recognition as sr
import pyglet
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'file.wav'
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True
def text_to_spech(text):
    f = open("speech.ogg","wb")
    data = {'text':str(text),'voice':'zahar','emotion':'evil','folderId':'b1guea5n4mjr4scq4s9u'}
    hd = {"Authorization":"Bearer CggaATEVAgAAABKABKFs1zsgxRFF7gOAzLMjQ8xgZ-53ct8VZca-UjYvfL58bk0sLmZ9jl_SompAMPHxAYYoHS-2Pkh8HWtR-E-rIsENnkdoOkKFAtHSdkZje9Pbv2NacT_FNqd4ncK6kBmNk17Od2CQ8xrfSza03w8Y1jV6Anv3bICcdLEPG19JWJ7796EKzztIgmlfUbwXb7LmH2BBufdQYkWyO80ChTBHDGBS-CY-eabUda_yblXdpLKEMb64X2tdemSWRoe2V5zscNJSVJx1KNB_6oZh7bf0PZa4NpKtU0_wfbG_Ftirq0rbQnfsYhxr3QcyBeFxNacmCfakQ51XnBWRnWLfYEQ-wM1CHUH-ia-ww9bHZum5kUbFsR8dfj_WU7QDzbZHgvZRpY8Y87FgAcUq7m294JYoblUuy03r7VeQiXQ-SBMHaXAr7J538VL0874MKfX7kGrsJ6ZirJquHLRpQr1IIxcar2bTzSHViQ7QESKsZY8Ndmxxq_7Cj7_lGHKmFLmGzBqY4bdNKXGXa5evMKVbQpyU5tOda0dckietdry5Nvhdjk5XGml_7trfE8m3SkUTqtm2jGgVdBZ6hH70-QNEbwv4Upe-VZIssTG477tB7OqharWpf095drbnzgWcC0PIQf0_nwQcMgn8k7jO0FDDUCGTOhSseixF3peOUxV9RrOeljqMGmQKIGM5Y2I4NWM3ODYzNjRmZTZiNGJhMzkyMjA2ZDNiMDg4EJqc5t8FGNrt6N8FIiIKFGFqZWZpY3NmdHV1ZWc2cGZmODVoEgppY2h5b3Rja2luWgAwAjgBSggaATEVAgAAAFABIPME"}
    res = requests.post("https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize/", headers = hd, data = data)
    f.write(res.content)
    f.close()

engine = pyttsx3.init()
#text_to_spech("Hello, dmitry")
#print(speech_to_text("speach.ogg"))
'''
lst = []

duration = 10  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    lst.append(lst)
    print (volume_norm)

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)
    print('--------------------------------------------')
    print(mean(lst))
    print(max(lst))
    print(min(lst))

 '''


r = sr.Recognizer()
while 1:
	#r = str(randrange(100))
	WAVE_OUTPUT_FILENAME = "file.wav"
# start Recording

	audio = pyaudio.PyAudio()
	stream = audio.open(format=FORMAT, channels=CHANNELS,
	                rate=RATE, input=True,
	                frames_per_buffer=CHUNK)
	frames = []
	lst = []
	i = 0
	s = 1
	f = 0
	while s:
		threshold = 2500 
		max_value = 0
		data = stream.read(CHUNK)
		as_ints = array('h', data)
		max_value = max(as_ints)
		print(max_value)
		if max_value > threshold and f == 0:
			print("recording...")
			f = 1
		if f == 1:
			frames.append(data)
			if len(lst) < 41:
				lst.append(max_value)
			elif i > 39:
				i = 0
			else:
				i+=1
			if len(lst) == 41:
				lst[i] = max_value
				if int(max(lst)) < 1500:
					break

		

	print("finished recording")
	 
	 
	# stop Recording
	stream.stop_stream()
	stream.close()
	
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()
	harvard = sr.AudioFile('file.wav')
	with harvard as source:
		audio1 = r.record(source)
	try:
		qwe = r.recognize_google(audio1)
		print(qwe)
		print('lahi')
		
	except Exception:
		pass
	#time.sleep(1)
	audio.terminate()