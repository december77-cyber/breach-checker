ZAD.1

docker compose up -d --build

[+] Building 1.8s (22/22) FINISHED                                                                                      
 => [internal] load local bake definitions                                                                         0.0s
 => => reading from stdin 1.14kB                                                                                   0.0s
 => [frontend internal] load build definition from Dockerfile                                                      0.0s
 => => transferring dockerfile: 205B                                                                               0.0s
 => [backend internal] load build definition from Dockerfile                                                       0.0s
 => => transferring dockerfile: 200B                                                                               0.0s
 => [backend internal] load metadata for docker.io/library/python:3.12-slim                                        1.5s
 => [frontend internal] load metadata for docker.io/library/nginx:alpine                                           0.2s
 => [frontend internal] load .dockerignore                                                                         0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [frontend 1/4] FROM docker.io/library/nginx:alpine@sha256:785835ea65db4bba6f021acc0f3be91b0fef76a53fe41f8588c  0.0s
 => => resolve docker.io/library/nginx:alpine@sha256:785835ea65db4bba6f021acc0f3be91b0fef76a53fe41f8588c6698d2aed  0.0s
 => [frontend internal] load build context                                                                         0.0s
 => => transferring context: 120B                                                                                  0.0s
 => CACHED [frontend 2/4] COPY index.html style.css script.js /usr/share/nginx/html/                               0.0s
 => CACHED [frontend 3/4] COPY nginx.conf /etc/nginx/conf.d/default.conf                                           0.0s
 => CACHED [frontend 4/4] RUN date > /usr/share/nginx/html/build.txt                                               0.0s
 => [frontend] exporting to image                                                                                  0.0s
 => => exporting layers                                                                                            0.0s
 => => exporting manifest sha256:1cb95d2206cac379b156c014f07d8a3fdaf903606039163d86fd0931aa067e26                  0.0s
 => => exporting config sha256:84c386445bd281adff4280149286ee18ac2cf22ff27efab2ea24a2ca3a3a2487                    0.0s
 => => exporting attestation manifest sha256:6e1f814fdad483bdbec4d91a590901a8aa600d3fcc5004ada6ea9ea1bd02fe56      0.0s
 => => exporting manifest list sha256:90cb51d0aaf432c8bdbc9ee5cb7e5db799881b6a36e8d1f7a3a920d4efc573d8             0.0s
 => => naming to docker.io/library/breach-checker-frontend:latest                                                  0.0s
 => => unpacking to docker.io/library/breach-checker-frontend:latest                                               0.0s
 => [frontend] resolving provenance for metadata file                                                              0.0s
 => [backend internal] load .dockerignore                                                                          0.0s
 => => transferring context: 78B                                                                                   0.0s
 => [backend 1/5] FROM docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365  0.0s
 => => resolve docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe  0.0s
 => [backend internal] load build context                                                                          0.0s
 => => transferring context: 63B                                                                                   0.0s
 => CACHED [backend 2/5] WORKDIR /app                                                                              0.0s
 => CACHED [backend 3/5] COPY requirements.txt .                                                                   0.0s
 => CACHED [backend 4/5] RUN pip install --no-cache-dir -r requirements.txt                                        0.0s
 => CACHED [backend 5/5] COPY app.py .                                                                             0.0s
 => [backend] exporting to image                                                                                   0.0s
 => => exporting layers                                                                                            0.0s
 => => exporting manifest sha256:c11de0cb762e0d8d6e28f0030141ea30ed771f28798f08ca3d8099b605f8eb5f                  0.0s
 => => exporting config sha256:b94b17f3e2958d7943683a3cc33edfb65eee844e08776f68c80847e65b691166                    0.0s
 => => exporting attestation manifest sha256:af89126ea1a9324cc76c8408e9aa578c6d3a57b168e233694962a71a1a6d8e05      0.0s
 => => exporting manifest list sha256:859cd57280d87b8d573df77401e32a68f8a01b77df1fa49518e783dfed27513c             0.0s
 => => naming to docker.io/library/breach-checker-backend:latest                                                   0.0s
 => => unpacking to docker.io/library/breach-checker-backend:latest                                                0.0s
 => [backend] resolving provenance for metadata file                                                               0.0s
[+] up 6/6
 ✔ Image breach-checker-frontend       Built                                                                        1.9s
 ✔ Image breach-checker-backend        Built                                                                        1.9s
 ✔ Network breach-checker_default      Created                                                                      0.0s
 ✔ Container breach-checker-db-1       Healthy                                                                      5.7s
 ✔ Container breach-checker-backend-1  Healthy                                                                     11.2s
 ✔ Container breach-checker-frontend-1 Started                                                                     11.2s


testowy@Mac breach-checker % docker compose ps

NAME                        IMAGE                     COMMAND                  SERVICE    CREATED          STATUS             PORTS
breach-checker-backend-1    breach-checker-backend    "python app.py"          backend    13 seconds ago   Up 7 seconds(healthy)    5000/tcp
breach-checker-db-1         postgres:16-alpine        "docker-entrypoint.s…"   db         13 seconds ago   Up 13 seconds (healthy)   5432/tcp
breach-checker-frontend-1   breach-checker-frontend   "/docker-entrypoint.…"   frontend   13 seconds ago   Up 2 seconds             0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
testowy@Mac breach-checker % 


ZAD.2

Po INSERT:
INSERT 0 1

Po down + up
ERROR:  duplicate key value violates unique constraint "leaked_hashes_pkey"
DETAIL:  Key (hash)=(bc45408273d7e1914b741c3407b0b559764f7876) already exists.

Po down -v + up
INSERT 0 1

Dodany skrót przetrwał docker compose down, ponieważ dane PostgreSQL są przechowywane w nazwanym wolumenie Dockera, który istnieje niezależnie od cyklu życia samych kontenerów.

ZAD.3
docker compose exec frontend nslookup backend

Server:         127.0.0.11
Address:        127.0.0.11:53

docker compose ps

NAME                        IMAGE                     COMMAND                  SERVICE    CREATED          STATUS            PORTS
breach-checker-backend-1    breach-checker-backend    "python app.py"          backend    2 minutes ago    Up 2 minutes(healthy)   5000/tcp
breach-checker-backend-2    breach-checker-backend    "python app.py"          backend    10 seconds ago   Up 9 seconds(healthy)   5000/tcp
breach-checker-backend-3    breach-checker-backend    "python app.py"          backend    10 seconds ago   Up 9 seconds(healthy)   5000/tcp
breach-checker-db-1         postgres:16-alpine        "docker-entrypoint.s…"   db         2 minutes ago    Up 2 minutes(healthy)   5432/tcp
breach-checker-frontend-1   breach-checker-frontend   "/docker-entrypoint.…"   frontend   2 minutes ago    Up 2 minutes            0.0.0.0:8080->80/tcp, [::]:8080->80/tcp


czy ten wynik polecenia dokce logs backend jest poprawny breach-checker % docker compose logs backend
backend-1  | W bazie jest 89 hashy
backend-1  |  * Serving Flask app 'app'
backend-1  |  * Debug mode: off
backend-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
backend-1  |  * Running on all addresses (0.0.0.0)
backend-1  |  * Running on http://127.0.0.1:5000
backend-1  |  * Running on http://172.19.0.3:5000
backend-1  | Press CTRL+C to quit
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:16:35] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:16:40] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:16:45] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:16:50] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:16:55] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:00] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:05] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:10] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:15] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:21] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:26] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:31] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:36] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:41] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:46] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:51] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:17:56] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:01] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:06] "GET /health HTTP/1.1" 200 -
backend-2  | W bazie jest 90 hashy
backend-2  |  * Serving Flask app 'app'
backend-2  |  * Debug mode: off
backend-2  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
backend-2  |  * Running on all addresses (0.0.0.0)
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:11] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:16] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:21] "GET /health HTTP/1.1" 200 -
backend-2  |  * Running on http://127.0.0.1:5000
backend-2  |  * Running on http://172.19.0.6:5000
backend-2  | Press CTRL+C to quit
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:18:35] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:18:40] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:18:45] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:26] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:31] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:37] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:42] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:47] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:52] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:18:57] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:02] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:07] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:18:50] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:18:55] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:00] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:05] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:10] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:15] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:20] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:25] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:30] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:36] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:41] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:46] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:51] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:19:56] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:12] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:17] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:22] "GET /health HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:20:01] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:20:06] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:20:11] "GET /health HTTP/1.1" 200 -
backend-2  | check: hash=bc454...
backend-2  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-2  | check: hash=bc454...
backend-2  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-2  | check: hash=bc454...
backend-2  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-2  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-2  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:20:16] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:20:21] "GET /health HTTP/1.1" 200 -
backend-3  | W bazie jest 90 hashy
backend-3  |  * Serving Flask app 'app'
backend-3  |  * Debug mode: off
backend-3  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
backend-3  |  * Running on all addresses (0.0.0.0)
backend-3  |  * Running on http://127.0.0.1:5000
backend-3  |  * Running on http://172.19.0.5:5000
backend-3  | Press CTRL+C to quit
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:18:35] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:18:40] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:18:45] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:20:26] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:20:31] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:20:36] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:20:41] "GET /health HTTP/1.1" 200 -
backend-2  | 127.0.0.1 - - [19/Nov/2026 08:20:46] "GET /health HTTP/1.1" 200 -
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:18:50] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:18:55] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:00] "GET /health HTTP/1.1" 200 -
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:05] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:10] "GET /health HTTP/1.1" 200 -
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:15] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:20] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:25] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:30] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:36] "GET /health HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:41] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:46] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:51] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:19:56] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:20:01] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:20:06] "GET /health HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:20:11] "GET /health HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:19:26] "POST /check HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:27] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:32] "GET /health HTTP/1.1" 200 -
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:37] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:42] "GET /health HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | check: hash=bc454...
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:47] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:53] "GET /health HTTP/1.1" 200 -
backend-3  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:20:16] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:20:21] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:20:26] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:20:31] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:20:36] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:20:41] "GET /health HTTP/1.1" 200 -
backend-3  | 127.0.0.1 - - [19/Nov/2026 08:20:46] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:19:58] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:20:03] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:20:08] "GET /health HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-1  | check: hash=bc454...
backend-1  | 172.19.0.4 - - [19/Nov/2026 08:20:12] "POST /check HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:20:13] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:20:18] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:20:23] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:20:28] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:20:33] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:20:38] "GET /health HTTP/1.1" 200 -
backend-1  | 127.0.0.1 - - [19/Nov/2026 08:20:43] "GET /health HTTP/1.1" 200 -

Nginx rozwiązuje nazwę domeny backend na adres IP tylko raz — podczas własnego startu — i zapamiętuje ten wynik w pamięci podręcznej, dlatego przed restartem frontendu cały ruch trafiał wyłącznie do pierwotnej repliki (backend-1). Dopiero po wykonaniu docker compose restart frontend Nginx ponownie odpytał wbudowany serwer DNS Dockera, pobrał listę wszystkich trzech adresów IP i zaczął rozdzielać ruch między