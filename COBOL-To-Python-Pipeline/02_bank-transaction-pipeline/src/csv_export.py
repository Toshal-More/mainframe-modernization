import csv

def main():
    with open (r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\02_bank-transaction-pipeline\input\transactions.dat","r") as f,open (r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\02_bank-transaction-pipeline\output\Tran_Export.csv","w") as o:

        fields = ['ACC_ID','ACC_Name','TRAN_TYP','TRAN_Amount','BAL','New_Bal']
        writer = csv.DictWriter(o,fieldnames=fields)
        writer.writeheader()

        read_IP(f,writer)

def read_IP(f,writer):

    for line in f:
        record = { 'ACC_ID' : line[0:8],
                   'ACC_Name' : line[8:28],
                   'TRAN_TYP' : line[28:30],
                   'TRAN_Amount' : int(line[30:36])/100,
                   'BAL' : int(line[36:44]),

        }

        if record['TRAN_TYP'] == 'CR':
            record['New_Bal'] = record['BAL'] + record['TRAN_Amount']
        elif record['TRAN_TYP'] == 'DR':
            record['New_Bal'] = record['BAL'] - record['TRAN_Amount']


        write_CSV(writer,record)


def write_CSV(writer,record):
    writer.writerow(record)

main()