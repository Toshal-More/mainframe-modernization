#OPENING THE .DAT FILE AND START READING THE FILE LINE BY LINE 
def main():
    with open("C:\cobol-to-python-pipeline\input\employees.dat", "r") as f, open("C:\cobol-to-python-pipeline\output\employees_salary.txt", "w") as o:
    
     write_header(o);

     for line in f:
       Record = format_IP(line);
       
       Record = calculate_hrs_rate(Record);

       write_report(o,Record);


def format_IP(line):
  Record = {  "EMPID"     : line[0:6],
              "EMP_NAME"  : line[6:28],
              "WORK_HRS"  : int(line[28:32]),
              "WORK_RATE" : int(line[32:37]) / 100,
              "SALARY"    : 0.0 }
 
  return Record;

def calculate_hrs_rate(Record):
    sal = (Record['WORK_HRS'] * Record['WORK_RATE'])
    Record['SALARY'] = sal
    print("Salary in fun",sal)
    print(Record['SALARY'])

    return Record

def write_report(o,Record):
   o.write(f"{Record['EMPID']:<10}"
           f"{Record['EMP_NAME']:<15}"
           f"{Record['WORK_HRS']:<15}"
           f"{Record['WORK_RATE']:<15.2f}"
           f"{Record['SALARY']:<12.2f}"
           f"\n")
#   o.write(Record['EMPID'])
#   o.write(Record['EMP_NAME'])
#   o.write(str(Record['WORK_HRS']))
#   o.write(str(Record['WORK_RATE']))
#   o.write(str(Record['SALARY']))
#   o.write("\n")

def write_header(o):
   o.write("=" * 75 + "\n")
   o.write(f"{'EMPLOYEE SALARY REPORT':^75}\n")
   o.write(f"{'COBOL TO PYTHON PIPELINE PROJECT':^75}\n")
   o.write("=" * 75 + "\n")
   o.write(f"{'EMP ID':<10}"
           f"{'EMPLOYEE NAME':<15}"
           f"{'WORKING HRS':<15}"
           f"{'WORKING RATE':<15}"
           f"{'SALARY':<12}"
           f"\n")

main()