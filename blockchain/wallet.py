import hashlib
import os
import time

class Wallets:
    def __init__(self):
        super().__init__()
        self.wallets = []
    def create_wallet(self, block):
        while True:
            private_key = hashlib.sha512(os.urandom(512) + os.urandom(128) + block.hash.encode() * 3 + str(block.nonce).encode()).hexdigest()
            if private_key not in self.wallets:
                break
        public_key = hashlib.sha512(private_key.encode()).hexdigest()
        self.wallets.append({private_key: public_key})
        
        wallet_block = block
        wallet_block.index = block.index + 2
        wallet_block.mine = 0
        wallet_block.data = public_key
        wallet_block.coins = 0
        wallet_block.previous_hash = block.hash
        wallet_block.hash = block.calculate_hash()

        return public_key, wallet_block
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
