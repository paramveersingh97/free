import os 
import getpass
os.system("tput setaf 2")
print("\t\t\tHey, Welcome to the TUI. It makes life simple.")
os.system("tput setaf 3")
print("\t\t\t----------------------------------------------")
os.system("tput setaf 7")

print("Do you want to work on remote host or local host ? ")
input("Press key to continue...")
ip = "192.168.56.102"
actualpass = "yadav"
passwd = getpass.getpass(" Enter the password : ")
if passwd==actualpass:
    print("Welcome")
elif passwd!=actualpass:
    print("You are an unauthorise user")

output= os.system("ssh root@192.168.56.102")
print(output)
os.system("scp -r 192.168.56.102:/dir/a.txt /dir")
 





