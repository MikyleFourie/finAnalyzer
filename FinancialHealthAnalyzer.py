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
    
    #Converts income from Dollars to Rand where the exchange rate is $1 = R20
    def total_revenue_C(self):
        return self.total_revenue() * 20

    #Adds together all transactions labeled "Expense"
    def total_expenses(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Expense")

    #Subtracts the Expenses from Revenue to find Profit
    def profit(self):
        return self.total_revenue_C() - self.total_expenses()

    #Divides Profit by Revenue to obtain Profit Margin
    def profit_margin(self):
        return self.profit() / self.total_revenue_C()
    
    #Finds the Average Transaction Amount by dividing (TotalRevenue-TotalExpenses) by Amount of transactions
    #i.e., Profit / Number of Transactions
    def average_transaction_amount(self):
        return self.profit() / len(self.transactions)

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
        #Test data for a Healthy case                               #Expected results for current Test Data:
        transactions_data_H = [                                     #Total Revenue:             2500
            FinancialTransaction("2024-01-01", "Income", 1000),     #Total Converted Revenue:   50000
            FinancialTransaction("2024-01-02", "Expense", 500),     #Total Expenses:            800
            FinancialTransaction("2024-01-03", "Expense", 300),     #Profit:                    49200
            FinancialTransaction("2024-01-04", "Income", 1500)      #Profit Margin:             0.984
        ]                                                           #Ave Transaction Amount:    12300
        self.transactions = transactions_data_H                     #Financial Health:          Healthy
        #comment above line to exclude, remove comment to test

        #Test data for a Warning case                               #Expected results for current Test Data:
        transactions_data_W = [                                     #Total Revenue:             35
            FinancialTransaction("2024-01-01", "Income", 15),       #Total Converted Revenue:   700
            FinancialTransaction("2024-01-02", "Income", 20),       #Total Expenses:            1700
            FinancialTransaction("2024-01-03", "Expense", 1200),    #Profit:                    -1000
            FinancialTransaction("2024-01-04", "Expense", 500)      #Profit Margin:             -1.4285714
        ]                                                           #Ave Transaction Amount:    -250
        #self.transactions = transactions_data_W                     #Financial Health:          Warning
        #comment above line  to exclude, remove comment to test

    #Test case example that returns total revenue. Inluded as a tutorial for basis of other test cases.
    def test_total_revenue(self):
        testAnalyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(testAnalyzer.total_revenue(), 2500)
        #self.assertEqual(testAnalyzer.total_revenue(), 35)

    #Test case that returns the value of the total revenue after being converted from dollars to rand
    def test_total_revenue_C(self):
        testAnalyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(testAnalyzer.total_revenue_C(), 50000)
        #self.assertEqual(testAnalyzer.total_revenue_C(), 700)

    #Test case that returns total expenses
    def test_total_expenses(self):
        testAnalyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(testAnalyzer.total_expenses(), 800)
        #self.assertEqual(testAnalyzer.total_expenses(), 1700)

    #Test case that returns total profit compared to a static value
    def test_profit1(self):
        testAnalyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(testAnalyzer.profit(), 49200)
        #self.assertEqual(testAnalyzer.profit(), -1000)

    #Test case that returns total profit compared to a calculation of outputs from previous functions
    def test_profit2(self):
        testAnalyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(testAnalyzer.profit(), testAnalyzer.total_revenue_C() - testAnalyzer.total_expenses())

    #Test case that returns profit margin. Almost equal to check approximate data up to 7 decimal places
    def test_profit_margin(self):
        testAnalyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertAlmostEqual(testAnalyzer.profit_margin(), 0.984)
        #self.assertAlmostEqual(testAnalyzer.profit_margin(), (-1.4285714))

    #Test case that returns average transaction amount
    def test_average_transaction_amount(self):
        testAnalyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(testAnalyzer.average_transaction_amount(), 12300)
        #self.assertEqual(testAnalyzer.average_transaction_amount(), -250)

    #Test case that checks financial health
    def test_financial_health(self):
        testAnalyzer = FinancialHealthAnalyzer(self.transactions)
        profLoss = testAnalyzer.total_revenue_C() - testAnalyzer.total_expenses()

        if testAnalyzer.financial_health() == "Healthy":
            self.assertGreater(profLoss, -1)
        elif testAnalyzer.financial_health() == "Warning":
            self.assertTrue( -1000 <= profLoss < 0)
        elif testAnalyzer.financial_health() == "Critical":
            self.assertLess(profLoss, -1000)



#Main function is where your code starts to run. Methods need to be compiled correctly before they can be called from main    
if __name__ == '__main__':
    #Do not change the transaction data, this data needs to produce the correct output stated in the lab brief
    #List of transactions to be processed for the correct outputs as per lab brief
    transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 50),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 75)
        ]
    FinancialHealthAnalyzer.transactions = transactions_data    #loads the list into class
    analyzer = FinancialHealthAnalyzer(FinancialHealthAnalyzer.transactions)
    print("Profit: ", analyzer.profit())
    print("Profit margin: ", analyzer.profit_margin())
    print("Average transaction amount: ", analyzer.average_transaction_amount())
    print("Financial health: ", analyzer.financial_health())
    unittest.main(verbosity=2)
    