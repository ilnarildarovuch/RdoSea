import hashlib
from miner import mine_block
from save_blocks import open_blockchain, save_blockchain

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_str = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha512(hash_str.encode()).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = []
        self.difficulty = 4