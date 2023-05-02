import requests
from User_Account.user_account_blueprint import *
from Accounts.account_maintain import *

class Tests:
    name = "Saurabh"
    email = "saurabhchaudahry@gmail.com"
    salary = 10000
    ids = 201

    positive = {"name": "jack", "acc_no": 123456, "balance": 100000}
    duplicate = {"name": "abc", "acc_no": 1234567, "balance": 500000}
    minimum = {"name": "rock", "acc_no": 12345, "balance": 1000}

    def test_account_creation(self):
        endpoint = UserAccount.new_user(self.name, self.email, self.salary, self.ids)
        assert endpoint.status_code == 201, "User was not created"
        assert endpoint.json()["ids"] == self.ids, "ids mismatched"
        assert endpoint.json()["name"] == self.name, "Name mismatched"
        assert endpoint.json()["email"] == self.email, "Job mismatched"
        assert endpoint.json()["salary"] == self.salary, "salary mismatched"

    def test_account_deletion(self):
        delete = UserAccount.delete_user(self.ids)
        assert delete.status_code == 204, "User Not Deleted"

    def test_check_the_user(self):
        request = Accounts.check_the_user(self.positive["name"])
        code = request.status_code
        assert code == 200, "user does not exist"

    def test_duplicate_user(self):
        req = Accounts.duplicate_user(self.positive["name"], self.positive["acc_no"])
        code = req.status_code
        assert code == 400, "something wrong happens"

    def test_deposit(self):
        req = Accounts.deposit(self.positive["acc_no"], 10000)
        req2 = Accounts.deposit(self.positive["acc_no"], 100)
        assert req == "can not deposit this much amount in a single transaction", "Wrong results"
        code = req2.status_code
        assert code == 201, "something went wrong"
        req3 = Accounts.deposit(10001, 100)
        assert req3 == "wrong account number", "Wrong result returned"

    def test_withdraw(self):
        req = Accounts.withdrawl(self.positive["acc_no"],91000)
        assert req == "you cannot withdraw 90 percent amount from account in one time", "wrong input"
        req2 = Accounts.withdrawl(self.positive["acc_no"],90)
        assert req2.status_code == 201, "something wrong"
        req3 = Accounts.withdrawl(10001, 100)
        assert req3 == "wrong account number", "Wrong result returned"

    def test_minimum_ammount(self):
        req = Accounts.minimum_amount(self.minimum["acc_no"],901)
        assert req == "Account should have minimum balance of $100", "wrong input"
        req2 = Accounts.minimum_amount(self.minimum["acc_no"],90)
        assert req2 == req2.status_code == 201 , "something wrong"
        req3 = Accounts.minimum_amount(2143125,890)
        assert req3 == "account does not match" , "something wrong"


obj = Tests()
obj.test_account_creation()