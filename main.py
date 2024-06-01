import hashlib
import time
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
        # self.create_genesis_block()
        self.difficulty = 4  # adjust the difficulty level here

    # def create_genesis_block(self):
    #     genesis_block = Block(0, time.time(), "Genesis", "0")
    #     self.chain.append(genesis_block)

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        block_mined = mine_block(new_block, self.difficulty)
        self.chain.append(block_mined)


if __name__ == '__main__':
    block_chain = open_blockchain('blockchain.xlsx', BlockChain(), Block)
    while True:
        block = Block(len(block_chain.chain), time.time(), f"Rdosea", block_chain.chain[-1].hash)
        block_chain.add_block(block)
        try:
            save_blockchain(block_chain, 'blockchain.xlsx')
        except Exception:
            try:
                time.sleep(15)
                save_blockchain(block_chain, 'blockchain.xlsx')
            except Exception:
                save_blockchain(block_chain, 'blockchain.xlsx')
                break