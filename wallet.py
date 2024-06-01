import hashlib
import os
import requests

class Wallets:
    def __init__(self):
        super().__init__()
        self.wallets = []
    def create_wallet(self):
        while True:
            private_key = hashlib.sha512(requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=100&max=10000&count=15").text.encode() + os.urandom(128)).hexdigest()
            if private_key not in self.wallets:
                break
        public_key = hashlib.sha512(private_key.encode()).hexdigest()
        self.wallets.append({private_key: public_key})
        return public_key
    def get_coins_from_account(self, chain, wallet):
        coins = 0
        for i in chain:
            if wallet in i.data:
                coins += i.coins
        return coins