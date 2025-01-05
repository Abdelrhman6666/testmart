import os

class BankAccount:
    def __init__(self, name, accountType, balance=0):
        """Initialize the bank account with username, account type, balance, and a unique ID"""
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.user_id = self.generate_user_id()
        
        # Create a transaction file with a specific naming format
        self.transaction_file = f"{self.name}_{self.accountType}_{self.user_id}.txt"
        self.create_transaction_file()
        
    def generate_user_id(self):
        """Generate a unique user ID (using a simple counter for simplicity)"""
        return hash(self.name + self.accountType) % 10000  # Simplified user ID generation

    def create_transaction_file(self):
        """Create a new file for storing transactions"""
        if not os.path.exists(self.transaction_file):
            with open(self.transaction_file, 'w') as file:
                file.write("Transaction History for account: " + self.transaction_file + "\n")
                file.write("==========================================\n")
                file.write(f"Initial Balance: ${self.balance}\n")
                file.write("==========================================\n")

    def deposit(self, amount):
        """Deposit money into the account and log the transaction"""
        if amount > 0:
            self.balance += amount
            self.log_transaction(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance is available"""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.log_transaction(f"Withdrew: ${amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    
    def log_transaction(self, transaction):
        """Log the transaction to the statement file"""
        with open(self.transaction_file, 'a') as file:
            file.write(f"{transaction} | New Balance: ${self.balance}\n")
    
    def get_balance(self):
        """Return the current account balance"""
        return self.balance

    def get_user_id(self):
        """Return the user ID"""
        return self.user_id
    
    def get_username(self):
        """Return the username"""
        return self.name
    
    def get_account_type(self):
        """Return the account type"""
        return self.accountType
    
    def get_transaction_history(self):
        """Return the transaction history from the file"""
        if os.path.exists(self.transaction_file):
            with open(self.transaction_file, 'r') as file:
                history = file.read()
                print(history)
        else:
            print("No transaction history found.")

# Test the code
if __name__ == "__main__":
    # Create multiple bank account objects
    account1 = BankAccount("JohnDoe", "chequing", 500)
    account2 = BankAccount("JaneSmith", "savings", 1000)

    # Perform some transactions
    account1.deposit(200)
    account1.withdraw(100)
    account2.deposit(500)
    account2.withdraw(200)

    # Get the transaction history
    account1.get_transaction_history()
    account2.get_transaction_history()

    # Display balances and account details
    print(f"{account1.get_username()}'s Balance: ${account1.get_balance()}")
    print(f"{account2.get_username()}'s Balance: ${account2.get_balance()}")
