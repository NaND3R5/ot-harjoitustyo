class User:
    '''Class that represents the user

    Attributes:
        username: string , represents the users username
        password: string , represents the users password
        balance: float , represents the users current balance
        income: float , represents the users current monthly income
        expenses: float , represents the users monthly recurring expenses
    '''

    def __init__(self, username, password, balance, income, expenses):
        '''Class constructor, makes new user.

        Args:
            username: string , represents the users username
            password: string , represents the users password
            balance: float , represents the users current balance
            income: float , represents the users current monthly income
            expenses: float , represents the users monthly recurring expenses

        '''

        self.username = username
        self.password = password
        self.balance = balance
        self.income = income
        self.expenses = expenses
