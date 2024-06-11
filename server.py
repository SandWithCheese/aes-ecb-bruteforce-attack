from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from flask import Flask
import os

app = Flask(__name__)

KEY = os.urandom(16)
FLAG = "ini_pesan_rahasia"


@app.route("/encrypt/<plaintext>/")
def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return {"ciphertext": encrypted.hex()}


if __name__ == "__main__":
    app.run(debug=True)
