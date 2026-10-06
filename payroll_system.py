# ============================================================
# SMART EMPLOYEE PAYROLL SYSTEM
# ============================================================
# Calculates employee salary with tax, bonus, and increment
# Concepts: Variables, Data Types, Control Flow, Nested if, Tax Slab
# ============================================================

# ---------- Company Information ----------
company_name = input("Enter the Company Name: ")
company_id = input("Enter the Company ID: ")
company_address = input("Enter the Company Address: ")
contact_number = input("Enter the Contact Number: ")
hr_manager = input("Enter the HR Manager: ")

# ---------- Employee Details ----------
employee_name = input("Enter the Employee Name: ")
employee_id = input("Enter the Employee ID: ")
employee_address = input("Enter the Employee Address: ")
department = input("Enter the Department: ")
designation = input("Enter the Designation: ")
date_of_joining = input("Enter the Date of Joining: ")
age = int(input("Enter the Age: "))
gender = input("Enter the Gender: ")
mobile_number = input("Enter the Mobile Number: ")
email = input("Enter the Email: ")
pan_number = input("Enter the PAN Number: ")
bank_account = input("Enter the Bank Account: ")

# ---------- Salary Structure ----------
basic_salary = float(input("Enter the Basic Salary: "))
hra = float(input("Enter the HRA: "))
transport_allowance = float(input("Enter the Transport Allowance: "))
medical_allowance = float(input("Enter the Medical Allowance: "))
special_allowance = float(input("Enter the Special Allowance: "))

# ---------- Attendance ----------
total_working_days = int(input("Enter the Total Working Days: "))
days_present = int(input("Enter the Days Present: "))
days_absent = int(input("Enter the Days Absent: "))
paid_leave = int(input("Enter the Paid Leave: "))

# ---------- Deductions ----------
pf_rate = float(input("Enter the PF Rate: "))
professional_tax = float(input("Enter the Professional Tax: "))
loan_deduction = float(input("Enter the Loan Deduction: "))

# ---------- Performance ----------
performance_score = int(input("Enter the Performance Score: "))
year_of_service = int(input("Enter the Years of Service: "))

# ---------- Status Flags ----------
is_permanent = True
is_on_probation = False
is_eligible_for_bonus = True
insurance_linked = None

# ============================================================
# CALCULATIONS
# ============================================================
gross_salary = basic_salary + hra + transport_allowance + medical_allowance + special_allowance
pf_deduction = basic_salary * pf_rate / 100
total_deduction = pf_deduction + professional_tax + loan_deduction
net_salary = gross_salary - total_deduction
per_day_salary = gross_salary / total_working_days
absent_deduction = per_day_salary * days_absent

# ============================================================
# DECISION 1 — Performance Grade
# ============================================================
if performance_score >= 90:
    grade_category = "A - Excellent"
elif performance_score >= 75:
    grade_category = "B - Good"
elif performance_score >= 60:
    grade_category = "C - Average"
else:
    grade_category = "D - Needs Improvement"

# ============================================================
# DECISION 2 — Attendance Status
# ============================================================
if days_present >= 24:
    category = "Excellent Attendance"
elif days_present >= 19:
    category = "Good Attendance"
else:
    category = "Poor Attendance"

# ============================================================
# DECISION 3 — Bonus Calculation
# ============================================================
if performance_score >= 90:
    bonus = gross_salary * 20 / 100
elif performance_score >= 75:
    bonus = gross_salary * 10 / 100
elif performance_score >= 60:
    bonus = gross_salary * 5 / 100
else:
    bonus = 0

# ============================================================
# DECISION 4 — Tax Slab Calculation
# ============================================================
annual_salary = net_salary * 12
if annual_salary <= 300000:
    tax = 0
elif annual_salary <= 600000:
    tax = (annual_salary - 300000) * 5 / 100
elif annual_salary <= 900000:
    tax = 15000 + (annual_salary - 600000) * 10 / 100
elif annual_salary <= 1200000:
    tax = 45000 + (annual_salary - 900000) * 15 / 100
else:
    tax = 90000 + (annual_salary - 1200000) * 30 / 100

# ============================================================
# DECISION 5 — Increment Eligibility (Nested if)
# ============================================================
if year_of_service >= 1:
    if performance_score >= 75:
        if is_permanent:
            increment = "Eligible for 15% increment"
        else:
            increment = "Not Permanent - no increment"
    else:
        increment = "Low Performance - no increment"
else:
    increment = "Minimum 1 year service required"

# ============================================================
# OUTPUT — Payroll Summary
# ============================================================
print("=" * 50)
print("EMPLOYEE PAYROLL SUMMARY")
print("=" * 50)
print(f"{'Employee Name':<20}:{employee_name}")
print(f"{'Gross Salary':<20}:₹{gross_salary:.2f}")
print(f"{'PF Deduction':<20}:₹{pf_deduction:.2f}")
print(f"{'Total Deduction':<20}:₹{total_deduction:.2f}")
print(f"{'Net Salary':<20}:₹{net_salary:.2f}")
print(f"{'Performance Score':<20}:{performance_score}")
print(f"{'Performance Grade':<20}:{grade_category}")
print(f"{'Attendance':<20}:{category}")
print(f"{'Bonus':<20}:₹{bonus:.2f}")
print(f"{'Tax':<20}:₹{tax:.2f}")
print(f"{'Increment':<20}:{increment}")
print("=" * 50)
