import time
import hashlib

# Block Class
class Block():
    #Constructor
    def __init__(self, data, time):
        self.data = data
        self.time = time
        self.nonce = 0
        self.hash()

    def hash(self):
        hash_key = hashlib.sha256()
        msg = str(self.data) + str(self.time) + str(self.nonce)
        byte_msg = msg.encode()
        hash_key.update(byte_msg)
        self.cur_hash = hash_key.hexdigest()
        while not self.cur_hash[0:3] == '000':
          self.nonce += 1
          msg = str(self.data) + str(self.time) + str(self.nonce)
          byte_msg = msg.encode()
          hash_key.update(byte_msg)
          self.cur_hash = hash_key.hexdigest()

#------------------------------------------------------------------------------
# Authenticates block
def authenticator(block, blockchain):
    if int(block.data) % 2 == 0 :
        blockchain.append(block)
        print("This is a valid block.")
        for i in blockchain:
            print(",-----------------------------------,")
            print("|This block's identity is: %8s"  % blockchain.index(i), "|")
            print("|The data stored inside is: %7s"  % i.data, "|")
            print("|The time of genesis is: %10s" % i.time, "|")
            print("|The nonce is: %20s" % i.nonce, "|")
            print("`-----------------------------------'")
            print("The hash for this block is: \n\t", i.cur_hash)

    else:
        print("Invalid Block.")
#------------------------------------------------------------------------------

blockchain = []

#------------------------------------------------------------------------------

while True:
    data = input("What number would you like stored in the block? ")

    if data == 'x':
        exit(0)

    B = Block(data,int(time.time()))

    authenticator(B, blockchain)

## TODO prev_hash
##
## h = prev_block.hash( all data members except for cur_hash)
## if h == prev_block.cur_hash
##     prev_block is valid and the new block is added
## else
##     prev_block is invalid / altered and new block is not added
