import math

user_choice = input('''What do you want to calculate?
type "n" - for count of months,
type "a" - for annuity monthly payments,
type "p" - for credit principal:''')
if user_choice == "n":
    principal = int(input("Enter credit principal:"))
    monthly_amount = int(input("Enter monthly payment:"))
    credit_interest = float(input("Enter credit interest:"))
    monthly_interest = credit_interest / 1200
    total_no_of_months = math.ceil(math.log(monthly_amount / (monthly_amount - monthly_interest * principal), 1 + monthly_interest))
    no_of_years = total_no_of_months // 12
    no_of_months = total_no_of_months % 12
    if no_of_years == 0:
        print("You need {} months to repay this credit!".format(no_of_months))
    elif no_of_months == 0:
        if no_of_years == 1:
            print("You need {} year to repay the credit!".format(no_of_years))
        else:
            print("You need {} years to repay the credit!".format(no_of_years))
    else:
        print("You need {} years and {} months to repay this credit!".format(int(no_of_years), math.ceil(no_of_months)))
elif user_choice == "a":
    principal = int(input("Enter credit principal:"))
    no_of_months = int(input("Enter count of periods:"))
    credit_interest = float(input("Enter credit interest:"))
    monthly_interest = credit_interest / 1200
    annuity_payment = principal * ((monthly_interest * math.pow(1 + monthly_interest, no_of_months)) /
                                   (math.pow(1 + monthly_interest, no_of_months) - 1))
    print("Your annuity payment = {}!".format(math.ceil(annuity_payment)))
elif user_choice == "p":
    monthly_amount = float(input("Enter monthly payment:"))
    no_of_months = int(input("Enter count of periods:"))
    credit_interest = float(input("Enter credit interest:"))
    monthly_interest = credit_interest / 1200
    credit_principal = monthly_amount / ((monthly_interest * math.pow(1 + monthly_interest, no_of_months)) /
                                   (math.pow(1 + monthly_interest, no_of_months) - 1))
    print("Your credit principal = {}!".format(round(credit_principal)))


# credit_principal = int(input("Enter the credit principal:"))
# user_option = input('''What do you want to calculate?
# type "m" - for count of months,
# type "p" - for monthly payment:''')
# if user_option == "m":
#     monthly_amount = int(input("Enter monthly payment:"))
#     if credit_principal % monthly_amount == 0 and credit_principal // monthly_amount == 1:
#         print("It takes {} month to repay the credit".format(credit_principal // monthly_amount))
#     elif credit_principal % monthly_amount == 0:
#         print("It takes {} months to repay the credit".format(credit_principal // monthly_amount))
#     else:
#         print("It takes {} months to repay the credit".format(credit_principal // monthly_amount + 1))
# elif user_option == "p":
#     time_period = int(input("Enter count of months:"))
#     if credit_principal % time_period == 0:
#         print("Your monthly payment = {}".format(credit_principal // time_period))
#     else:
#         monthly_payment = ceil(credit_principal / time_period)
#         last_payment = credit_principal - (time_period - 1) * monthly_payment
#         print("Your monthly payment = {} with last month payment = {}.".format(monthly_payment, last_payment))