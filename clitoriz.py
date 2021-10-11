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
    
    def all():
        print("Coming Soon...")

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