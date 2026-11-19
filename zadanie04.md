ZAD.1

curl http://localhost:5001/health
{"status":"ok"}

192.168.65.1 - - [12/Nov/2026 08:18:10] "GET /health HTTP/1.1" 200 -

ZAD.2

testowy@Mac breach-checker % docker run --rm --network breach-net healthcheck-probe
backend: OK
testowy@Mac breach-checker % docker run --rm healthcheck-probe
backend: UNREACHABLE
testowy@Mac breach-checker % docker stop backend
backend
testowy@Mac breach-checker % docker run --rm --network breach-net healthcheck-probe
backend: UNREACHABLE
testowy@Mac breach-checker % docker start backend                                  
backend

Bez flagi --network kontener uruchamia się w domyślnej sieci bridge, która nie obsługuje automatycznego rozpoznawania nazw kontenerów i jest odizolowana od sieci breach-net, w której działa backend. Dopiero podłączenie obu kontenerów do tej samej sieci utworzonej przez użytkownika pozwala wbudowanemu serwerowi DNS Dockera przetłumaczyć nazwę backend na jego wewnętrzny adres IP.

ZAD.3

Po restart:
docker exec backend cat /tmp/notatka.txt                   
notatka

Po remove:
docker exec backend cat /tmp/notatka.txt
cat: /tmp/notatka.txt: No such file or directory

historia.txt
Wed Nov 18 23:08:31 UTC 2026
Wed Nov 18 23:09:07 UTC 2026

Dlaczego plik w /tmp przetrwał restart, ale nie docker rm?
Plik zapisał się w warstwie zapisywalnej konkretnej instancji kontenera – restart jedynie zatrzymuje i wznawia procesy wewnątrz tego samego kontenera, zachowując jego system plików. Polecenie docker rm trwale usuwa cały kontener wraz z jego warstwą zapisywalną, dlatego nowo utworzony kontener startuje z czystego obrazu bez tego pliku.

Dlaczego historia.txt przetrwała usunięcie obu kontenerów?
Wolumen breach-dane jest zarządzany przez Dockera i przechowywany na dysku hosta niezależnie od cyklu życia kontenerów. Usunięcie kontenerów niszczy tylko same kontenery, pozostawiając dane w wolumenie nienaruszone.

Czy lista wycieków przetrwałaby docker rm i dlaczego?
Tak, przetrwałaby. Plik leaked-sha1.txt jest zamontowany z lokalnego systemu plików hosta za pomocą bind mounta, więc jego źródło znajduje się bezpośrednio na dysku komputera poza kontenerem . Usunięcie kontenera poleceniem docker rm nie usuwa plików zamontowanych z dysku hosta.