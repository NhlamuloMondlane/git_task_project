# Original Code

def check_dormant_accounts(accounts):
    """Check for dormant accounts among active client accounts."""
    dormant_accounts = []
    for account in accounts:
        if account['status'] == 'active' and account['last_activity'] < '2022-01-01':
            dormant_accounts.append(account)
    return dormant_accounts

def main():
    """Main function."""
    accounts = [
        {'id': 1, 'name': 'Client A', 'status': 'active', 'last_activity': '2021-10-15'},
        {'id': 2, 'name': 'Client B', 'status': 'active', 'last_activity': '2020-12-20'},
        {'id': 3, 'name': 'Client C', 'status': 'inactive', 'last_activity': '2021-05-30'},
    ]
    dormant_accounts = check_dormant_accounts(accounts)
    print("Dormant Accounts:")
    for account in dormant_accounts:
        print(account['name'])

if __name__ == "__main__":
    main()

# Refactored Code

def find_dormant_accounts(accounts):
    """Find dormant accounts among active client accounts."""
    dormant_accounts = []
    for account in accounts:
        if account['status'] == 'active' and account['last_activity'] < '2022-01-01':
            dormant_accounts.append(account)
    return dormant_accounts

def print_dormant_accounts(accounts):
    """Print dormant accounts."""
    print("Dormant Accounts:")
    for account in accounts:
        print(account['name'])

def main():
    """Main function."""
    accounts = [
        {'id': 1, 'name': 'Client A', 'status': 'active', 'last_activity': '2021-10-15'},
        {'id': 2, 'name': 'Client B', 'status': 'active', 'last_activity': '2020-12-20'},
        {'id': 3, 'name': 'Client C', 'status': 'inactive', 'last_activity': '2021-05-30'},
    ]
    dormant_accounts = find_dormant_accounts(accounts)
    print_dormant_accounts(dormant_accounts)

if __name__ == "__main__":
    main()
