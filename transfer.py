from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair
from solathon.utils import sol_to_lamport

client = Client("https://api.devnet.solana.com")

sender = Keypair().from_private_key("PnWSqwPRhbvs9oKj9Z36yCh1QiFDgdSAk64uF9EW5tniwuUPB3dXCxN5iyByowRVZmYYsDA6mmQzAMw9qsQbC5F")
receiver = PublicKey("2eHKF3THqC3AMqcUhPSUhcwct7nBmUnso5aPMYqYZCK7")
amout = sol_to_lamport(0.50)

instruction = transfer(
    from_public_key=sender.public_key,
    to_public_key=receiver,
    lamports=amout
)

transaction = Transaction(instructions=[instruction], signers=[sender])

result = client.send_transaction(transaction)
print(result)