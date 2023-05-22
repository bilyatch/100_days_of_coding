#  "^"--> this sign gives the start sign in regex
#  "+"--> this sign joins the conditions
#  "\"-->"this sign is  used to check if a string contains the specified search pattern
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your email address:")
if re.search(email_condition,user_email):
    print("Right format")
else:
    print("Wrong format")
