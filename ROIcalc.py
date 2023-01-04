class ROI:
    def __init__(self, name, income, expense, annual_cashflow):
        self.name = name
        self.income = income
        self.expense = expense
        self.annual_cashflow = annual_cashflow

    def gross_income(self):
        salary = input('Enter monthly gross income: $')
        other = input('Please enter any additional incomes. If no other incomes, please enter 0: $')
        salary_int = int(salary)
        other_int = int(other)
        total_income = salary_int + other_int
        self.income = total_income
        print(f'Gross income: ${total_income}')
        print(f'Amount Saved: ${self.income} ')

    def expenses(self):
        expense = input('Enter monthly expenses: $')
        expense_int = int(expense)
        self.expense = expense_int
        print(f'Total Expense: ${expense_int}')
    
    def net_income(self):
        monthly_cash_flow = self.income - self.expense
        self.annual_cashflow = monthly_cash_flow * 12
        print(f'Monthly Cash Flow: ${monthly_cash_flow}')
        print(f'Annual Cash Flow: ${self.annual_cashflow} ')
    
    def return_on_investment(self):
        down_payment = input('Enter downpayment: $')
        closing_costs = input('Enter closing costs?: $')
        refurbishment_budget = input('Enter refurbishment costs. If none please enter 0: $')
        misc = input('Enter misc expenses. If none please enter 0: $')
        down_payment_int  = int(down_payment)
        closing_costs_int = int(closing_costs)
        refurbishment_budget_int = int(refurbishment_budget)
        misc_int = int(misc)
        total_investment = down_payment_int + closing_costs_int + refurbishment_budget_int + misc_int
        Return_on_investment = self.annual_cashflow / total_investment
        Return_on_investment_percentage = Return_on_investment * 100
        print(f'Return on Investment: {Return_on_investment_percentage}%')


User = ROI('Savanna','tbd', 'tbd', 'tbd')

User.gross_income()
User.expenses()
User.net_income()
User.return_on_investment()