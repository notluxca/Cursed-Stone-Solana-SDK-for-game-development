import sys
from solathon.core.instructions import transfer
from solathon import Client, Keypair, Transaction, PublicKey
from solathon.utils import sol_to_lamport, lamport_to_sol


nets = thisdict = {
  "devnet": "https://api.devnet.solana.com",
  "testnet": "",
  "mainnet": ""
}
# set the new in use
client = Client("https://api.devnet.solana.com")


# create public and private key as wallet account | adress on solana blockchain
def createWallet():
    new_account = Keypair()
    print(new_account.public_key, new_account.private_key)


# check provided wallet address balance | WORKING
def get_balance(wallet):
    balance = client.get_balance(wallet)
    print(lamport_to_sol(balance['result']['value']))

# dont try to request more than 1 sol per time, it will rate limit you | WORKING
def requestAirdrop(value, pubKey):
    amount = sol_to_lamport(value)
    res = client.request_airdrop(pubKey, amount)
    print("Airdrop response: ", res)



# transfer sol from sender to receiver and return the transaction result, return the actual balance
def send(amount, sender_pk, receiver):
    client = Client("https://api.devnet.solana.com")
    sender = Keypair().from_private_key(sender_pk)
    receiver = PublicKey(receiver)
    amount = sol_to_lamport(amount)

    instruction = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver,
        lamports=amount
    )
    transaction = Transaction(instructions=[instruction], signers=[sender])
    result = client.send_transaction(transaction)
    print(result)




# handle sys argv passed on .exe execution time, this handle the connection betwen unity and the script
def handleArgv(argv):        
        if argv[1] == "transfer":
            try:
                value = float(argv[2])
                privateKey = argv[3]
                receiverKey = argv[4]
                send(value, privateKey, receiverKey)
            except Exception as error:
                print(f"Error: {error}")
                
                
        if argv[1] == "generateWallet":
            createWallet()
            
        if argv[1] == "requestAirdrop":
            value = argv[2]
            adress = argv[3]
            
            requestAirdrop(value, adress)
        if argv[1] == "getbalance":
            pubkey = argv[2]
            get_balance(pubkey)



if __name__ == "__main__":
    argv = sys.argv
    handleArgv(argv)


