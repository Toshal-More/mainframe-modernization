# 02 — Bank Transaction Pipeline

A Python pipeline that modernizes a classic COBOL bank transaction batch process.  
Part of the [Mainframe Modernization Portfolio](https://github.com/yourusername/mainframe-modernization).

---

## 📌 What This Project Does

Banks are one of the biggest users of mainframe systems in the world.  
This project simulates how a mainframe batch job processes daily bank transactions by:

- Reading a bank transaction fixed-width flat file (`.dat`) — simulating mainframe input
- Parsing each field by position — just like a COBOL copybook
- Processing Credit and Debit transactions — replacing COBOL IF/ELSE paragraph
- Generating a formatted transaction report with updated balances

---

## 📄 Input File Layout (Copybook)

| Field        | Picture Clause | Start | End | Length |
|--------------|---------------|-------|-----|--------|
| ACCOUNT-ID   | PIC X(8)      | 1     | 8   | 8      |
| ACCOUNT-NAME | PIC X(20)     | 9     | 28  | 20     |
| TRANS-TYPE   | PIC X(2)      | 29    | 30  | 2      |
| TRANS-AMOUNT | PIC 9(6)V99   | 31    | 36  | 6      |
| BALANCE      | PIC 9(8)V99   | 37    | 44  | 8      |

> `CR` = Credit (amount added to balance)  
> `DR` = Debit (amount subtracted from balance)  
> `V99` = Implied decimal — no actual decimal point stored in the file

### Sample Input
```
AC000001Rajesh Kumar        CR00250015000000
AC000002Sunita Mehta        DR00150008500000
AC000003Vikram Shah         CR01000025000000
```

---

## ⚙️ How It Works

```
transactions.dat → Format_IP() → Cal_New_Bal() → Write_Report() → transactions_report.txt
    (input)          (parse)       (CR/DR logic)     (output)
```

| Python Function  | COBOL Equivalent               |
|------------------|-------------------------------|
| `Format_IP()`    | READ + MOVE to working storage |
| `Cal_New_Bal()`  | IF/ELSE + COMPUTE paragraph    |
| `Write_Header()` | WRITE HEADER-RECORD            |
| `Write_Report()` | WRITE DETAIL-RECORD            |

**Business Logic:**
```python
if TRANS_TYPE == 'CR':
    NEW_BALANCE = BALANCE + TRANS_AMOUNT   # Credit → add to balance
else:
    NEW_BALANCE = BALANCE - TRANS_AMOUNT   # Debit  → subtract from balance
```

---

## 📊 Sample Output

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

---

## 🚀 How to Run

```bash
# Navigate into this project
cd COBOL-To-Python-Pipeline/02_bank-transaction-pipeline

# Run the pipeline
python src/parser.py

# Check the output
# Open output/transactions_report.txt
```

---

## 💡 Key Concepts Demonstrated

- Fixed-width flat file parsing
- Implied decimal handling — `PIC 9(6)V99` to Python float
- CR/DR business logic — Credit and Debit transaction processing
- Structured report generation — header and detail pattern
- Function based design — each function mirrors a COBOL paragraph

---

## 🔮 Future Enhancements

- [X] Load transactions into SQLite database
- [X] Export results to CSV
- [ ] Flag overdraft accounts where NEW_BALANCE is negative
- [ ] Add transaction date field
- [ ] Add EBCDIC decoding for real mainframe files

<<<<<<< HEAD
---
=======
---
>>>>>>> a8b4db5ca129be916af3e9765710adf6383ddabb
