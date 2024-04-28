import random

from db import get_user_by_email, create_user_account, add_user, get_user_account, update_account_balance
from models import Account, User

"""
These are your helper functions. They are responsible for containing business logic but not directly interacting with the database.
"""


def create_new_user_helper(first_name, last_name, email, dob, password):
    """
    Creates a new user and persists it in the database
    :param user_name: full name of the new user
    :param user_email: email of the new user
    :param user_password: password of the new user
    :return:
    """
    # create a new User model
    new_user = User(None, first_name, last_name, email, dob, password)
 

    # persist new user in the database
    add_user(new_user)

    print(f"Created new user: {new_user}")





def create_new_account_helper(email):
    """
    Creates a new account for the given user and persists it in the database
    :param user_email: email of an existing user
    :param account_type: type of account to create
    :return:
    """
    # get user from the database by calling db.get_user_by_email
    user = get_user_by_email(email)

    # create randomized account and routing numbers
    new_account_number = str(random.randint(100000000, 999999999))

    # create a new Account model representing the user's new account
    new_account = Account(new_account_number, 0, user.Id )


    create_user_account(user, new_account)

    print(f"Created new account: {new_account}")



def get_account_balance_helper(user_email) -> Account:
    """
    Gets the account for the given user and account type
    :param user_email: user email
    :param account_type: type of account we want to get info for
    :return: User account if it exists
    """

    # get user from the database by calling db.get_user_by_email
    user = get_user_by_email(user_email)

    # get account from database for the given user and account type
    return get_user_account(user)




def get_account_helper(user_email) -> Account:
    """
    Gets the account for the given user and account type
    :param user_email: user email
    :param account_type: type of account we want to get info for
    :return: User account if it exists
    """

    # get user from the database by calling db.get_user_by_email
    user = get_user_by_email(user_email)

    # get account from database for the given user and account type
    return get_user_account(user)


def deposit_into_account_helper(user_email, deposit_amount):
    """
    Deposits the given amount into the given account
    :param user_email: user email
    :param account_type: type of account we want to deposit into
    :param deposit_amount: amount to deposit
    :return:
    """
    # get account from database for the given user and account type
    account = get_account_helper(user_email)

    # update account balance
    new_balance = float(account.Balance) + float(deposit_amount)

    # update account in database
    update_account_balance(account.Id, new_balance)

    print(f"Deposited ${deposit_amount} into account {account.Account_Num}")