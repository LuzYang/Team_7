class CryptoWallet:
    def __init__(self, walletId):
        self._balance = 0.0
        self._walletId = walletId
        self._transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        self._balance += amount
        self._transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return
        if amount > self._balance:
            print("Insufficient balance.")
            return
        self._balance -= amount
        self._transaction_history.append(f"Withdrew: {amount}")

    def check_balance(self):
        return self._balance

    def transaction_history(self):
        return "\n".join(self._transaction_history)


def main():
    wallets = {}
    while True:
        print("\nMenu:")
        print("1 - Create Wallet")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Check Balance")
        print("5 - Transaction History")
        print("0 - Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            wallet_id = input("Enter a wallet ID: ")
            if wallet_id in wallets:
                print("Wallet ID already exists.")
            else:
                wallets[wallet_id] = CryptoWallet(wallet_id)
                print(f"Wallet with ID {wallet_id} created.")
        
        elif choice == "2":
            wallet_id = input("Enter wallet ID: ")
            if wallet_id not in wallets:
                print("Wallet not found.")
            else:
                amount = float(input("Enter deposit amount: "))
                wallets[wallet_id].deposit(amount)
        
        elif choice == "3":
            wallet_id = input("Enter wallet ID: ")
            if wallet_id not in wallets:
                print("Wallet not found.")
            else:
                amount = float(input("Enter withdrawal amount: "))
                wallets[wallet_id].withdraw(amount)
        
        elif choice == "4":
            wallet_id = input("Enter wallet ID: ")
            if wallet_id not in wallets:
                print("Wallet not found.")
            else:
                balance = wallets[wallet_id].check_balance()
                print(f"Balance for wallet {wallet_id}: {balance}")
        
        elif choice == "5":
            wallet_id = input("Enter wallet ID: ")
            if wallet_id not in wallets:
                print("Wallet not found.")
            else:
                history = wallets[wallet_id].transaction_history()
                print(f"Transaction history for wallet {wallet_id}:\n{history}")
        
        elif choice == "0":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
