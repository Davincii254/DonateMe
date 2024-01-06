def show_homepage():
    print("\n       === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.   Login       | 2.   Register        |")
    print("------------------------------------------")
    print("| 3.   Donate      | 4.   Show Donations  |")
    print("------------------------------------------")
    print("|              5.   Exit                  |")
    print("------------------------------------------")

    def donate (username):
        donation_atm = float(input("Please enter amount to donate"))
        donation = username + "donated $" + str(donation_atm)
        print("Thank you for your Donation!", username)
        return donation
    
    def show_donations (donations):
        print("\n--- All Donations ---")
        if len(donations) == 0:
            print("Currently, there are no donations.")
        else:
            return donations