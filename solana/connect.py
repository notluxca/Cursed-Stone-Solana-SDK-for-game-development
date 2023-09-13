import sys
from solathon import * 
# from solathon import Client, PublicKey, Keypair ,Transaction
import ed25519
import os
    # Example Code for blockChainWriteOperation



hasWallet = False

class LocalWallet:
    def __init__(self, value, adress) -> None:
        self.adress = adress
        ...

    def getBalance():
         
         ...
    



def createWallet():
    private_key_bytes = os.urandom(32)
    private_key = ed25519.SigningKey(private_key_bytes)
    return private_key
    ...

def withdraw(value):
     ...


def transferBlock(value, adress):
        #transferBlock
        
        
        client = Client("https://api.devnet.solana.com")
        sender = Keypair.from_private_key(private_key)
        print(sender)
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
    if argv == True:
        if argv[1] == "transfer":
            try:
                adress = argv[2]
                value = int(argv[3])
                transferBlock(value, adress)
            except Exception as error:
                print(f"Error: {error}")

        




if __name__ == "__main__":
    print("Solana integration api")
    argv = sys.argv
    if hasWallet == False:
        key = createWallet()

    handleArgv(argv)


    
