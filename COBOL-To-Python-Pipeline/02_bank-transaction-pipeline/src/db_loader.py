import sqlite3

def main():
    conn = sqlite3.connect("C:\\Mainframe-Modernization\\COBOL-To-Python-Pipeline\\02_bank-transaction-pipeline\\output\\transaction.db")

    create_Tran_table(conn)
    load_data_TRAN01(conn)
    Read_data(conn)

def create_Tran_table(conn):

    cursor = conn.cursor()

    cursor.execute("""
                    create table if not exists TRAN01 (
                    ACC_ID  text,
                    ACC_NAME text,
                    TYPE text,
                    AMOUNT real,
                    BALANCE real,
                    NEW_BALANCE real )
                   """)
    
    conn.commit()



def load_data_TRAN01(conn):
    cursor = conn.cursor()

    with open(r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\02_bank-transaction-pipeline\input\transactions.dat","r") as f:
        
        for line in f:
            ACC_ID = line[0:8]
            ACC_NAME = line[8:28]
            TYPE = line[28:30]
            AMOUNT = int(line[30:36])/100
            BALANCE = int(line[36:45])/100

            if TYPE == 'CR':
               NEW_BALANCE = BALANCE + AMOUNT
            elif TYPE == 'DR':
               NEW_BALANCE = BALANCE - AMOUNT


            cursor.execute("""
                   insert into TRAN01 (
                   ACC_ID,
                   ACC_NAME,
                   TYPE,
                   AMOUNT,
                   BALANCE,
                   NEW_BALANCE
                   )
                   values (?,?,?,?,?,?)
                   """,(ACC_ID,
                   ACC_NAME,
                   TYPE,
                   AMOUNT,
                   BALANCE,
                   NEW_BALANCE))

        conn.commit()
    

def Read_data(conn):
    cursor = conn.cursor()

    cursor.execute("""
                   select * from 
                   TRAN01 
                   """)
    
    Data = cursor.fetchall()
    print("Data",Data)

    for Row in Data:
        print(Row[0])
        print(Row[1])
        print(Row[2])
        print(Row[3])
        print(Row[4])
        print(Row[5])
        
main()