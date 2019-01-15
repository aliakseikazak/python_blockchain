# Initializing our (empty) blockchain list
blockchain = []
open_transactions = []
owner = "Aliaksei"


def get_last_blockchain_value():
    """
    :return: the last value of the current blockchain.
    """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]
def add_transaction(tx_recipient, tx_sender=owner, tx_amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain.
    :argument tx_sender: The sender of the coins.
    :argument tx_recipient: The recipient of the coins.
    :argument tx_amount: The amount of the coins sent with the transaction (default = 1.0)
    """
    transaction = {
        "sender": tx_sender,
        "recipient": tx_recipient,
        "amount": tx_amount
    }
    open_transactions.append(transaction)


def mine_block():
    pass


def get_transaction_value():
    """
    :return: the input of the user (a new transaction amount) as a float.
    """
    # Get the user input, transform it from a string to a float and store it in user_input
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your transaction amount please: "))
    return tx_recipient, tx_amount


def get_user_choice():
    """ Prompts the user for its choice and return it. """
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    """ Output all blocks of the blockchain. """
    # Output the blockchain list to the console
    for block in blockchain:
        print("Outputting Block")
        print(block)
    else:
        print("-" * 20)


def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise. """
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            # If we're checking the first block, we should skip the iteration (since there's no previous block)
            continue
        # Check the previous block (the entire one) vs the first element of the current block
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


waiting_for_input = True

# A while loop for the user input interface
# It's a loop that exits once waiting_for_input becomes False or when break is called
while waiting_for_input:
    print("Please choose:")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if "1" == user_choice:
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add the transaction amount to the blockchain
        add_transaction(recipient, tx_amount=amount)
    elif "2" == user_choice:
        print_blockchain_elements()
    elif "h" == user_choice:
        # Make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif "q" == user_choice:
        # This will lead to the loop to exist because it's running condition becomes False
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from the list!")
    if not verify_chain():
        print("Invalid blockchain!")
        print_blockchain_elements()
        # Break out of the loo
        break
else:
    print("User left!")

print("Done!")
