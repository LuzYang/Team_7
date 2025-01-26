from coin_acceptor import CoinAcceptor
def main():
    acceptor=CoinAcceptor(0,0)
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")
    print()
    while True:
        value=float(input("Insert coin(0 return, -1 exit):"))
        if value==0:
            acceptor.returnCoins()
        elif value==-1:
            print("Exiting program.")
            break
        else:
            acceptor.insertCoin(value)
    print()
    print("Program ending.")
if __name__=="__main__":
    main()
