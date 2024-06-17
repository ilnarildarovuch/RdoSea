import requests
import hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0, coins=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.coins = coins
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_str = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha512(hash_str.encode()).hexdigest()

public_key = input("Enter your public key :> ")

# Now it's our hash 407b96c5f0f3445ffd4e59787c6bb17454f25fc9cbd622a81ea1257bf8ddc1acf0d5817c5868306205db37d80c72bdd20be0bb2946ab8d7e723dbf75b99f9f26
#    ╱|、
#   (˚ˎ 。7  
#    |、˜〵          
#   じしˍ,)ノ

while True:
    block = Block(0, 0.0, "", "")
    difficulty = int(requests.get("http://127.0.0.1:5000/get_difficulty").text)
    block_re = eval(requests.get("http://127.0.0.1:5000/get_block").text)

    block.index = int(block_re["index"])
    block.timestamp = float(block_re["timestamp"])
    block.data = public_key
    block.previous_hash = block_re["previous_hash"]
    block.nonce = int(block_re["nonce"])
    block.coins = int(block_re["coins"])
    block.hash = block_re["hash"]

    target_hash = "0" * difficulty
    while block.hash[:difficulty] != target_hash:
        block.nonce += 1
        block.hash = block.calculate_hash()
    print("Mined block at nonce: " + str(block.nonce))
    print(requests.get(f"http://127.0.0.1:5000/send_block?index={block.index}&timestamp={block.timestamp}&data={block.data}&previous_hash={block.previous_hash}&nonce={block.nonce}&hash={block.hash}").text)