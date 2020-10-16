from take_input import take_input
from excel_reader import read_excel
from cert_id_gen import cert_id_generator
from cert_generator import cert_generator
from db_write import db_write

def main():
    stock, metal, header = take_input()
    cert_template, db_sheet, certbook, db, prev_id = read_excel(stock, metal)
    cert_id = cert_id_generator(prev_id)
    certbook = cert_generator(certbook, cert_template, db_sheet, db, cert_id, header)
    db_write(db_sheet, db, cert_id, header)

if __name__ == "__main__":
    main()