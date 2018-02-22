salary = input("Enter your starting salary: ")
percent = float(input("Enter the percent for your raise in percentage: "))
years = input("Enter the number of years: ")
print("Starting Salary", "Years", "Percent Increase")

for year in range(1, years + 1):
    if year == 1:
        print(str(year), "{:.2f}".format(salary))
        continue
    update = (salary * percent)
    salary += update
    print(str(year), "{:.2f}".format(salary))