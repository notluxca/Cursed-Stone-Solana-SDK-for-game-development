from solathon import Client, Keypair

#endereço da carteira que deseja verificar
wallet_address = "8rZdhnRN3VarLqS5RbDN218tCdPzfRGDpdixqRzB9A8n"

client = Client("https://api.devnet.solana.com")

#saldo da carteira
balance = client.get_balance(wallet_address)

print("Saldo da carteira:", balance['result']['value'])
#5KweVpwELARfDLfRiFNn948a9bCT5CatKY7iY7bboV13