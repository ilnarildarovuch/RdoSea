from blockchain_pm import BlockChain

class RD:
    def __init__(self):
        self.blockchain = BlockChain()
        self.value = 345552 # per block
        self.halving_cycle = 21000
        self.halving_count = 0

    def halving(self):
        self.chain_size = len(self.blockchain)
        if self.chain_size * self.value % self.halving_cycle == 0:
            self.halving_count += 1
            self.value = self.value / 2
        return self.value