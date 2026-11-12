import os
import re  # Wymagane do walidacji wyrażeń regularnych

from flask import Flask, jsonify, request
from flask_cors import CORS

HASHES_FILE = os.environ.get("HASHES_FILE", "/app/data/leaked-sha1.txt")

app = Flask(__name__)
CORS(app, origins=["http://localhost:8080"])


def load_hashes():
    with open(HASHES_FILE, encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}


KNOWN_HASHES = load_hashes()
print(f"Wczytano {len(KNOWN_HASHES)} hashy z {HASHES_FILE}", flush=True)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/check")
def check():
    data = request.get_json(silent=True) or {}
    if "hash" not in data:
        return jsonify({"error": "brak pola 'hash'"}), 400

    h = str(data["hash"]).lower()

    # Krok 3: Sprawdzenie poprawności formatu SHA-1 (40 znaków heksadecymalnych) przed zalogowaniem
    if not re.fullmatch(r"[0-9a-f]{40}", h):
        return jsonify({"error": "niepoprawny format hasha"}), 400

    # Krok 3: W logu zapisujemy tylko początek skrótu (np. 5 pierwszych znaków)
    print(f"check: hash={h[:5]}", flush=True)

    # TODO 1: sprawdź, czy h należy do zbioru KNOWN_HASHES
    found = h in KNOWN_HASHES

    # TODO 2: zwróć JSON {"found": found}
    return jsonify({"found": found})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)