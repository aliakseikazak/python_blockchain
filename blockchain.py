from builtins import input, float

# Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """
    :return: the last value of the current blockchain.
    """
    return blockchain[-1]


# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]
def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.
    :argument transaction_amount: The amount that should be added
    :argument last_transaction: The last blockchain transaction (default=[1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """
    :return: the input of the user (a new transaction amount) as a float.
    """
    # Get the user input, transform it from a string to a float and store it
    user_input = float(input("Your transaction amount please: "))
    return user_input


# Get the first transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount)

# Get the second transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

# Get the third transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

# Output the blockchain list to the console
print(blockchain)
