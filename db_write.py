def db_write(db_sheet, db, cert_id, header):
    index = str(len(db_sheet['A']) + 1)

    db_sheet["A" + index] = cert_id
    db_sheet["B" + index] = header['heat']
    db_sheet["C" + index] = header['lot']
    db_sheet["D" + index] = header['mfg']
    db_sheet["E" + index] = header['material']
    db_sheet["F" + index] = header['condition']

    db.save("cert-db.xlsx")
    
