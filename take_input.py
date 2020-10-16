def take_input():
    while True:
        stock = input("( 1 ) STOCK OR ( 2 ) BUYOUT >>> ")
        check = ['1', '2']
        if stock in check:
            break
        else:
            print("Choose 1 or 2")
            continue

    while True:
        metal = input("METAL TYPE: (S)STEEL  (N)NICKEL (A)ALUMINUM (T)TITANIUM >>> ").upper()
        check = ['S', 'N', 'T', 'A']
        if metal in check:
            break
        else:
            print(" Invalid Entry. Try Again")
            continue
# stock = 1/2 meatl = S/N/T/A

    header = {
            "heat": input("HEAT NUMBER >>> "),
            "lot": input("LOT NUMBER >>> "),
            "mfg": input("MFG >>> "),
            "material": input("Material >>> "),
            "condition": input("Condition >>> ")
            }
    return stock, metal, header
