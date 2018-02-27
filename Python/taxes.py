# CODED BY FelipeCRamos
# FOR FREETIME


def showPrice(price_real, price_dollar):
    print("Splitting things:")
    for i in range(1,13):
        print("\t%ix of R$ %.2f" %(i, price_real/i))
    print("\nTotal: R$ %.2f | $ %.2f" %(price_real, price_dollar))
    print("")
    main()


def real_to_dollar():
    global dollar_price
    a_real = float(input("Please, enter the amount of REAIS:\nR$ "))
    showPrice(a_real, (a_real/dollar_price)/1.60)


def dollar_to_real():
    global dollar_price
    a_dollar = float(input("Please, enter the amount of DOLLARS:\n $ "))
    showPrice((a_dollar*1.60)*dollar_price, a_dollar)


def main():
    print("\nWelcome, please select one of the options above:\n"
    "(1) ~ To convert from REAL to DOLLAR\n"
    "(2) ~ To convert from DOLLAR to REAL")
    choice = int(input("Option: "))
    if(choice == 1):
        real_to_dollar()
    else:
        dollar_to_real()

dollar_price = float(input("First, tell us the price for US$ 1 in REAL: "))
main()
