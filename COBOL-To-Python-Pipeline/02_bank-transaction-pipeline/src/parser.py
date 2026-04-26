def main():
        
    with open("C:\\bank-transaction-pipeline\\input\\transactions.dat","r") as f, open("C:\\bank-transaction-pipeline\\output\\transactions_report.txt","w") as o:

       Write_Header(o);

       for line in f:
           Record = Format_IP(line);
           Record = Cal_New_Bal(Record);        
           Write_Report(o,Record);

       Write_Footer(o);


def Write_Header(o):

    o.write("=" * 100)
    o.write("\n")
    o.write(f"{'BANK TRANSACTION REPORT':^100}")
    o.write("\n")
    o.write(f"{'COBOL TO PYTHON PIPELINE PROJECT':^100}")
    o.write("\n")
    o.write("=" * 100)
    o.write("\n")
    o.write(f"{'ACC ID':<12}")
    o.write(f"{'ACCOUNT NAME':<20}")
    o.write(f"{'TYPE':<10}")
    o.write(f"{'AMOUNT':<10}")
    o.write(f"{'BALANCE':<15}")
    o.write(f"{'NEW BALANCE':<15}")
    o.write("\n")

def Format_IP(line):

    Record ={}

    ACC_ID = line[0:8]
    ACCOUNT_NAME = line[8:28]
    TRAN_TYPE = line[28:30]
    TRAN_AMOUNT = line[30:36]
    BALANCE = line[36:45]

    Record['ACC_ID'] =  line[0:8]  
    Record['ACCOUNT_NAME'] =  line[8:28]
    Record['TRAN_TYPE'] =  line[28:30]
    Record['TRAN_AMOUNT'] =  int(line[30:36])/100
    Record['BALANCE'] =  int(line[36:45])/100
    Record['NEW_BALANCE'] =  0.0

    print(Record)

    print("ACC_ID",ACC_ID)
    print("ACCOUNT_NAME",ACCOUNT_NAME)
    print("TRAN_TYPE",TRAN_TYPE)
    print("TRAN_AMOUNT",TRAN_AMOUNT)
    print("BALANCE",BALANCE)

    return(Record);

def Cal_New_Bal(Record):
    if Record['TRAN_TYPE'] == 'CR':
        New_Bal = int(Record['BALANCE']) + int(Record['TRAN_AMOUNT'])
        print("New_Bal",New_Bal)
    else:
        New_Bal = int(Record['BALANCE']) - int(Record['TRAN_AMOUNT'])
        print("New_Bal",New_Bal)

    Record['NEW_BALANCE'] = New_Bal
    print(Record)

    return(Record);

def Write_Report(o,Record):
    o.write(f"{Record['ACC_ID']:<12}"
            f"{Record['ACCOUNT_NAME']:<20}"
            f"{Record['TRAN_TYPE']:<10}"
            f"{Record['TRAN_AMOUNT']:<10.2f}"
            f"{Record['BALANCE']:<15.2f}"
            f"{Record['NEW_BALANCE']:<15.2f}"
            f"\n")
    

def Write_Footer(o):
    o.write("=" * 100)
    o.write("\n")
    o.write(f"{'END OF REPORT':^100}")
    o.write("\n")
    o.write("=" * 100)
     
main()