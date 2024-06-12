import hashlib
from miner import mine_block
from save import open_blockchain, save_blockchain, open_wallets, save_wallets

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0, coins=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.coins = coins
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_str = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha512(hash_str.encode()).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = []
        self.difficulty = 5
    def __len__(self):
        return len(self.chain)
    def add_block(self, block):
        # if len(block.hash) != 64:
        #     print(64)
        #     return "BAD"
        # if int(block.hash, 16) < int("0" * self.difficulty, 16):
        #     print("AGREE")
        #     if block.previous_hash == self.chain[-1].hash and block.index > len(self.chain) - 1:
        #         print("GOOD")
        #         self.chain.append(block)
        #         return "GOOD"
        #     block.index = 0 - block.index
        #     block.coins /= 6
        #     print("UPDATED BLOCK")
        #     self.chain.append(block)
        #     return "UNCLE"
        # print("ALL IS BAD")
        # return "BAD"
    # yes, this is pretty bad
    self.chain.append(block)