import os

#ask for the commit message
commit_message = input("enter your message : ")

#Run git commands
os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push -u origin main")