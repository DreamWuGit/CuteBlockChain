__author__ = 'etxxybc'
import hashlib
import  json
from  time import time
from uuid import uuid4

class BlockChain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]

    def new_block(self,proof, prevous_hash=None):
        block={"index":len(self.chain)+1,"timestamp":time(),"transactions":self.current_transactions,
               "proof":proof, "previous_hash":prevous_hash}
        self.current_transactions=[]
        self.chain.append(block)
        return block

    def hash(self,block):
        block_string=json.dumps(block,sort_keys=True).encode()
        return  hashlib.sha256(block_string).hexdigest()

    def last_block(self):
        return self.chain[-1]

    def new_transaction(self,sender, recipient,amount):
        self.current_transactions.append({"sender":sender, "recipient":recipient,"amount":amount})
        return self.last_block()["index"]+1

    def prrof_of_work(self,last_proof):
        proof=0
        while self. valid_proof(last_proof,proof) is False:
            proof +=1

        return  proof

    def valid_proof(self,last_proof,proof):
        guess="{0}{1}".format(last_proof,proof).encode()
        guess_hash=hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

