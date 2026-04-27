import sqlite3

def main():

   Connection = Create_Connection();
   Create_EMP_Table(Connection); 
   Load_EMP_OP_Data(Connection);
   Read_EMP_Data(Connection);
   Connection.close();
   print("Done OK")

def Create_Connection():

    Connection = sqlite3.connect(r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\01_employee-salary-pipeline\output\Employee.db")
    print("Database connected succefully")

    return Connection;
    
def Create_EMP_Table(Connection):

    Cursor = Connection.cursor();

    Cursor.execute("""
                   CREATE TABLE IF NOT EXISTS EMPLOYEE_SALARY (
                   EMP_ID TEXT,
                   EMP_NAME TEXT,
                   WORK_HRS INTEGER,
                   WORK_RATE REAL,
                   SALARY REAL)
                   """)
    Connection.commit();
    print("Table created OK")


def Load_EMP_OP_Data(Connection):

    with open(r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\01_employee-salary-pipeline\input\employees.dat","r") as f:

        Cursor = Connection.cursor()
        for line in f:
            EMP_ID = line[0:6]
            EMP_NAME = line[6:28]
            WORK_HRS = int(line[28:32])
            WORK_RATE = int(line[32:37])/100
            SALARY = WORK_HRS * WORK_RATE

            print(EMP_ID)
            print(EMP_NAME)
            print(WORK_HRS)
            print(WORK_RATE)
            print(SALARY)

            Cursor.execute("""
                           INSERT INTO EMPLOYEE_SALARY
                           (EMP_ID, EMP_NAME, WORK_HRS, WORK_RATE, SALARY)
                           VALUES (?, ?, ?, ?, ?)
                           """, ((EMP_ID, EMP_NAME, WORK_HRS, WORK_RATE, SALARY)))

        Connection.commit()
        print("Data Loaded OK in DB table")

def Read_EMP_Data(Connection):
    Cursor = Connection.cursor()

    Cursor.execute("""
                   SELECT * FROM EMPLOYEE_SALARY 
                   """)
    
    rows = Cursor.fetchall()

    for row in rows:
        print("EMP-ID", row[0])
        print("EMP-NAME", row[1])
        print("WORK-HRS", row[2])
        print("WORK-RATE", row[3])
        print("SALARY", row[4])
        
main()