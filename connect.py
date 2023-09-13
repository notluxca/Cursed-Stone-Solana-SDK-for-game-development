import sys

    # Example Code for blockChainWriteOperation

class LocalWallet:
    def __init__(self, value, adress) -> None:
        self.adress = adress
        ...

    def getBalance():
         ...
    



def createWallet():
    ...

def withdraw(value):
     ...


def transferBlock(value, adress):
        #transferBlock
        balance = getLocalWalletBalance()
        if value < balance:
            withdraw(value)            
            print(f"Block Sent {value} to adress {adress}")



def getLocalWalletBalance():
        # check and get balance
        balance = 12
        return balance 

def handleArgv(argv):
    if argv[1] == "help":
        print("Solana integration api")
    if argv[1] == "transfer":
        try:
            adress = argv[2]
            value = int(argv[3])

            transferBlock(value, adress)
        except Exception as error:
            print(f"Error: {error}")

    




if __name__ == "__main__":
    print("init")
    argv = sys.argv
    handleArgv(argv)


    
