import csv

def main():

    Read_data()
           
def Read_data():
    with open(r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\01_employee-salary-pipeline\input\employees.dat","r") as f,open(r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\01_employee-salary-pipeline\output\employees.csv","w") as o:
        
        Fields = ['EMP_ID','EMP_NAME','WORK_HRS','WORK_RATE','SALARY']
        writer = csv.DictWriter(o,fieldnames=Fields)
        writer.writeheader()

        for line in f:
            Record = format_IP(line)
            write_CSV(writer,Record)

def format_IP(line):
        
        Record = {'EMP_ID' : line[0:6],
                  'EMP_NAME' : line[6:28],
                  'WORK_HRS' : int(line[28:32]),
                  'WORK_RATE' : int(line[32:37])/100,
                  'SALARY' : (int(line[28:32]) * int(line[32:37])/100)
                 }
        
        return Record

def write_CSV(writer,Record):
    writer.writerow(Record)

main()