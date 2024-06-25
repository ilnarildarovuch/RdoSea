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
        self.mine = 1
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_str = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce) # i just added self.coins, i hate that, that's was 3 commits
        return hashlib.sha512(hash_str.encode()).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = []
        self.difficulty = 5
        # genesis 0	0	Good is good	125beb350e897116515abe527f24332e00426ba521c3dee3ea029f48ac6086108283f1b1ff0277802f4d21d2779b1064f822aceca19ab5d5686aba6eafc4589c	fa03ab728dbd40ea6723fb708299f2e50d9d73df8c290639dd2165bf38ac3ce0bbdc6efe2a40a5b20e962ab98ce96bf89ee10fd2a39588d27c043c755d78d921	0	0	0

    def __len__(self):
        return len(self.chain)
    
    def add_block(self, block):
        if block in self.chain:
            return "BAD", "BLOCK_ALREADY_EXISTS"
        
        if block.hash != block.calculate_hash():
            return "BAD", "HASH_ERROR"

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