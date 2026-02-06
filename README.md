# 🏦 Bank Account Management System with SMS Notifications

This project is a **Python-based bank account management system** that demonstrates how core banking operations like **deposit** and **withdrawal** can be implemented with:

- Custom exception handling  
- Logging of transactions  
- Real-time SMS notifications using **Twilio**  
- Clean, object-oriented design  

It’s ideal for learning **Python OOP**, **error handling**, **logging**, and **third-party API integration**.

---

## ✨ Features

- ✅ Create a bank account with an initial balance  
- 💸 Withdraw money with balance validation  
- 💰 Deposit money with input validation  
- 📩 Receive SMS alerts for every transaction  
- 🧾 Log all activities to a file  
- ⚠️ Custom exceptions for invalid operations  

---

## 🛠️ Technologies Used

- **Python 3**
- **Twilio REST API** (for SMS notifications)
- **logging module** (for transaction logs)
- **datetime module** (for timestamps)

---
## 🚀 How It Works

### Account Creation

A bank account is initialized with the following details:

- **Account number**
- **Initial balance**
- **User phone number**



## Withdrawal Operation

The withdrawal process follows these steps:

- Verifies whether the withdrawal amount exceeds the available balance  
- Raises a **custom exception** if funds are insufficient  
- Sends an **SMS notification** to the registered phone number  
- Logs the transaction details  

### Deposit Operation

The deposit process includes:

- Validation to ensure the deposit amount is **positive**  
- Updating the **account balance**  
- Sending an **SMS confirmation** to the registered phone number  
- Logging the **transaction details**  

### 🧾 Logging

All system activities are logged to the file **`bank_transactions.log`**, including:

- Account creation events  
- Successful deposits and withdrawals  
- Failed transaction attempts  
- SMS sending status  
- Critical and unexpected system errors  
****

### 📩 SMS Notifications

Each transaction triggers an SMS notification:

- ✅ **Success messages** for deposits and withdrawals  
- ❌ **Failure messages** for invalid operations  

If an SMS fails to send, the error is logged without interrupting program execution.


