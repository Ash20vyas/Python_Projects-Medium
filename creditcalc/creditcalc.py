import sys
args = sys.argv

if len(args)!= 5:
    print("Incorrect parameters.")
    quit()
option = args[1][7:]
principal = int(args[2][12:])
periods = int(args[3][10:])
interest = float(args[4][11:])
if min(principal, periods, int(interest)) < 0:
    print("Incorrect parameters.")
    quit()
if option == "diff":
    print(option)
elif option == "annuity":
    print(option)
else:
    print("Incorrect parameters.")

# python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10
# python credit_calc.py --type=diff --principal=500000 --periods=8 --interest=7.8
# python credit_calc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# python credit_calc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8



# import math
#
# option = input('''What do you want to calculate?
# type "n" - for count of months,
# type "a" - for annuity monthly payment,
# type "p" - for credit principal:
# ''')
# if option == "n":
#     credit_principal = int(input("Enter credit principal:\n"))
#     annuity_payment = int(input("Enter monthly payment:\n"))
#     credit_interest = int(input("Enter credit interest:\n"))
#     nominal_interest = credit_interest / 1200
#     if nominal_interest <= 0:
#         months = math.ceil(math.log(annuity_payment / (annuity_payment - nominal_interest * credit_principal)))
#     else:
#         months = math.ceil(math.log(annuity_payment / (annuity_payment - nominal_interest * credit_principal), 1 + nominal_interest))
#     if months < 12:
#         print("You need {} month{} to repay this credit!".format(months, 's' if months > 1 else ''))
#     elif months % 12 == 0:
#         print("You need {} year{} to repay this credit!".format(months // 12, 's' if months // 12 > 1 else ''))
#     else:
#         print("You need {} year{} and {} month{} to repay this credit!"
#               .format(months // 12, 's' if months // 12 > 1 else '',
#                       months % 12, 's' if months % 12 > 1 else ''))
# elif option == "a":
#     credit_principal = int(input("Enter credit principal:\n"))
#     period_count = int(input("Enter count of periods\n"))
#     credit_interest = float(input("Enter credit interest:\n"))
#     nominal_interest = credit_interest / 1200
#     annuity_payment = round(credit_principal * nominal_interest * (1 + nominal_interest) ** period_count
#                             / ((1 + nominal_interest) ** period_count - 1))
#     print(f"Your annuity payment = {annuity_payment}!")
# elif option == "p":
#     annuity_payment = float(input("Enter monthly payment:\n"))
#     period_count = int(input("Enter count of periods\n"))
#     credit_interest = float(input("Enter credit interest:\n"))
#     nominal_interest = credit_interest / 1200
#     # annuity_payment = 8721.8
#     credit_principal = round(annuity_payment / ((nominal_interest * (1 + nominal_interest) ** period_count)
#                                                 / ((1 + nominal_interest) ** period_count - 1)))
#     print(f"Your credit principal = {credit_principal}!")
