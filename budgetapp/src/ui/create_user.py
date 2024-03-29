from tkinter import ttk, constants, StringVar
from service.budgetapp_service import budgetapp_service, UsernameTakenError


class CreateUserView:
    """Class of the create user view
    """
    def __init__(self, root, handle_create_user, handle_show_login_view):
        """Class constructor

            Args:
                root: Tk-object, represents the window
                handle_create_user: reference to method for switching view to home view
                handle_show_login_view: reference to method for switching view to login view

        """
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._username_input = None
        self._password_input = None
        self._balance_input = None
        self._income_input = None
        self._expenses_input = None
        self._error_variable = None
        self._error_label = None
        self._frame = None

        self._initialize()

    def pack(self):
        """Packs the frame
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the frame
        """
        self._frame.destroy()

    def _initialize_username_field(self):
        """Initializes username input field
        """
        label = ttk.Label(master=self._frame, text='Username')
        self._username_input = ttk.Entry(master=self._frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_input.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        """Initializes password input field
        """
        label = ttk.Label(master=self._frame, text='Password')
        self._password_input = ttk.Entry(master=self._frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_input.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_balance_field(self):
        """Initializes balance input field
        """
        label = ttk.Label(master=self._frame, text='Balance (€)')
        self._balance_input = ttk.Entry(master=self._frame)

        label.grid(padx=10, pady=10, sticky=constants.W)
        self._balance_input.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_income_field(self):
        """Initializes income input field
        """
        label = ttk.Label(master=self._frame, text='Monthly Income (€)')
        self._income_input = ttk.Entry(master=self._frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self._income_input.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_expenses_field(self):
        """Initializes expenses input field
        """
        label = ttk.Label(master=self._frame,
                          text='Monthly Recurring Expenses (€)')
        self._expenses_input = ttk.Entry(master=self._frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self._expenses_input.grid(padx=5, pady=5, sticky=constants.EW)

    def _create_user_handler(self):
        """If the conditions are met, creates new user
        """
        username = self._username_input.get()
        password = self._password_input.get()
        balance = self._balance_input.get()
        income = self._income_input.get()
        expenses = self._expenses_input.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error('Username and password is required')
            return

        try:
            balance = float(balance)
            income = float(income)
            expenses = float(expenses)

            if balance <= 0 or income <= 0 or expenses <= 0:
                self._show_error('Value above 0 required')
                return

        except:
            ValueError('The amounts must be positive numbers')
            self._show_error('The amounts must be positive numbers')
            return

        try:
            budgetapp_service.create_user(
                username, password, balance, income, expenses)
            self._handle_create_user()
        except UsernameTakenError:
            self._show_error(f'The username {username} has already been taken')

    def _show_error(self, text):
        """Shows error message

            Args:
                text: string, the error message

        """
        self._error_variable.set(text)
        self._error_label.grid()

    def _hide_error(self):
        """Hides error message
        """
        self._error_label.grid_remove()

    def _initialize(self):
        """Initializes all class-components/window features
        """
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='orange'
        )
        self._error_label.grid(row=1, column=0, padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()
        self._initialize_balance_field()
        self._initialize_income_field()
        self._initialize_expenses_field()

        login_button = ttk.Button(
            master=self._frame,
            text='Login',
            command=self._handle_show_login_view
        )
        create_user_button = ttk.Button(
            master=self._frame,
            text='Create New User',
            command=self._create_user_handler
        )
        self._frame.grid_columnconfigure(1, weight=1, minsize=200)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
