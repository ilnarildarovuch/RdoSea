import blockchain_pm
import time
import crypto

coin = crypto.RD()
coin.blockchain = blockchain_pm.open_blockchain('blockchain.xlsx', blockchain_pm.BlockChain(), blockchain_pm.Block)

miner = blockchain_pm.mine_block(coin.blockchain.difficulty, coin.blockchain.chain)
while True:
    coin.blockchain.chain = miner.mine(blockchain_pm.Block(len(coin.blockchain.chain), time.time(), f"Rdosea ({coin.halving()} RD)", coin.blockchain.chain[-1].hash))
    blockchain_pm.save_blockchain(coin.blockchain, 'blockchain.xlsx')