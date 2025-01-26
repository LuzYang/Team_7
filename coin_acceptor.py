class CoinAcceptor:
    amount:int
    value:float
    def __init__(self,amount=0,value=0.0):
        self.amount=amount
        self.value=value
    def insertCoin(self,coin_value):
        print("Inserting...")
        self.amount+=1
        self.value+=coin_value
        print(f"Inserted coins = {self.amount}, value = {self.value}€")
    def getAmount(self):
        print(f"Currently '{self.amount}' coins in coin acceptor")
    def returnCoins(self)->tuple:
        print("Returning coins...")
        print(f"{self.amount} coins with {self.value}€ value returned.")
        self.amount=0
        self.value=0
        

