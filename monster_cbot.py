from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, colorama, urllib.request
from termcolor import *

colorama.init()

cprint('''
 _______  _______  _        _______ _________ ______   _______ 
(       )(  __   )( (    /|(  ____ \\__   __// ___  \ (  ____ )
| () () || (  )  ||  \  ( || (    \/   ) (   \/   \  \| (    )|
| || || || | /   ||   \ | || (_____    | |      ___) /| (____)|
| |(_)| || (/ /) || (\ \) |(_____  )   | |     (___ ( |     __)
| |   | ||   / | || | \   |      ) |   | |         ) \| (\ (   
| )   ( ||  (__) || )  \  |/\____) |   | |   /\___/  /| ) \ \__
|/     \|(_______)|/    )_)\_______)   )_(   \______/ |/   \__/
                                                               
''' , 'red')
cprint('''
                           ______    ____    ____   ______
                          / ____/   / __ )  / __ \ /_  __/
                         / /       / __  | / / / /  / /   
                        / /___    / /_/ / / /_/ /  / /    
                        \____/   /_____/  \____/  /_/     
                                                          
''', 'cyan')

cprint("Coded by:M0NST3R , \nZERO NO ONE\n\n\n","yellow")
cprint("Facebook of Creator: https://fb.com/lildead.lilalive.3\n","cyan")


def clicker(link,proxy):

    coptions = webdriver.ChromeOptions()
    coptions.add_argument('--proxy-server=' + proxy)

    driver = webdriver.Chrome(options=coptions)
    try:
        driver.get(link)
        time.sleep(3)

        element = driver.find_element_by_id("skip_bu2tton")
        element.click()

        cprint("\nGetting a visit\n\n","blue")

        time.sleep(2)

        driver.quit()
    except:
        cprint("broken proxy","red")
        driver.quit()
        pass
           
def checker(proxy):
    proxy_support = urllib.request.ProxyHandler({'https' : proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    print("\nTrying => "+proxy)
    try:
        urllib.request.urlopen("https://adf.ly/")
        ccprint(proxy.replace("\n","") + " Is working\n",'green')
        with open("checked_proxies.txt","a+") as appe:
            appe.write(proxy.replace("\n","") + "\n")
        
    except:
        cprint(proxy.replace("\n","") + " Is not working\n",'red')
        pass
    
    
try:
    proxies = open("proxies_here.txt","r+").readlines()
except:
    cprint("No Proxies \nExiting","red")
    exit()
if proxies == "":
    cprint("file is empty Please enter some proxies \nYou can find Proxies on http://www.proxyserverlist24.top/ \n Exiting","red")
checkask = input("Do you want to check proxies? (Y,n)\n-: ")
link = input("Enter Your ad.fly link (ex http://ad.fly/1121548)\n- : ")
if checkask == "Y" or checkask == "y":
    newtxt = open("checked_proxies.txt","w+")
    cprint("\n\nChecking Proxies..\n\n","green")
    for proxy in proxies:
        checker(proxy)
    cprint("Finished checking...\nGetting clicks now!!\n\n\n","green")
    proxies = open("checked_proxies.txt","r+").readlines()
    
for proxy in proxies:
    cprint("Trying from: " + proxy ,"green")
    clicker(link=link, proxy=proxy)


cprint("JOB FINISHED!!! :) \n\nC U later ","cyan")
    
    
    

