from selenium import webdriver
from time import sleep

class fbot:
    def __init__(self,username,pw):
     
        self.driver = webdriver.Chrome()
        self.username = username
        self.pw = pw
        self.driver.get("https://www.instagram.com")
        sleep(4)
#for username
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
#for password
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")\
            .send_keys(pw)
#for login
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")\
            .click()
        sleep(2)
#for not saving info
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
            .click()
        sleep(2)
#for not now
        
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
            .click()
        sleep(2)
# New Function
    def get_unfollow(self): 
        
#for profile icon
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")\
            .click()
        sleep(2)
#for profile
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")\
            .click()
        sleep(2)
#for followers
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")\
            .click()
        followers = self._getnames()

#for following
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")\
            .click()
        following = self._getnames()
# Checking the accounts that are not following you back 
        non_followers = [user for user in following if user not in followers] 
# This will output the names of accounts        
        print(non_followers)
# Just to make it more easy to read
        f = open("Non-Followers.txt",'w')
        non_followers = map(lambda x:x+'\n', non_followers)
# Saving the data in File 
        f.writelines(non_followers)
        f.close() 
        print("Close the program and check for a file named Non-Followers.txt")
    def _getnames(self):
        sleep(2)
#scrolling box
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last,h = 0, 1
#condition for scrollbox ends
        while last!= h:
            last = h
            sleep(1)
            h = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
#catching the names
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name !='']
    
#close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        sleep(2)
        return names

def credentials():
    user = input("Enter your Username(without @): ")
    pas = input("Enter your Password:\t\t ")
    return user, pas


# Main Function
print("\n\n\t\t\t\t\tWELCOME TO INSTAGRAM BOT")
print("\n\n\t\t\t\t!! Fill in your correct details\n\n")
user, pas = credentials()
try:
    new = fbot(user, pas)
    new.get_unfollow()
#Checking if there is an error !!!
except:
    print("\t\t\t\t\tError !!!!")
