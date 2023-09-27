import sys
from solathon.core.instructions import transfer
from solathon import Client, Keypair, Transaction, PublicKey
from solathon.utils import sol_to_lamport


nets = thisdict = {
  "devnet": "https://api.devnet.solana.com",
  "testnet": "",
  "mainnet": ""
}
# set the new in use
client = Client("")


# create public and private key as wallet account | adress on solana blockchain
def createWallet():
    new_account = Keypair()
    print(f"Public Key: {new_account.public_key} | Private Key: {new_account.private_key}")


# check provided wallet address balance
def get_balance(wallet):
    balance = client.get_balance(wallet)
    print("Saldo da carteira:", balance['result']['value'])


# transfer sol from sender to receiver and return the transaction result, return the actual balance
def transfer(receiver_address, amount):
    sender = Keypair().from_private_key("")
    receiver = PublicKey(receiver_address)
    value = sol_to_lamport(amount)

    
    
    instruction = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver,
        lamports=value
    )
    
    
    
    transaction = Transaction(instructions=[instruction], signers=[sender])
    result = client.send_transaction(transaction)
    print(result)




# handle sys argv passed on .exe execution time, this handle the connection betwen unity and the script
def handleArgv(argv):
        
        if argv[1] == "transfer":
            try:
                adress = argv[2]
                value = int(argv[3])   
            except Exception as error:
                print(f"Error: {error}")
        if argv[1] == "test":
            createWallet()


if __name__ == "__main__":
    print("Solana integration api")
    argv = sys.argv
    handleArgv(argv)


