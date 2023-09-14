from solana. import Wallet

def createSolanaWallet():
    wallet = Wallet()
    print(f"Public Key: {wallet.pubkey}")
    print(f"Private Key: {wallet.secret_key}")  # Use with caution!
    return wallet

new_wallet = createSolanaWallet()