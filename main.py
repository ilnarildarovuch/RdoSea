import blockchain_pm
import time

blockchain = blockchain_pm.open_blockchain('blockchain.xlsx', blockchain_pm.BlockChain(), blockchain_pm.Block)

miner = blockchain_pm.mine_block(blockchain.difficulty, blockchain.chain)

blockchain.chain = miner.mine(blockchain_pm.Block(len(blockchain.chain), time.time(), f"Rdosea", blockchain.chain[-1].hash))

blockchain_pm.save_blockchain(blockchain, 'blockchain.xlsx')