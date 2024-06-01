class RD:
    def __init__(self):
        self.value = 345552 # per block
        self.halving_cycle = 21000
        self.halving_count = 0

    def halving(self):
        if self.value % self.halving_cycle == 0:
            self.value = self.value // 2
            self.halving_count += 1
