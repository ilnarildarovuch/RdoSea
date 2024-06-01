import blockchain_pm
import time
import crypto
import wallet

coin = crypto.RD()
coin.blockchain = blockchain_pm.open_blockchain('blockchain.xlsx', blockchain_pm.BlockChain(), blockchain_pm.Block)
coin.wallets = blockchain_pm.open_wallets('wallets.xlsx', wallet.Wallets)

miner = blockchain_pm.mine_block(coin.blockchain.difficulty, coin.blockchain.chain)

public_key = coin.wallets.create_wallet()

coin.blockchain.chain = miner.mine(blockchain_pm.Block(len(coin.blockchain.chain), time.time(), f"{public_key}", coin.blockchain.chain[-1].hash, coins=coin.halving()))
blockchain_pm.save_blockchain(coin.blockchain, 'blockchain.xlsx')
blockchain_pm.save_wallets(coin.wallets, 'wallets.xlsx')