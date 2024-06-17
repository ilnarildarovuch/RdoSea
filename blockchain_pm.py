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
        hash_str = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce) # i just added self.coins, i hate that, that's was 3 commits
        return hashlib.sha512(hash_str.encode()).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = []
        self.difficulty = 5

    def __len__(self):
        return len(self.chain)
    
    def add_block(self, block):
        if block.hash != block.calculate_hash():
            print("HASH")
            return "BAD"
        
        if block.previous_hash != self.chain[-1].hash:
            print("PREVIOUS HASH")
            return "BAD"
        
        if block.hash[:self.difficulty] != "0" * self.difficulty:
            print("DIFFICULTY")
            return "BAD"
        
        if block.index < self.chain[-1].index:
            if block.hash in self.chain:
                return "UNCLE"
            print("INDEX")
            return "BAD"
        return "GOOD"