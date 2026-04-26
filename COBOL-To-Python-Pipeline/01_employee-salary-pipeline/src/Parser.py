#OPENING THE .DAT FILE AND START READING THE FILE LINE BY LINE 
def main():
    with open("C:\cobol-to-python-pipeline\input\employees.dat", "r") as f, open("C:\cobol-to-python-pipeline\output\employees_salary.txt", "w") as o:
    
     for line in f:
       EMPID,EMP_NAME,WORK_HRS,WORK_RATE = format_IP(line); 
       SALARY = calculate_hrs_rate(WORK_HRS , WORK_RATE);
       write_report(o,EMPID,EMP_NAME,WORK_HRS,WORK_RATE,SALARY)


       print("EMP-ID",EMPID)
       print("EMP-NAME",EMP_NAME)
       print("WORK-HRS",WORK_HRS)
       print("WORK-RATE",WORK_RATE)
       print("SALARY",SALARY)
       
       
def format_IP(line):
    EMPID = line[0:6]
    EMP_NAME = line[6:28]
    WORK_HRS = line[28:32] 
    WORK_RATE = line[32:37]
#    print("EMP-ID",EMPID)
#    print("EMP-NAME",EMP_NAME)
#    print("WORK-HRS",WORK_HRS)
#    print("WORK-RATE",WORK_RATE)

    return EMPID,EMP_NAME,WORK_HRS, WORK_RATE

def calculate_hrs_rate(WORK_HRS, WORK_RATE):
    WORK_RATE_A = int(WORK_RATE)/100
    SALARY = (WORK_RATE_A * int(WORK_HRS))
#    print("SALARY",SALARY)

    return SALARY

def write_report(o,EMPID,EMP_NAME,WORK_HRS,WORK_RATE,SALARY):
        o.write(EMPID)
        o.write(EMP_NAME)
        o.write(WORK_HRS)
        o.write(WORK_RATE)
        o.write(str(SALARY))
    
main()

