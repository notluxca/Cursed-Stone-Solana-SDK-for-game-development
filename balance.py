from solathon import Client, Keypair

#endereço da carteira que deseja verificar
wallet_address = "6q1rgdT9TehEP6eLv9dbfFu1NJ3DV2UF7uGQSh6fZAhE"

client = Client("https://api.devnet.solana.com")

#saldo da carteira
balance = client.get_balance(wallet_address)

print("Saldo da carteira:", balance['result']['value'])
#5KweVpwELARfDLfRiFNn948a9bCT5CatKY7iY7bboV13