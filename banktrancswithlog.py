import logging
from twilio.rest import Client
from datetime import datetime
now=datetime.now()

logging.basicConfig(filename='bank_transactions.log',level=logging.INFO)

logging.getLogger("twilio").setLevel(logging.WARNING)

class InvalidAccountError(Exception):
    def __init__(self, message="Invalid account operation"):
        self.message = message
        super().__init__(self.message)

class BankAccount:
    def __init__(self, account_number, balance, phone_number):
        self.account_number = account_number
        self.balance = balance
        self.phone_number = phone_number

        # Twilio credentials (replace with your actual credentials)
        self.account_sid = ''
        self.auth_token = ''
        self.twilio_number = '+'

        self.client = Client(self.account_sid, self.auth_token)
        logging.info(f"Account Created:{self.account_number},initial balance: ${self.balance} Logging Time: {now.strftime('%d-%m-%Y %I:%M:%S %p')}")

    def send_sms(self, message):
        try:
            self.client.messages.create(
            body=message,
            from_=self.twilio_number,
            to=self.phone_number
            )
            logging.info(f"SMS sent to {self.phone_number} :{message}")
        except Exception as e:
            logging.error(f"Failed to send SMS to {self.phone_number}: {e}")
          
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InvalidAccountError("Insufficient funds for withdrawal")
            self.balance -= amount
            msg = f"Withdrawal of ${amount} successful. Available balance: ${self.balance} Withdraw Time: {now.strftime('%d-%m-%Y %I:%M:%S %p')}" 
            self.send_sms(msg)
            logging.info(f"{msg} (Account: {self.account_number} Withdraw Time: {now.strftime('%d-%m-%Y %I:%M:%S %p')})")
            return self.balance
        except InvalidAccountError as e:
            error_msg =f"Withdrawal failed: {e}"
            self.send_sms(error_msg)
            logging.warning(f"{error_msg} (Account:{self.account_number})")
            raise
            
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise InvalidAccountError("Deposit amount must be positive")
            self.balance += amount
            msg = f"Deposit of ${amount} successful. Available balance: ${self.balance} Deposit Time: {now.strftime('%d-%m-%Y %I:%M:%S %p')}"
            self.send_sms(msg)
            logging.info(f"{msg} (Account: {self.account_number} Deposit Time: {now.strftime('%d-%m-%Y %I:%M:%S %p')})")
            return self.balance 
        except InvalidAccountError as e:
            error_msg =f"Deposit failed :{e}"
            self.send_sms(error_msg)
            logging.warning(f"{error_msg} (Account: {self.account_number})")
            raise



# Sample usage
try:
    account = BankAccount("U0998XXXXXX97", 10000, "+") 

    try:
        withdraw_amount = float(input("Enter amount to withdraw ($): "))
        account.withdraw(withdraw_amount)
    except InvalidAccountError as e:
        print(f"Custom exception caught: {e}")
    finally:
        print("Withdrawal attempt completed.")
        logging.info("Withdrawal attempt completed: ")

    try:
        deposit_amount = float(input("Enter amount to deposit ($): "))
        account.deposit(deposit_amount)
    except InvalidAccountError as e:
        print(f"Custom exception caught during deposit: {e}")
    finally:
        print("Deposit attempt completed.") 
        logging.info("Deposit attempt Completed.")   

except Exception as e:
    print(f"Unexpected error: {e}")
    logging.critical(f"Unexpected error:{e}")