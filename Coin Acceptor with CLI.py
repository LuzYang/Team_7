class CoinAcceptor:
    def __init__(self):
        self.coins = 0
        self.total_value = 0.0

    def insert_coin(self, coin_value: float):
        if coin_value > 0:
            self.coins += 1
            self.total_value += coin_value
            print(f"Inserting...\nInserted coins = {self.coins}, value = {self.total_value}€")
        elif coin_value == 0:
            return self.return_coins()
    
    def return_coins(self) -> tuple:
        print(f"Returning coins...\n{self.coins} coins with {self.total_value}€ value returned.")
        self.coins = 0
        self.total_value = 0.0
        return self.coins, self.total_value


def main():
    coin_acceptor = CoinAcceptor()
    print("Program Starting.")
    print("Welcome To The Coin Acceptor Program.")
    
    while True:
        try:
            coin_value = float(input("Insert coin(0 return, -1 exit): "))
            
            if coin_value == -1:
                print("Exiting program.")
                break
            elif coin_value == 0:
                coin_acceptor.insert_coin(coin_value)
            elif coin_value > 0:
                coin_acceptor.insert_coin(coin_value)
            else:
                print("Invalid coin value. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid coin value.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
