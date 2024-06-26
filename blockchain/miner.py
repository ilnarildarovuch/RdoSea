class mine_block:
    """SHA 512"""
    def __init__(self, diff, chain):  
        self.difficulty = diff
        self.chain = chain
    def mine(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        block_mined = self.mine_block(new_block, self.difficulty)
        self.chain.append(block_mined)

    def mine_block(self, block, difficulty):
        target_hash = "0" * difficulty
        while block.hash[:difficulty] != target_hash:
            block.nonce += 1
            block.hash = block.calculate_hash()
        print("Mined block at nonce: " + str(block.nonce))
        return block