import json

print("welcome login singup page")
user=input("what you want sing up or login account")
if user=="sing":
    name=input("enter the name")
    last_name=input("enter your last name")
    email=input("enter the email id")
    password=input("enter your password")
    confim_passwprd=input("enter your password again.....")
    if "@" in email and "." or "1-9" in email:
        print("successfull")
        if "@" in password or "#" in password:
            if password==confim_passwprd:
                print("Account creat succesfully")
                a=open("log.txt","a")
                new_file=a.write("name :-")
                new_file=a.write(name)
                new_file=a.write("\n")

                new_file=a.write("last_name :-")
                new_file=a.write(last_name)
                new_file=a.write("\n")
            
                new_file=a.write("password")
                new_file=a.write(password)
                new_file=a.write("\n")

                new_file=a.write("email id :-")
                new_file=a.write(email)
                new_file=a.write("\n")
                print()
                a.close()
                print()
                js=json.dumps(new_file)
                print(js)
            else:
                print("your password is wrong")
        else:
            print("in password no special charators")
    else:
        print("incorrect email")
elif user=="login":
    name1=input("enter your name")
    file=open("log.txt","r")
    new_file1=file.read()
    if name1 in new_file1:
        password1=input("enter your password :")
        if password1 in new_file1:
            print("succeessfll")
            email1=input("enter your email id")
            if email1 in new_file1:
                print("login succesfull")
                print()
                j=json.dumps(new_file1)
                print(j)
                print(type(j))
            else:
                print("email is wrong")
        else:
            print("password is wrong")
    else:
        print("user name is wromg")