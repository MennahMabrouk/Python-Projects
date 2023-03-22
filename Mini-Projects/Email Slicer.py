#collect email from user
#split by @,the frist part user name , the second part is gonna be domain
#split domain use dot
def main():
    print("Slice your E-mail!")
    print("")
    while True:
        email_input= input("Enter your Email Adress: ")
        (username, domain) = email_input.split("@")
        (domain,extension)= domain.split(".")

        print("Your User Name: ", username)
        print("Your Domain: ", domain)
        print("Your Extension: ", extension )
main()