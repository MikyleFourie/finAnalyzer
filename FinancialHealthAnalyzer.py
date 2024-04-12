import unittest
from io import StringIO

#FinancialTransaction class allows for the program to read FinancialTransaction data found in test setUp and main below.
#This class does not need to be edited -----------------------------------------------------------
class FinancialTransaction:
    def __init__(self, date, type, amount):
        self.date = date
        self.type = type
        self.amount = amount

    @staticmethod
    def from_line(line):
        parts = line.strip().split(',')
        date, type, amount = parts[0], parts[1], float(parts[2])
        return FinancialTransaction(date, type, amount)
#-------------------------------------------------------------------------------------------------


class FinancialHealthAnalyzer:
    def __init__(self, transactions):
        self.transactions = transactions

    #Adds together all transactions labeled "Income"
    def total_revenue(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Income")

    #Adds together all transactions labeled "Expense"
    def total_expenses(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Expense")

    #Subtracts the Expenses from Revenue to find Profit
    def profit(self):
        return self.total_revenue() - self.total_expenses() #NEED TO CHECK IF THIS WORKS

    #Divides Profit by Revenue to abtain Profit Margin
    def profit_margin(self):
        return self.profit() / self.total_revenue()
    
    #Finds the Average Transaction Amount by dividing (TotalRevenue-TotalExpenses) by Amount of transactions
    #i.e., Profit / Number of Transactions
    def average_transaction_amount(self):
        #return self.profit() / len(self.transactions)
        return len(self.transactions) #just testing if len works. Expecting output to be 4

    #Determines finalncial health and returns the corresponding string
    def financial_health(self):
        profit = self.profit()
        if profit >= 0:
            return "Healthy"
        elif -1000 >= profit < 0:
            return "Warning"
        else:
            return "Critical"

class TestFinancialHealthAnalyzer(unittest.TestCase):
    #Setup data allows for code to be tested without manually writing test transaction code for every test function. 
    #setUp transaction data and structure may be changed to include more test functions.
    def setUp(self):
        transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 1000),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 1500)
        ]
        self.transactions = transactions_data

    #Test case example that returns total revenue. Inluded as a tutorial for basis of other test cases.
    def test_total_revenue(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_revenue(), 2500)

    def test_total_expenses(self):
    #This code needs to be completed
    def test_profit(self):
    #This code needs to be completed

    #Additional testing methods might be required. test_total_revenue can be changed/expanded

#Main function is where your code starts to run. Methods need to be compiled correctly before they can be called from main    
if __name__ == '__main__':
    #Do not change the transaction data, this data needs to produce the correct output stated in the lab brief
    transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 50),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 75)
        ]
    FinancialHealthAnalyzer.transactions = transactions_data
    analyzer = FinancialHealthAnalyzer(FinancialHealthAnalyzer.transactions)
    print("Profit: ")
    print("Profit margin: ")
    print("Average transaction amount: ")
    print("Financial health: ")
    unittest.main()
    