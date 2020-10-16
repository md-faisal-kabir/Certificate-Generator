import os
from datetime import datetime

def cert_generator(certbook, cert_template, db_sheet, db, cert_id, header):
    cell = [ ]
    if cert_template.title == "Buyout Cert":
        cell = ['N6', 'M2', 'P2', 'M3', 'M4', 'N5' ]
    else:
        cell = ['O6', 'N2', 'Q2', 'N3', 'N4', 'O5' ]



    cert_template[cell[0]] = cert_id
    cert_template[cell[1]] = header['heat']
    cert_template[cell[2]] = header['lot']
    cert_template[cell[3]] = header['mfg']
    cert_template[cell[4]] = header['material']
    cert_template[cell[5]] = header['condition']

    try:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        timestamp = datetime.now()
        file = str(timestamp.year) + '-' + str(timestamp.month) + '-' + str(timestamp.day)
        folder = desktop + "\\AMC-CERTS\\"+ file
        if not os.path.exists(folder):
            os.makedirs(folder)
        certbook.save(f"{folder}\\" + cert_id + " - Product Certification.xlsx ")
        certbook.close()
        os.startfile(f"{folder}\\" + cert_id + " - Product Certification.xlsx ")
        return certbook
    except:
        print("*** DID NOT WORK!!!! CLOSE THE OPENED ((PRODUCTION CERTIFICATION.XLSX)) SHEET FIRST ***")

    
    

