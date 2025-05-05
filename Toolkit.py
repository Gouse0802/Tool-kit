def Grosstax(filing_statuss,Annual_incomee):
    sum = 0
    remain = 0
    match filing_statuss:
        case "individual":
            if Annual_incomee < 250000:
                return sum
            if Annual_incomee > 250000:
                if Annual_incomee > 250000 and Annual_incomee < 500000:
                    remain = Annual_incomee - 250000
                    sum = (5*remain)/100
                else:
                    sum = (5 * 250000)/100
                    
            if Annual_incomee > 500000:
                if Annual_incomee > 500000 and Annual_incomee < 1000000:
                    remain = Annual_incomee - 500000
                    sum = sum + (20*remain)/100
                else:
                    sum = sum + (20 * 500000)/100
                    
            if Annual_incomee > 1000000:
                remain = Annual_incomee-1000000
                sum = sum + (30*remain)/100
            return sum 
            
        case "seniorcitizen":
            if Annual_incomee < 300000:
                return sum
            if Annual_incomee > 300000:
                if Annual_incomee > 300000 and Annual_incomee < 500000:
                    remain = Annual_incomee - 300000
                    sum = (5*remain)/100
                else:
                    sum = (5 * 200000)/100
                    
            if Annual_incomee > 500000:
                if Annual_incomee > 500000 and Annual_incomee < 1000000:
                    remain = Annual_incomee - 500000
                    sum = sum + (20*remain)/100
                else:
                    sum = sum + (20 * 500000)/100
            
            if Annual_incomee > 1000000:
                remain = Annual_incomee-1000000
                sum = sum + (30*remain)/100        
            return sum
        
        case "superseniorcitizen":
            if Annual_incomee < 500000:
                return sum
            
            if Annual_incomee > 500000:
                if Annual_incomee > 500000 and Annual_incomee < 1000000:
                    remain = Annual_incomee - 500000
                    sum = (20*remain)/100
                else:
                    sum = (20 * 500000)/100
            
            if Annual_incomee > 1000000:
                remain = Annual_incomee-1000000
                sum = sum + (30*remain)/100        
            return sum        



print("Welcome to Income Tax Toolkit!")
print("Please choose a calculator:")

print("1. Mortgage Calculator:")
print("2. Investment Return Calculator:")
print("3. Savings Goal Calculator:")
print("4.Income Tax Calculator:")

Option = int(input("Enter your choice (1-4): "))
match Option:
    case 1:
        loan_term = int(input('Enter the loan term(in years) :'))
        p = int(input('Enter the loan amount :'))
        anuual_rate =int(input('Enter the annual interest rate :'))
        loan_months = loan_term*12
        rate_mon = anuual_rate/100
        rate_mon = rate_mon/12
        
        Monthly_cal = (p*(rate_mon*((1+rate_mon)**loan_months)))/(((1+rate_mon)**loan_months)-1)
        print('The overall monthly mortgage payment is: %4.2f'%Monthly_cal)
    case 2:
        p = int(input('Enter the invested value :'))
        time = int(input('Enter the Time horizon :'))
        rate = int(input('Enter the rate of interest :'))
        
        rate = rate/100
        
        future_val = p*(1+rate)**time
        
        print('The Total value of investment be %.2f'%(future_val))
    case 3:
        future_goal = int(input('Enter your goal amount :'))
        time = int(input('Enter the time :')) 
        anuual_rate = int(input('Enter the rate :'))
        
        Noof_mon = time * 12
        month_rate = anuual_rate/(12*100)
        
        PMT = (future_goal*month_rate)/(((1+month_rate)**Noof_mon)-1)
        
        print('The monthly amount should be :%.2f'%(PMT))
    case 4:
        Annual_income = int(input("Enter the Annual income ="))
        Deductions = int(input("Enter the Deduction ="))
        filing_status = input("Enter the filing_status =")
        filing_status = filing_status.lower()
        Tax_credits = int(input("Enter the Tax credits ="))
        
        Taxable_Income = Annual_income - Deductions
        
        gross = Grosstax(filing_status,Taxable_Income)
        if gross:
            net_tax = gross - Tax_credits
            print("The Total tax is ",net_tax)
        else:
            print("No tax")
