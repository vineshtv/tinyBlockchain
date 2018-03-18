import hashlib as hasher
import datetime as dt

'''
    The block class contains all the information regarding the block. It also contains a 
    build_hash method which generates the hash of the block
'''
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hashValue = self.build_hash()

    def build_hash(self):
        sha = hasher.sha256()
        sha.update(str(self.index) + 
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))

        return sha.hexdigest()

def create_genesis_block():
    ''' 
        This method generates the genesis block - the first block in the blockchain 
    '''
    return Block(0, dt.datetime.now(), "genesis block", "0")


def new_block(last_block):
    '''
        This method takes block and generates the next block in the chain
    '''
    this_index = last_block.index + 1
    this_timestamp = dt.datetime.now()
    this_data = "This is block number: " + str(this_index)
    this_previous_hash = last_block.previous_hash
    return Block(this_index, this_timestamp, this_data, this_previous_hash)


# Now lets generate the actual blockchain

# Generate the genesis block
tiny_blockchain = [create_genesis_block()]
previous_block = tiny_blockchain[0]

# 20 blocks in this tiny blockchain
num_blocks = 20 # apart from the genesis block

# Add the blocks to the blockchain
for i in range(0, num_blocks):
    block_to_add = new_block(previous_block)
    tiny_blockchain.append(block_to_add)
    previous_block = block_to_add

    print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    print "Hash: {}\n".format(block_to_add.hashValue) 
