import getpass
import time
import os
print("Booting up proxy...")
time.sleep(10)
select = input("select what to do: ")
if select == "stop":
    print("Stopping")
elif select == "login":
    pw = getpass.getpass("Enter admin password: ")

while pw !="test":
    pw = getpass.getpass("WRONG. Enter admin password: ")



print("Succesfully logged in as a admin")


