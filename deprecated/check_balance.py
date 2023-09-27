from solathon import Client, PublicKey

client = Client("https://api.devnet.solana.com")
receiver = PublicKey("2eHKF3THqC3AMqcUhPSUhcwct7nBmUnso5aPMYqYZCK7")

balance = client.get_balance(receiver)
print("Saldo da carteira de destino:", balance)
