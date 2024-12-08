# serwer (freeswitch + voipmonitor)

Najpierw trzeba zdobyć klucz licencyjny z https://www.voipmonitor.org/whmcs/store/gui-server-you-host, można podać kompletnie fake dane, tylko maila trzeba mieć dostęp.
Gdzieś tam dalej ze strony można zdobyć klucz w formacie .php (przycisk download gdzieś tam będzie).
Potem umieścić jego zawartość w pliku `./server/key.php`.

- Uruchomienie wszystkiego:

```bash
cd server
docker compose up --build
```
(czasami przy pierwszym buildzie ma problemy z pobieraniem plików z sourceforga, trzeba próbować do skutku...)

Jak wszystko się uruchomi to w przeglądarce można wejść na `http://localhost`.
Po jakimś czasie powinno się pokazać menu główne voipmonitora, jakieś wyskakujące komunikaty można skipnąć/zignorować/odmówić.
Ciekawą sekcją będzie "Active calls" na którą można wejść i obserwować aktywne połączenia.

## testowanie

wszystkie softphony są trochę beznadziejne... ale Linphone powinien działać:
https://www.linphone.org/en/linphone-softphone/

+ pobrać i zainstalować
+ odpalając dodać konto "Use a SIP account"
+ - username: 1000
  - SIP domain: adres IP komputera w sieci LAN (np. 192.168.0.1)
  - password: 1234 (można zmienić w configu freeswitcha)
  - transport: TCP
+ wejść w preferences
+ w zakładce network odznaczyć "Set SIP TCP/UDP port"
+ zadzwonić na 9198 aby usłyszeć muzyczkę tetrisową

Podczas rozmowy powinno być ją też widać na voipmonitorze