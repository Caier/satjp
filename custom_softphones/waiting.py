import pjsua2 as pj
import argparse
import time

class MyCall(pj.Call):
    def __init__(self, acc, audio_file):
        super().__init__(acc)
        self.audio_file = audio_file
        self.player = None
        self.is_active = False

    def onCallState(self, prm):
        call_info = self.getInfo()
        print(f"Call state: {call_info.stateText}")
        if call_info.state == pj.PJSIP_INV_STATE_CONFIRMED:
            print("Call connected")
            self.is_active = True
        elif call_info.state == pj.PJSIP_INV_STATE_DISCONNECTED:
            print("Call disconnected")
            self.is_active = False
            if self.player:
                self.player.stopTransmit()
                self.player = None

def onCallMediaState(self, prm):
    call_info = self.getInfo()
    print("Checking call media state...")
    
    for i in range(len(call_info.media)):
        media_info = call_info.media[i]
        if media_info.type == pj.PJMEDIA_TYPE_AUDIO and media_info.status == pj.PJSUA_CALL_MEDIA_ACTIVE:
            print("Audio media is active")
            call_med = self.getMedia(i)
            if isinstance(call_med, pj.AudioMedia):
                print("Call media active - playing audio file")
                self.player = pj.AudioMediaPlayer()
                self.player.createPlayer(self.audio_file)
                self.player.startTransmit(call_med)


class MyAccount(pj.Account):
    def __init__(self, audio_file):
        super().__init__()
        self.audio_file = audio_file
        self.current_call = None

def pjsua2_main(caller_uri, caller_password, port, audio_file):
    ep_cfg = pj.EpConfig()
    ep = pj.Endpoint()
    ep.libCreate()
    ep.libInit(ep_cfg)

    sipTpConfig = pj.TransportConfig()
    sipTpConfig.port = port
    ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, sipTpConfig)
    ep.libStart()
    
    acfg = pj.AccountConfig()
    acfg.idUri = caller_uri
    acfg.regConfig.registrarUri = "sip:127.0.0.1"
    auth_username = caller_uri.split(":")[1].split("@")[0]
    cred = pj.AuthCredInfo("digest", "*", auth_username, 0, caller_password)
    acfg.sipConfig.authCreds.append(cred)

    acc = MyAccount(audio_file)
    acc.create(acfg)

    print("Waiting for incoming calls. Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ep.libDestroy()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--caller-uri", required=True)
    parser.add_argument("--caller-password", required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--audio-file", required=True)

    args = parser.parse_args()
    pjsua2_main(args.caller_uri, args.caller_password, args.port, args.audio_file)
