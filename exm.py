import sys

sys.path.insert(0, 'blockchain')

import blockchain_pm
import time
import crypto
import wallet

coin = crypto.RD()
coin.blockchain = blockchain_pm.open_blockchain('blockchain.xlsx', blockchain_pm.BlockChain(), blockchain_pm.Block)
coin.wallets = blockchain_pm.open_wallets('wallets.xlsx', wallet.Wallets)

public_key, new_wallet_block = coin.wallets.create_wallet(coin.blockchain.chain[-1])
coin.blockchain.chain.append(new_wallet_block)

miner = blockchain_pm.mine_block(coin.blockchain.difficulty, coin.blockchain.chain)

miner.mine(blockchain_pm.Block(len(coin.blockchain.chain), time.time(), f"{public_key}", coin.blockchain.chain[-1].hash, coins=coin.halving()))

coin.blockchain.chain = miner.chain
blockchain_pm.save_blockchain(coin.blockchain, 'blockchain.xlsx')
blockchain_pm.save_wallets(coin.wallets, 'wallets.xlsx')