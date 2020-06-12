import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
args = parser.parse_args()


def annuity_calculator(principal=0, no_of_months=0, payment=0, credit_interest=0):
    if payment == 0:
        monthly_interest = credit_interest / 1200
        annuity_payment = principal * ((monthly_interest * math.pow(1 + monthly_interest, no_of_months)) /
                                       (math.pow(1 + monthly_interest, no_of_months) - 1))
        print("Your annuity payment = {}!".format(math.ceil(annuity_payment)))
        print("Overpayment = {}".format(math.ceil(annuity_payment) * no_of_months - principal))
    elif principal == 0:
        monthly_interest = credit_interest / 1200
        credit_principal = payment / ((monthly_interest * math.pow(1 + monthly_interest, no_of_months)) /
                                             (math.pow(1 + monthly_interest, no_of_months) - 1))
        print("Your credit principal = {}!".format(math.floor(credit_principal)))
        print("Overpayment = {}".format(payment * no_of_months - math.floor(credit_principal)))
    else:
        monthly_interest = credit_interest / 1200
        total_no_of_months = math.ceil(
            math.log(payment / (payment - monthly_interest * principal), 1 + monthly_interest))
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
            print("You need {} years and {} months to repay this credit!".format(int(no_of_years),
                                                                                 math.ceil(no_of_months)))
        print("Overpayment = {}".format(payment * total_no_of_months - math.floor(principal)))


if args.type == "diff" and len(sys.argv) >= 4:
    if args.payment or not args.principal or not args.periods or not args.interest:
        print("Incorrect parameters")
    elif args.principal > 0 and args.periods > 0 and args.interest > 0:
        principal = args.principal
        periods = args.periods
        interest = args.interest / 1200
        total_payment = 0
        for i in range(1, periods + 1):
            monthly_payment = math.ceil((principal / periods) + interest * (principal - (principal * (i - 1)) / periods))
            print("Month {}: paid out {}".format(i, monthly_payment))
            total_payment += monthly_payment
        print("\nOverpayment = {}".format(total_payment - principal))
    else:
        print("Incorrect parameters")
elif args.type == "annuity" and len(sys.argv) >= 4:
    if not args.interest:
        print("Incorrect parameters")
    else:
        if not args.payment:
            annuity_calculator(principal=args.principal, no_of_months=args.periods, credit_interest=args.interest)
        elif not args.principal:
            annuity_calculator(payment=args.payment, no_of_months=args.periods, credit_interest=args.interest)
        else:
            annuity_calculator(payment=args.payment, principal=args.principal, credit_interest=args.interest)
else:
    print("Incorrect parameters")