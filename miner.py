def mine_block(block, difficulty):
    """SHA 512"""
    target_hash = "0" * difficulty
    while block.hash[:difficulty] != target_hash:
        block.nonce += 1
        block.hash = block.calculate_hash()
    print("Mined block at nonce: " + str(block.nonce))
    return block