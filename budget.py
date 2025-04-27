import os

def main():
    print("Welcome to the Budget Planner!")
    
    # Get total income
    while True:
        try:
            paycheck = float(input("Enter your total paycheck amount: $"))
            if paycheck <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    remaining = paycheck
    print(f"Starting amount: ${paycheck:.2f}")
    
    # Get expenses
    expenses = {}
    
    # If there's an expenses.txt, offer to load it
    if os.path.isfile('expenses.txt') and \
       input("Load expenses from 'expenses.txt'? (y/n): ").strip().lower() == 'y':
        
        with open('expenses.txt') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                try:
                    # split on the first '-' to separate name from amount
                    name_part, amount_part = line.split('-', 1)
                    name = name_part.strip()
                    # remove any leading '$' and parse float
                    amount = float(amount_part.strip().lstrip('$'))
                except ValueError:
                    print(f"Warning: could not parse line: {line}")
                    continue
                
                expenses[name] = amount
                remaining -= amount
                print(f"Loaded {name}: ${amount:.2f}. Remaining: ${remaining:.2f}")
    
    else:
        # Get expenses
        while True:
            try:
                num_expenses = int(input("How many regular expenses do you have? "))
                if num_expenses < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        for i in range(num_expenses):
            name = input(f"Enter name for expense #{i+1}: ")
            while True:
                try:
                    amount = float(input(f"Enter amount for {name}: $"))
                    if amount <= 0:
                        print("Please enter a positive number.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            
            expenses[name] = amount
            remaining -= amount
            print(f"Remaining: ${remaining:.2f}")
    
    # Optional allocations
    optional_allocations = {}
    if remaining > 0:
        print("\nYou have ${:.2f} remaining. Let's allocate it to optional categories.".format(remaining))
        
        while remaining > 0:
            name = input("Enter a category name (or 'done' to finish): ")
            if name.lower() == 'done':
                break
                
            while True:
                try:
                    percentage = float(input(f"What percentage of your remaining ${remaining:.2f} would you like to allocate to {name}? (0-100): "))
                    if percentage < 0 or percentage > 100:
                        print("Please enter a percentage between 0 and 100.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            
            amount = (percentage / 100) * remaining
            optional_allocations[name] = amount
            remaining -= amount
            print(f"Allocated ${amount:.2f} to {name}")
            print(f"Remaining: ${remaining:.2f}")
            
            if remaining <= 0.01:  # Account for floating point errors
                print("All money has been allocated!")
                remaining = 0
                break
    
    # Print budget summary
    print("\n===== BUDGET SUMMARY =====")
    print(f"Total Income: ${paycheck:.2f}")
    
    print("\nEXPENSES:")
    total_expenses = 0
    for name, amount in expenses.items():
        print(f"{name}: ${amount:.2f}")
        total_expenses += amount
    print(f"Total Expenses: ${total_expenses:.2f} ({(total_expenses/paycheck)*100:.1f}% of income)")
    
    if optional_allocations:
        print("\nOPTIONAL ALLOCATIONS:")
        total_optional = 0
        for name, amount in optional_allocations.items():
            print(f"{name}: ${amount:.2f}")
            total_optional += amount
        print(f"Total Optional Allocations: ${total_optional:.2f} ({(total_optional/paycheck)*100:.1f}% of income)")
    
    if remaining > 0:
        print(f"\nUnallocated: ${remaining:.2f} ({(remaining/paycheck)*100:.1f}% of income)")

if __name__ == "__main__":
    main()
