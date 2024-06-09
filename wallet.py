import hashlib
import os
import requests
import time

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
    def send_coins_to_account(self, chain, wallet_from, wallet_to, coins, Block, mine_block):
        sent_coins = 0
        for i in chain:
            if wallet_from in i.data:
                if i.coins >= coins - sent_coins:
                    i.coins -= coins - sent_coins
                    sent_coins = coins
                else:
                    sent_coins += i.coins
                    i.coins = 0
        if sent_coins < coins:
            for i in chain:
                if wallet_from in i.data:
                    if i.coins >= coins - sent_coins:
                        i.coins -= coins - sent_coins
                        sent_coins = coins
                    else:
                        sent_coins += i.coins
                        i.coins = 0
        if sent_coins < coins:
            return "Not enough coins in blocks"
        new_block = Block(len(chain), time.time(), f"{wallet_to}", chain[-1].hash, coins=coins)
        chain = mine_block(chain.difficulty, chain.chain).mine(new_block)
        return chain
