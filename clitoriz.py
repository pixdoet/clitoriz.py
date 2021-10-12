# clitoriz.py: main api file for the python clitoriz library
# To do:
# - Make it modular
# - Finish all the functions
# - Write documentation
# - Write an actual demo program that uses all the functions in a sensible way (reuse test.py?)

# © 2021 Ian Hiew. All rights reserved. Use of this software for commercial purposes is allowed provided that 
# you follow the guidelines in guidelines.txt

from json.decoder import JSONDecodeError
import requests

s = requests.Session()

class Clitoriz():
    def __init__(self):
        self.listLink = "https://clitoriz.cf/api/users/list.php"
        self.singleLink = "https://clitoriz.cf/api/users/getinfo.php?user="
    
    def debug():
        maxUsers = 1
        print(maxUsers)
    
    def all(self):
        try:
            self.dataAll = s.get(self.listLink).json()
        except JSONDecodeError:
            print("Failed connecting to the API, bad internet connection or API down?")
            return False
        else:
            # store everything into an array ig
            return True

    def user(self,username):
        #join link and username together :him:
        self.singleJoinedLink = self.singleLink + username
        #receive data from api link
        try:
            self.data = s.get(self.singleJoinedLink).json()
        except JSONDecodeError:
            print ("Failed connecting to the API, wrong username or bad internet connection maybe?")
            return False
        else:
            self.bio = str(self.data['Bio'])
            self.badge = str(self.data['Badge'])
            self.customStars = str(self.data['CustomStars'])
            self.customRank = str(self.data['CustomRank'])
            self.customBadge = str(self.data['CustomBadge'])
            self.status = str(self.data['Status'])
            self.picture = "https://clitoriz.cf/images/pfps/" + str(self.data['Picture'])
            return True
    
    def login(self,username,password):
        print (username)
        print (password)
        

clitoriz = Clitoriz()
