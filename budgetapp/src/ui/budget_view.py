from tkinter import ttk, constants
from service.budgetapp_service import budgetapp_service


class BudgetListView:
    def __init__(self,root,budgets, handle_delete_one):
        self._root = root
        self._budgets = budgets
        self._handle_delete_one= handle_delete_one
        self._frame =None

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_budget_item(self, budget):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=self._frame, text = budget.name)

        delete_budget_button= ttk.Button(
            master=self._frame,
            text='Delete',
            command=lambda: self._handle_delete_one_budget(budget.id)
        )
        label.grid(row=0 ,column=0,padx=10,pady=10,sticky=constants.W)
        delete_budget_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for budget in self._budgets:
            self._initialize_budget_item(budget)


class BudgetView:
    def __init__(self, root, handle_logout, handle_show_purchases):
        self._root = root
        self._handle_logout = handle_logout
        self._handle_show_purchases = handle_show_purchases
        self._user = budgetapp_service.current_user()
        
        self._budget_list_view = None
        self._budget_list_frame = None

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        budgetapp_service.logout()
        self._handle_logout()

    def _handle_delete_one_budget(self, budget_id):
        budgetapp_service.delete_one(budget_id)
        self._initialize_budget_list()

    def _initialize_budget_list(self):
        if self._budget_list_view:
            self._budget_list_view.destroy()

        budgets = budgetapp_service.fetch_user_budgets()

        self._budget_list_view = BudgetListView(
            self._budget_list_frame,
            budgets,
            self._handle_delete_one_budget
        )

        self._budget_list_view.pack()

    def _initialize_header(self):
        label = ttk.Label(
            master=self._frame,
            text=f'Logged in as testing'
        )
        logout_button = ttk.Button(
            master=self._frame,
            text='Logout',
            command=self._logout_handler
        )
        label.grid(row=1, column=0, padx=10, pady=10, sticky=constants.W)
        logout_button.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

    def _initialize_footer(self):

        purchase_history_button = ttk.Button(
            master=self._frame,
            text = 'View Purchase History',
            command=self._handle_show_purchases
        )
        purchase_history_button.grid(
            row=2,
            column=1,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._budget_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_budget_list()
        self._initialize_footer()

        self._budget_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_configure(1, weight=1, minsize=600)
        self._frame.grid_columnconfigure(1, weight=0)
