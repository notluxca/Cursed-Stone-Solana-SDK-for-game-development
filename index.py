from solathon import Client, Keypair
from solathon.utils import sol_to_lamport

client = Client("https://api.devnet.solana.com")
new_account = Keypair()
print(new_account.public_key, new_account.private_key) 
amount = sol_to_lamport(1)

res = client.request_airdrop(new_account.public_key, amount)
print("Airdrop response: ", res)

