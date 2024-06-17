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
        if block in self.chain:
            return "BAD", "BLOCK_ALREADY_EXISTS"
        
        if block.hash != block.calculate_hash():
            return "BAD", "HASH_ERROR"
        
        found_nonce = False
        for i in range(block.nonce + 1):
            temp_block = Block(block.index, block.timestamp, block.data, block.previous_hash, i, block.coins)
            if temp_block.hash[:self.difficulty] == "0" * self.difficulty:
                found_nonce = True
                break
        if not found_nonce:
            return "BAD", "INVALID_NONCE"

        if block.previous_hash != self.chain[-1].hash:
            return "BAD", "INVALID_PREVIOUS_HASH"
        
        if block.hash[:self.difficulty] != "0" * self.difficulty:
            return "BAD", "INVALID_DIFFICULTY"
        
        if block.index < len(self) - 1:
            return "BAD", "INDEX_ERROR"

        if block.timestamp < self.chain[-1].timestamp:
            return "BAD", "INVALID_TIMESTAMP"
        self.chain.append(block)
        return "GOOD"