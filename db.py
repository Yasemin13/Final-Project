import mysql.connector as mysql

from models import User, Account

# setup connection to database
db = mysql.connect(user='root', database='bank', password='root')

"""
These are your database access functions. They are responsible for direct interactions and queries to the database.
"""


def add_user(user: User):
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "INSERT INTO user ( First_Name, Last_Name, Email, DOB, Password) VALUES ( %s,%s,%s,%s, %s)"
    query_parameters = [ user.First_Name, user.Last_Name, user.Email, user.DOB, user.Password]
    cursor.execute(query, query_parameters)

    # commit changes
    db.commit()

    # close cursor
    cursor.close()


def get_user_by_email(email: str) -> User:
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "SELECT * FROM user WHERE email = %s"
    cursor.execute(query, [email])

    # get results
    result = cursor.fetchone()

    # close cursor
    cursor.close()

    # return result
    return User( result[5], result[0], result[1], result[2], result[3], result[4])


def create_user_account(user: User, new_account: Account):
    # insert the new account into our database
    cursor = db.cursor()

    # execute query
    query = "INSERT INTO bank_accounts (Account_Num, Id, Balance) VALUES (%s, %s, %s)"
    query_parameters = [new_account.Account_Num, user.Id, new_account.Balance]
    cursor.execute(query, query_parameters)

    # commit changes
    db.commit()

    # close cursor
    cursor.close()


def get_user_account(user: User) -> Account:
    # create cursor
    cursor = db.cursor(buffered=True)

    # execute query
    query = "SELECT * FROM bank_accounts WHERE Id = %s"
    query_parameters = [user.Id]
    cursor.execute(query, query_parameters)

    # get results
    result = cursor.fetchone()

    # close cursor
    cursor.close()

    # return result
    return Account(result[0], result[2], result[1])


def update_account_balance(account_id, new_balance):
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "UPDATE bank_accounts SET Balance = %s WHERE Id = %s"
    query_parameters = [new_balance, account_id]
    cursor.execute(query, query_parameters)

    # commit changes
    db.commit()

    # close cursor
    cursor.close()