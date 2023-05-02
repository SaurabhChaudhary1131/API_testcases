import requests


class Accounts:
    positive = {"name": "jack", "acc_no": 123456, "balance": 100000}
    duplicate = {"name": "abc", "acc_no": 1234567, "balance": 500000}
    minimum = {"name": "rock", "acc_no": 12345, "balance": 1000}

    def check_the_user(self, user_name):
        request = None
        if user_name == self.positive["name"]:
            request = requests.get("https://reqres.in/api/users/2")
        else:
            request = "User does not exist"
        return request

    def duplicate_user(self, user_name, account_no):
        req = None
        if account_no == self.duplicate["acc_no"]:
            print(user_name)
            print(self.duplicate["acc_no"])
            print("account already present can not make duplicate account")
            req = requests.post("https://reqres.in/api/register")
            print(req)
        else:
            req = "Incorrect account number/Account does not exists"
        return req

    def deposit(self, acc_no, amount_deposit):
        req = None
        if acc_no == self.positive["acc_no"]:
            if amount_deposit >= 10000:
                req = "can not deposit this much amount in a single transaction"
            else:
                c = self.positive["balance"] + amount_deposit
                print("Updated balance is", c)
                req = requests.post("https://reqres.in/api/users")
        else:
            req = "wrong account number"
        return req

    def withdrawl(self, acc_no, amount_withdraw):
        if acc_no == self.positive["acc_no"]:
            if amount_withdraw >= (self.positive["balance"]) * .9:
                print("you cannot withdraw 90 percent amount from account in one time")
            else:
                print("updated balance is", self.positive["balance"] - amount_withdraw)
                req = requests.post("https://reqres.in/api/users")
                print(req)
                code = req.status_code
                assert code == 201, "something went wrong"
        else:
            print("wrong account number")

    def minimum_amount(self, account_no, amount_withdrawn):
        if account_no == self.minimum["acc_no"]:
            #print("enter the amount")
            #amount_withdrawn = int(input())
            c = self.minimum["balance"] - amount_withdrawn
            if c >= 100:
                print("updated balance is", c)
                req = requests.post("https://reqres.in/api/users")
                print(req)
                code = req.status_code
                assert code == 201, "something went wrong"
            else:
                print("Account should have minimum balance of $100")
        else:
            print("account does not match")
