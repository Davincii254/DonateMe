from donations_pkg import homepage
from donations_pkg import user

database = {
    "admin" : "password123"
}
donations = []
authorized_user = ""

while True:
    homepage.show_homepage ()
    if authorized_user == "":
        print("You must e logged in to donate!")
    else:
        print(" Logged in as:", authorized_user )
    
    choice = input("Plesae choose an option: ")
    if choice == "1":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = user.login(database, username, password)
    elif choice == "2":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = user.register(database, username, password)
        if authorized_user != "":
            database[authorized_user] = password
    elif choice == "3":
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            donation = homepage.donate(authorized_user)
            donations.append(donation)
    elif choice == "4":
        homepage.show_donations(donations)
    elif choice == "5":
        print("\nLeaving DonateMe...")
        break