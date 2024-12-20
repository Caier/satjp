import subprocess

caller_password = "1234"
callee_uri = "sip:9198@127.0.0.1"
audio_file = "audio.wav"

processes = []  
for i in range(20):
    uri = 10001 + i
    port = 5080 + i
    print(f"Uruchamiam program z portem: {port}")
    process = subprocess.Popen([
        "python3", "dialing.py",  
        "--caller-uri", "sip:"+str(uri)+"@127.0.0.1",
        "--caller-password", caller_password,
        "--callee-uri", callee_uri,
        "--audio-file", audio_file,
        "--port", str(port)
    ])
    processes.append(process)

for process in processes:
    process.wait()
