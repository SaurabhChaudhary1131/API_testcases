import json
import requests
import logging

class UserAccount:
    list_of_users = {}

    def dataenter(self):
        user = {"name": "Saurabh Beta", "email": "saurabh_prafful_ka_beta@gmail.com", "salary": "2", "ids": "201"}
        # not needed just added to showcase that I can work on JSON as well
        stringify = json.dumps(user)
        open("data.json", "w").write(stringify)
        val = {user["ids"]: user}
        self.list_of_users.update(val)
        print(self.list_of_users)
        return user

    def new_user(self, name, email, salary, ids):
        mydata = open("data.json", "r").read()
        endpoint = requests.post("https://reqres.in/api/users", params="page=2", data=json.loads(mydata))
        print(endpoint, endpoint.json())
        # print(endpoint.url)
        return endpoint

    def delete_user(self, user_ids):
        delete = requests.delete("https://reqres.in/api/users/" + user_ids)
        self.list_of_users.pop(user_ids)
        logging.info(self.list_of_users)
        return delete

    def multi_create_caller(self):
        make_user = 'Y'
        while make_user == 'Y' or make_user == 'y':
            user_created = self.dataenter()
            self.new_user(user_created["name"], user_created["email"], user_created["salary"], user_created["ids"])

    def multi_delete_caller(self, user_ids):
        delete_user = 'Y'
        while delete_user == 'Y' or delete_user == 'y':
            self.delete_user(user_ids)
            delete_user = input('Do you want to delete another user?\nPress Y or y for Yes\nPress any key for No\n')
