import subprocess
import time

time.sleep(5)

caller_password = "1234"
audio_file = "audio.wav"

processes = []  
for i in range(5):
    uri = 12001 + i
    port = 5080 + i
    print(f"Uruchamiam sluchacza z portem: {port}")
    process = subprocess.Popen([
        "python3", "waiting.py",  
        "--caller-uri", "sip:"+str(uri)+"@127.0.0.1",
        "--caller-password", caller_password,
        "--audio-file", audio_file,
        "--port", str(port)
    ])
    processes.append(process)


time.sleep(5)

for i in range(5):
    uri = 10001 + i
    port = 5090 + i
    print(f"Uruchamiam program z portem: {port}")
    process = subprocess.Popen([
        "python3", "dialing.py",  
        "--caller-uri", "sip:"+str(uri)+"@127.0.0.1",
        "--caller-password", caller_password,
        "--callee-uri", "sip:"+str(uri+2000)+"@127.0.0.1",
        "--audio-file", audio_file,
        "--port", str(port)
    ])
    processes.append(process)

for process in processes:
    process.wait()
