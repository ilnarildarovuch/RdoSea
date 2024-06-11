import blockchain_pm
import time
import crypto
import wallet
import uvicorn
from fastapi import FastAPI
import json

app = FastAPI()
coin = crypto.RD()
coin.blockchain = blockchain_pm.open_blockchain('blockchain.xlsx', blockchain_pm.BlockChain(), blockchain_pm.Block)
coin.wallets = blockchain_pm.open_wallets('wallets.xlsx', wallet.Wallets)

@app.get("/get_difficulty")
def get_difficulty():
    return blockchain_pm.BlockChain().difficulty

@app.get("/get_block")
def get_blockchain():
    block = blockchain_pm.Block(len(coin.blockchain.chain), time.time(), "", coin.blockchain.chain[-1].hash, coins=coin.halving())
    block_dict = {"index": block.index, "timestamp": block.timestamp, "data": block.data, "previous_hash": block.previous_hash, "nonce": block.nonce, "coins": block.coins, "hash": block.hash}
    return block_dict

@app.get("/send_block")
def get_blockchain_mine(index: int, timestamp: float, data, previous_hash, nonce: int, hash):
    block = blockchain_pm.Block(0, 0.0, "", "")
    block.index = index
    block.timestamp = timestamp
    block.data = data
    block.previous_hash = previous_hash
    block.nonce = nonce
    block.coins = coin.halving()
    block.hash = hash
    blockchain_pm.save_blockchain(coin.blockchain, 'blockchain.xlsx')
    blockchain_pm.save_wallets(coin.wallets, 'wallets.xlsx')    
    return coin.blockchain.add_block(block)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)