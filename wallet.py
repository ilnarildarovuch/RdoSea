import hashlib
import os
import requests

class Wallets:
    def __init__(self):
        super().__init__()
        self.wallets = []
    def create_wallet(self):
        private_key = hashlib.sha256(requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=100&max=10000&count=15").text.encode() + os.urandom(128)).hexdigest()
        public_key = hashlib.sha256(private_key.encode()).hexdigest()
        self.wallets.append({private_key: public_key})
        return public_key
    def get_coins_from_account(self):
        pass