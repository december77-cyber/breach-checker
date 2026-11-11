# Lab 03 - Wyniki
ZAD.1

docker inspect
{"autor":"Jakub Grudzien","data":"2026-11-05","maintainer":"NGINX Docker Maintainers <docker-maint@nginx.com>"}


testowy@MacBook-Air-3 frontend % docker history kuba-frontend:v1
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
59f01c2de107   3 minutes ago   COPY . /usr/share/nginx/html # buildkit         53.2kB    buildkit.dockerfile.v0
<missing>      3 minutes ago   LABEL autor=Jakub Grudzien data=2026-11-05      0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     RUN /bin/sh -c set -x     && apkArch="$(cat …   51.5MB    buildkit.dockerfile.v0
<missing>      2 weeks ago     ENV ACME_VERSION=0.4.1                          0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     ENV NJS_RELEASE=1                               0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     ENV NJS_VERSION=1.0.2                           0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     STOPSIGNAL SIGQUIT                              0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     ENTRYPOINT ["/docker-entrypoint.sh"]            0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     COPY 30-tune-worker-processes.sh /docker-ent…   16.4kB    buildkit.dockerfile.v0
<missing>      2 weeks ago     COPY 20-envsubst-on-templates.sh /docker-ent…   12.3kB    buildkit.dockerfile.v0
<missing>      2 weeks ago     COPY 15-local-resolvers.envsh /docker-entryp…   12.3kB    buildkit.dockerfile.v0
<missing>      2 weeks ago     COPY 10-listen-on-ipv6-by-default.sh /docker…   12.3kB    buildkit.dockerfile.v0
<missing>      2 weeks ago     COPY docker-entrypoint.sh / # buildkit          8.19kB    buildkit.dockerfile.v0
<missing>      2 weeks ago     RUN /bin/sh -c set -x     && addgroup -g 101…   5.99MB    buildkit.dockerfile.v0
<missing>      2 weeks ago     ENV DYNPKG_RELEASE=1                            0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     ENV PKG_RELEASE=1                               0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     ENV NGINX_VERSION=1.31.8                        0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     LABEL maintainer=NGINX Docker Maintainers <d…   0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     CMD ["/bin/sh"]                                 0B        buildkit.dockerfile.v0
<missing>      2 weeks ago     ADD alpine-minirootfs-3.24.3-aarch64.tar.gz …   9.31MB    buildkit.dockerfile.v0

Dwie najnowsze warstwy na samej górze historii (COPY oraz LABEL) pochodzą bezpośrednio z mojego pliku Dockerfile, natomiast wszystkie pozostałe, starsze warstwy poniżej zostały odziedziczone z obrazu bazowego nginx:alpine.

Warstwy o rozmiarze 0B nie wprowadzają żadnych fizycznych zmian w systemie plików kontenera, ponieważ odpowiadają jedynie za metadane konfiguracji np takie jak LABEL, CMD.

W wyniku polecenia docker inspect etykiety z obrazu bazowego są łączone z nowymi, dlatego widoczny jest oryginalny maintainer, a gdyby w Dockerfile zdefiniowano własną etykietę o tym samym kluczu, nowa wartość nadpisałaby wpis odziedziczony z obrazu bazowego.

ZAD.2
obraz na porcie 8001: Wed Nov 11 21:21:59 UTC 2026
obraz na porcie 8002: Wed Nov 11 21:21:59 UTC 2026

docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS          PORTS               NAMES
36aa713099a8   zad2-image:latest   "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   0.0.0.0:8002->80/tcp, [::]:8002->80/tcp   zad2-contener-2
87f605d5ea7b   zad2-image:latest   "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes   0.0.0.0:8001->80/tcp, [::]:8001->80/tcp   zad2-contener

Dlaczego czas w build.txt jest taki sam w obu kontenerach i nie jest to czas ich uruchomienia?

Instrukcja RUN wykonuje się tylko raz – podczas budowania obrazu (docker build), a nie w trakcie uruchamiania kontenera. Wynik polecenia date został na stałe zapisany w statycznej warstwie systemu plików obrazu. Każdy kolejny kontener uruchomiony z tego samego obrazu korzysta z tej samej, niezmiennej warstwy bazowej, dlatego plik build.txt zawiera dokładnie tę samą datę z momentu budowy, mimo że kontenery zostały utworzone w różnym czasie co potwierdzają różne wartości w kolumnie CREATED.

ZAD3
root   /usr/share/nginx/html;

Kopiujemy pliki aplikacji do katalogu /usr/share/nginx/html, ponieważ w domyślnej konfiguracji serwera Nginx dyrektywa root wskazuje właśnie na tę ścieżkę jako główny katalog dokumentów, z którego serwowane są statyczne pliki strony WWW.

ZAD.4

testowy@Mac frontend % docker exec zad4-kontener ls /usr/share/nginx
Dockerfile
html
index.html
script.js
style.css
zadanie03.md

testowy@Mac frontend % docker exec zad4-kontener ls /usr/share/nginx/html
50x.html
build.txt
index.html


Który plik `index.html` sprawdził `htmlhint` i dlaczego build przeszedł?
Podczas etapu budowania obrazu linter `htmlhint` sprawdzał plik `index.html` Twojej aplikacji znajdujący się w katalogu roboczym (lub skopiowany na wyższym poziomie), a ponieważ Twój kod nie zawierał błędów składniowych HTML, polecenie lintera zakończyło się kodem wyjścia `0`, co pozwoliło na pomyślne ukończenie budowania.
Błąd polegał wyłącznie na logicznym przesunięciu ścieżki docelowej: Nginx serwuje stronę z `/usr/share/nginx/html`, gdzie pozostał nienaruszony domyślny plik powitalny `index.html` z obrazu bazowego, podczas gdy poprawny kod Breach Checker trafił katalog wyżej do `/usr/share/nginx/`.

ZAD.5

testowy@Mac frontend % docker rmi kuba-frontend:latest
Untagged: kuba-frontend:latest

testowy@Mac frontend % docker rmi kuba-frontend:v1    
Untagged: kuba-frontend:v1
Deleted: sha256:59f01c2de1071c34379fc6ad65b6ec770ae51fc8c95ca719e3f957568bdc60c0

Odpowiedź na pytanie: Kiedy `docker rmi` faktycznie usuwa obraz z dysku?**
Polecenie `docker rmi` usuwa fizycznie warstwy obrazu z dysku (komunikaty `Deleted`) dopiero wtedy, gdy zostanie usunięty ostatni tag wskazujący na dany identyfikator `IMAGE ID`, a z obrazu nie korzysta żaden istniejący kontener. Jeśli do danego identyfikatora obrazu przypisany jest więcej niż jeden tag, `docker rmi` wykonuje jedynie operację `Untagged`, czyli usuwa wyłącznie nazwę/etykietę, pozostawiając dane na dysku.