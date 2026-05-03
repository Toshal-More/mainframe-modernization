# Mainframe Modernization Portfolio

A series of hands-on projects modernizing classic COBOL batch processes using Python, SQL, and Cloud.  
Built as part of my transition from **Mainframe Development → Modern Data Engineering**.

---

## 👨‍💻 About Me

I am a Mainframe Developer with experience in COBOL, JCL, VSAM, DB2, and CICS.  
I am currently transitioning into modern data engineering by rebuilding classic mainframe batch processes using Python and SQL.

This portfolio documents my learning journey — one project at a time.

---

## 🗂️ Portfolio Structure

```
mainframe-modernization/
│
└── COBOL-To-Python-Pipeline/
    ├── 01_employee-salary-pipeline/     ✅ Phase 1 & 2 Completed
    └── 02_bank-transaction-pipeline/    ✅ Phase 1 & 2 Completed
```

---

## 📁 COBOL To Python Pipeline

A series of projects that modernize COBOL batch programs by rewriting them in Python.  
Each project reads a mainframe-style fixed-width flat file, applies business logic, stores data in a SQLite database and generates a formatted report.

### What is a COBOL to Python Pipeline?

Mainframes store data in **fixed-width flat files** and process them using COBOL batch programs.  
These pipelines modernize that process by:

- Reading fixed-width `.dat` files — simulating real mainframe input
- Parsing each field by position — just like a COBOL copybook
- Applying business logic in Python — replacing COBOL paragraphs
- Storing data in SQLite database — replacing mainframe VSAM/DB2
- Generating formatted reports as output — replacing mainframe SYSOUT

---

### Project 01 — Employee Salary Pipeline

**Description:** Reads an employee payroll flat file, calculates gross salary, stores data in SQLite and generates a formatted salary report.

**Copybook Layout:**

| Field        | Picture Clause | Start | End | Length |
|--------------|---------------|-------|-----|--------|
| EMP-ID       | PIC X(6)      | 1     | 6   | 6      |
| EMP-NAME     | PIC X(22)     | 7     | 28  | 22     |
| WORKING-HRS  | PIC 9(4)      | 29    | 32  | 4      |
| WORKING-RATE | PIC 9(3)V99   | 33    | 37  | 5      |

**Business Logic:**
```
GROSS SALARY = WORKING HRS × WORKING RATE
```

**Sample Output:**
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

**Phases:**
```
✅ Phase 1 → Flat file to Text Report
✅ Phase 2 → Flat file to SQLite Database
✅ Phase 3 → CSV Export
🔄 Phase 4 → Streamlit Dashboard
⏳ Phase 5 → AWS S3 Cloud Integration
```

**Tech used:** `Python` `SQLite` `CSV` `Git` `GitHub`

---

### Project 02 — Bank Transaction Pipeline

**Description:** Reads a bank transaction flat file, processes Credit and Debit transactions, stores data in SQLite, exports to CSV and generates a formatted transaction report with updated balances.

**Copybook Layout:**

| Field        | Picture Clause | Start | End | Length |
|--------------|---------------|-------|-----|--------|
| ACCOUNT-ID   | PIC X(8)      | 1     | 8   | 8      |
| ACCOUNT-NAME | PIC X(20)     | 9     | 28  | 20     |
| TRANS-TYPE   | PIC X(2)      | 29    | 30  | 2      |
| TRANS-AMOUNT | PIC 9(6)V99   | 31    | 36  | 6      |
| BALANCE      | PIC 9(8)V99   | 37    | 44  | 8      |

**Business Logic:**
```
CR (Credit) → NEW BALANCE = BALANCE + TRANS AMOUNT
DR (Debit)  → NEW BALANCE = BALANCE - TRANS AMOUNT
```

**Sample Output:**
```
================================================================================
                         BANK TRANSACTION REPORT
                     COBOL TO PYTHON PIPELINE PROJECT
================================================================================
ACC ID      ACCOUNT NAME           TYPE      AMOUNT       BALANCE    NEW BALANCE
--------------------------------------------------------------------------------
AC000001    Rajesh Kumar           CR       2500.00     150000.00     152500.00
AC000002    Sunita Mehta           DR       1500.00      85000.00      83500.00
AC000003    Vikram Shah            CR      10000.00     250000.00     260000.00
================================================================================
```

**Phases:**
```
✅ Phase 1 → Flat file to Text Report
✅ Phase 2 → Flat file to SQLite Database
✅ Phase 3 → CSV Export
🔄 Phase 4 → Streamlit Dashboard
⏳ Phase 5 → AWS S3 Cloud Integration
```

**Tech used:** `Python` `SQLite` `CSV` `Git` `GitHub`

---

## 🛠️ Tech Stack

| Technology | Purpose | Status |
|------------|---------|--------|
| Python 3.11 | Core programming language | ✅ In use |
| SQLite | Local database integration | ✅ In use |
| Git | Version control | ✅ In use |
| GitHub | Code hosting and portfolio | ✅ In use |
| CSV | Data export format | ✅ In use |
| Streamlit | Dashboard visualization | 🔄 In Progress |
| AWS S3 | Cloud integration | ⏳ Coming soon |

---

## 🔮 Roadmap

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 1 | Flat file to Text Report | ✅ Completed |
| Phase 2 | SQLite Database Integration | ✅ Completed |
| Phase 3 | CSV Export | ✅ Completed |
| Phase 4 | Streamlit Dashboard | 🔄 In Progress |
| Phase 5 | Cloud Integration (AWS S3) | ⏳ Planned |

---

## 💡 Key Concepts Demonstrated

- Fixed-width flat file parsing — reading mainframe style data in Python
- Implied decimal handling — converting `PIC 9(x)V99` to Python float
- Business logic migration — replacing COBOL paragraphs with Python functions
- Database integration — inserting and querying data using SQLite
- Structured report generation — header, detail, footer pattern
- Function based design — each function mirrors a COBOL paragraph
- Version control — Git and GitHub for all projects

---

## 🚀 How to Run Any Project

**Prerequisites:**
- Python 3.11 or above
- VS Code (recommended)
- DB Browser for SQLite (to view database)

**Steps:**
```bash
# 1. Clone the repository
git clone https://github.com/Toshal-More/mainframe-modernization.git

# 2. Navigate into any project
cd mainframe-modernization/COBOL-To-Python-Pipeline/01_employee-salary-pipeline

# 3. Run Phase 1 - Text Report
python src/parser.py

# 4. Run Phase 2 - Database Loader
python src/db_loader.py

# 5. Check the output folder for report and database
```

---

*This portfolio is actively growing — new phases and projects added regularly as I continue my modernization journey.*