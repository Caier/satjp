import pjsua2 as pj
import argparse
import time

class MyCall(pj.Call):
    def __init__(self, acc, callee_uri, audio_file):
        super().__init__(acc)
        self.callee_uri = callee_uri
        self.audio_file = audio_file
        self.player = None
        self.is_active = False  # Flaga aktywności rozmowy

    def onCallState(self, prm):
        call_info = self.getInfo()
        print(f"Call state: {call_info.stateText}")
        if call_info.state == pj.PJSIP_INV_STATE_CONFIRMED:
            print("Call connected")
            self.is_active = True  # Ustaw flagę na aktywne
        elif call_info.state == pj.PJSIP_INV_STATE_DISCONNECTED:
            print("Call disconnected")
            self.is_active = False  # Ustaw flagę na nieaktywne
            if self.player:
                self.player.stopTransmit()
                self.player = None

    def onCallMediaState(self, prm):
        call_info = self.getInfo()
        print(f"Call media state: {call_info.mediaState}")
        if call_info.mediaState == pj.PJSUA_CALL_MEDIA_ACTIVE:
            call_med = self.getMedia(0)
            if isinstance(call_med, pj.AudioMedia):
                self.player = pj.AudioMediaPlayer()
                self.player.createPlayer(self.audio_file)
                self.player.startTransmit(call_med)

def pjsua2_main(caller_uri, caller_password, callee_uri, audio_file, port):
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
    acfg.regConfig.registrarUri = "sip:127.0.01"
    auth_username = caller_uri.split(":")[1].split("@")[0]
    cred = pj.AuthCredInfo("digest", "*", auth_username, 0, caller_password)
    acfg.sipConfig.authCreds.append(cred)

    acc = pj.Account()
    acc.create(acfg)

    # Making a call
    call = MyCall(acc, callee_uri, audio_file)
    prm = pj.CallOpParam()
    call.makeCall(callee_uri, prm)

    print("Waiting for call to connect...")

    try:
       # Pętla oczekująca na odpowiedź callee
        while call.is_active or not call.getInfo().state == pj.PJSIP_INV_STATE_DISCONNECTED:
            time.sleep(1)  # Czekaj i sprawdzaj status co 1 sekundę
    except KeyboardInterrupt:
        print("Call interrupted by user")

    # Rozłączanie po zakończeniu
    call.hangup(pj.CallOpParam())
    ep.libDestroy()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--caller-uri", required=True)
    parser.add_argument("--caller-password", required=True)
    parser.add_argument("--callee-uri", required=True)
    parser.add_argument("--audio-file", required=True)
    parser.add_argument("--port", type=int, required=True)

    args = parser.parse_args()
    pjsua2_main(args.caller_uri, args.caller_password, args.callee_uri, args.audio_file, args.port)
