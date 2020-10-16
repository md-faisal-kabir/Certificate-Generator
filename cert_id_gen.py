from excel_reader import read_excel
def cert_id_generator(prev_id):
    #read the last entry in database
    # increment the cert id
    prev_id = prev_id.split('-')

    if int(prev_id[2]) == 9999999999:
        prev_id[1] = str(int(prev_id[1]) + 1)
        prev_id[2] = '0'.zfill(10)
    else:
        prev_id[2] = str(int(prev_id[2])+1).zfill(10)
    cert_id = ('-').join(prev_id)
    return cert_id

def test_cert_id_gen(test_case):
    print (cert_id_generator(test_case[0])==test_case[1])

if __name__ == "__main__":
    # stock = input("Stock 1/2")
    # metal = input("Meta:S/T")
    # cert_template, db_sheet, certbook, db, prev_id = read_excel(stock, metal)
    # cert_id = cert_id_generator(prev_id)
    # print(cert_id)

    test_case = [
        ["AMC-0-0000000000", "AMC-0-0000000001"],
        ["AMC-0-9999999999", "AMC-1-0000000000"],
        ["AMC-0-0000000550", "AMC-0-0000000551"],
        ["AMC-1-9999999999", "AMC-2-0000000000"]
        ]

    for case in test_case:
        test_cert_id_gen(case)