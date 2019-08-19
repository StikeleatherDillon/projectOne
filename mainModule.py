class Customer:
    def __init__(self, email):

        self.email = email
        self.age = 0
        self.last_name = ""
        self.first_name = ""
        self.password = ""
        self.card_number = ""
        self.security_code = ""

    def input_age(self):

        while True:
            try:
                age = int(input("Enter age :"))
                if age < 0:
                    raise ValueError
                self.age = age
                break
            except ValueError:
                print("Age must be an non negative integer ")

    def input_password(self):
        while True:
            print("\nYour password must be 8-12 characters long containing at least one upper-case letter, "
                  "one lower-case letter, and one number.")
            password = input("Enter password : ")
            if not any(c.isupper() for c in password):
                print("does not contain upper-case")
            elif not any(c.islower() for c in password):
                print("does not contain lower-case")
            elif not any(c.isdigit() for c in password):
                print("does not contain number")
            elif len(password) < 8 or len(password) > 12:
                print("Password should be 8-12 characters long")
            else:
                print("\nValid password")
                self.password = password
                break

    def input_card_number(self):

        while True:
            card_number = input("Enter 16-digit credit card number : ")
            if all(c.isdigit() for c in card_number) and len(card_number) == 16:
                self.card_number = card_number
                break

            print("\nCard number must be 16 digits.")

    def input_security_code(self):
        while True:
            security_code = input("Enter 3-digit security code : ")
            if all(c.isdigit() for c in security_code) and len(security_code) == 3:
                self.security_code = security_code
                break

            print("\nPIN must be three digits.")

    def input_info(self):
        self.first_name = input("Enter first name : ")
        self.last_name = input("Enter last name : ")
        self.input_age()
        self.input_password()
        self.input_card_number()
        self.input_security_code()

    def verify_info(self):
        while True:
            print("\n------------------------------------------")
            print("\n 1. First name : {}".format(self.first_name))
            print("\n 2. Last name : {}".format(self.last_name))
            print("\n 3. Email address : {}".format(self.email))
            print("\n 4. Password : {}".format(self.password))
            print("\n 5. Age : {}".format(self.age))
            print("\n 6. Card number : {}".format(self.card_number))
            print("\n 7. Security code : {}".format(self.security_code))
            choice = int(input("\nTo correct any entry, enter the entry's number and press RETURN. If everything is "
                               "correct, press 0 :"))
            if choice == 1:
                self.first_name = input("Enter first name : ")
            elif choice == 2:
                self.last_name = input("Enter last name : ")
            elif choice == 3:
                self.email = input("Enter email address : ")
            elif choice == 4:
                self.input_password()
            elif choice == 5:
                self.input_age()
            elif choice == 6:
                self.input_card_number()
            elif choice == 7:
                self.input_security_code()
            elif choice == 0:
                print("Registration and verification completed for this customer.")
                break   # break from loop after successful verification
            else:
                print("Invalid choice. Please choose (1-7).")

    def output_info(self):
        return "{} {} {} {} {} {} {}\n".format(self.first_name,
                                               self.last_name,
                                               self.age,
                                               self.email,
                                               self.password,
                                               self.card_number,
                                               self.security_code)


if __name__ == '__main__':

    print("\n Customer 1")
    email = input("Enter email address : ")
    customer1 = Customer(email)
    customer1.input_info()
    customer1.verify_info()

    print("\n Customer 2")
    email = input("Enter email address : ")
    customer2 = Customer(email)
    customer2.input_info()
    customer2.verify_info()

    f = open("customers.txt", "w")
    f.write(customer1.output_info())
    f.write(customer2.output_info())
    f.close()
    print("\n Data of two customers written to the file 'customers.txt'")

