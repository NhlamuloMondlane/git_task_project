class Account:
    def __init__(self, account_number, balance, parent_entity, transactional_banker):
        """
        Initialize an account.

        Args:
            account_number (str): The account number.
            balance (float): The balance of the account.
            parent_entity (str): The parent entity associated with the account.
            transactional_banker (str): The transactional banker associated with the account.
        """
        self.account_number = account_number
        self.balance = balance
        self.parent_entity = parent_entity
        self.transactional_banker = transactional_banker
