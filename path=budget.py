# Get total income
while True:
    try:
        paycheck = float(input("Enter your monthly income: $"))
        if paycheck <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

remaining = paycheck
print(f"Monthly Income: ${paycheck:.2f}")

# … later, in the summary …
print("\n===== BUDGET SUMMARY =====")
print(f"Total Monthly Income: ${paycheck:.2f}") 