import sys
import base58
import codecs
from solathon import * 
import ed25519
import os
# from solathon import Client, PublicKey, Keypair ,Transaction
# Example Code for blockChainWriteOperation



def test():
    private_key_bytes = os.urandom(32)
    private_key = ed25519.SigningKey(private_key_bytes)
    return private_key
    ...


def createWallet():
    
    private_key_bytes = os.urandom(32)
    private_key = ed25519.SigningKey(private_key_bytes)
    
    solana_private_key_base58 = base58.b58encode(private_key.to_bytes()).decode('utf-8')
    public = private_key.get_verifying_key()
    public = base58.b58encode(public.to_bytes()).decode('utf-8')
    
    print("Private ", solana_private_key_base58)
    print("public ", public)

    
    
    return private_key

    


def transferBlock(value, adress):
        #transferBlock        
        client = Client("https://api.devnet.solana.com")
        sender = Keypair.from_private_key(private_key)
        
        receiver = PublicKey("receiver_public_key")
        amount = 100  

        instruction = transfer(
            from_public_key=sender.public_key,
            to_public_key=receiver, 
            lamports=100
            )

        transaction = Transaction(instructions=[instruction], signers=[sender])

        result = client.send_transaction(transaction)
        print("Transaction response: ", result)
        balance = getLocalWalletBalance()
        if value < balance:
            withdraw(value)            
            print(f"Block Sent {value} to adress {adress}")



def getLocalWalletBalance():
        # check and get balance
        balance = 12
        return balance 

def handleArgv(argv):
        if argv[1] == "transfer":
            try:
                adress = argv[2]
                value = int(argv[3])
                transferBlock(value, adress)
            except Exception as error:
                print(f"Error: {error}")
        if argv[1] == "test":
             key = createWallet()
             print(key)

        




if __name__ == "__main__":
    print("Solana integration api")

    argv = sys.argv
    handleArgv(argv)




    # if hasWallet == False:
    #    key = createWallet()


    
