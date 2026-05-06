# 01 — Employee Salary Pipeline

A Python pipeline that modernizes a classic COBOL payroll batch process.  
Part of the [Mainframe Modernization Portfolio](https://github.com/yourusername/mainframe-modernization).

---

## 📌 What This Project Does

- Reads an employee payroll fixed-width flat file (`.dat`) — simulating mainframe input
- Parses each field by position — just like a COBOL copybook
- Calculates gross salary — replacing COBOL COMPUTE paragraph
- Generates a formatted salary report as output — replacing mainframe SYSOUT

---

## 📄 Input File Layout (Copybook)

| Field        | Picture Clause | Start | End | Length |
|--------------|---------------|-------|-----|--------|
| EMP-ID       | PIC X(6)      | 1     | 6   | 6      |
| EMP-NAME     | PIC X(22)     | 7     | 28  | 22     |
| WORKING-HRS  | PIC 9(4)      | 29    | 32  | 4      |
| WORKING-RATE | PIC 9(3)V99   | 33    | 37  | 5      |

> `V99` = Implied decimal — no actual decimal point stored in the file

### Sample Input
```
E00001Ramesh Patil          016005075
E00002Priya Sharma          018505250
E00003Akash Mehta           020004800
```

---

## ⚙️ How It Works

```
employees.dat → format_IP() → calculate_salary() → write_report() → employees_salary.txt
   (input)        (parse)         (logic)              (output)      
                                                  → Employee.db       (SQLite)
                                                  → employees_salary.csv (CSV)
```

| Python Function      | COBOL Equivalent               |
|----------------------|-------------------------------|
| `format_IP()`        | READ + MOVE to working storage |
| `calculate_salary()` | COMPUTE paragraph              |
| `write_header()`     | WRITE HEADER-RECORD            |
| `write_report()`     | WRITE DETAIL-RECORD            |

**Business Logic:**
```python
SALARY = WORKING_HRS * WORKING_RATE
```

---

## 📊 Sample Output

```
================================================================================
                          EMPLOYEE SALARY REPORT
                      COBOL TO PYTHON PIPELINE PROJECT
================================================================================
EMP ID    EMPLOYEE NAME       WORKING HRS    WORKING RATE          SALARY
--------------------------------------------------------------------------------
E00001    Ramesh Patil                160           50.75         8120.00
E00002    Priya Sharma               185           52.50         9712.50
E00003    Akash Mehta                200           48.00         9600.00
================================================================================
```

---

## 🚀 How to Run

```bash
# Navigate into this project
cd COBOL-To-Python-Pipeline/01_employee-salary-pipeline

# Run Phase 1 - Text Report
python src/parser.py

# Run Phase 2 - SQLite Database
python src/db_loader.py

# Run Phase 3 - CSV Export
python src/csv_export.py

# Check the output folder for all generated files
```

---

## 💡 Key Concepts Demonstrated

- Fixed-width flat file parsing
- Implied decimal handling — `PIC 9(3)V99` to Python float
- Structured report generation — header and detail pattern
- Function based design — each function mirrors a COBOL paragraph
- SQLite database integration — INSERT and SELECT operations
- CSV export using Python built in `csv` module

---

## 🔮 Future Enhancements

- [x] Load data into SQLite database
- [x] Export results to CSV
- [ ] Upload to Cloudflare R2 Cloud Storage
- [ ] Power BI Dashboard
- [ ] Add EBCDIC decoding for real mainframe files

---