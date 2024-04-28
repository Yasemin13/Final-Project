class User:
    def __init__(self, user_id, first_name, last_name, email, dob, password):
        self.Id = user_id
        self.First_Name = first_name
        self.Last_Name = last_name
        self.Email = email
        self.DOB = dob
        self.Password = password

    def __str__(self):
        return f"User: {self.First_Name} - {self.Last_Name} - {self.Email} - {self.Password}"


class Account:
    def __init__(self, account_number, balance, user_id ):
        self.Account_Num = account_number
        self.Balance = balance
        self.Id = user_id


    def __str__(self):
        return f"Account: {self.Account_Num} - {self.Balance} - {self.Id}"