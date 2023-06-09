class RetInvestment():
    def __init__(self,):
         self.total_monthly_income = 0
         self.total_monthly_expenses = 0
         self.total_monthly_cash_flow = 0
         self.total_annual_cash_flow = 0
         self.return_on_investment = 0


#combine all monthly income
    def income(self):
        print(f"\nLet's figure out your total monthly expenses.")
        while True:
            self.rent = input(f"\nHow much rent are you charging your tenant? Enter numbers only no comma, decimal, or special character. For none type '0'.")
            try:
                self.rent = int(self.rent)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.laundry = input(f"\nHow much are you charging your tenant for laundry services? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.laundry = int(self.laundry)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.storage = input(f"\nHow much are you charging your tenant for storage? Enter numbers only no comma, decimal, or special character. For none type '0'.")
            try:
                self.storage = int(self.storage)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.misc = input(f"\nPlease enter the total of any misc. charges to your tenant that have not been previously asked? Enter numbers only no comma, decimal, or special character. For none type '0'.")
            try:
                self.misc = int(self.misc)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")
     
        self.total_monthly_income = int(self.rent) + int(self.laundry) + int(self.storage) + int(self.misc)
        print(f"\nYour total monthly income on the property is ${self.total_monthly_income}.")


#combine all expenses
    def expenses(self):
        print(f"\nLet's figure out your total expenses.")
        while True:
            self.tax = input(f"\nWhat is the total amount of taxes you pay on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.tax = int(self.tax)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.insurance = input(f"\nWhat is the total amount you pay to insure the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.insurance = int(self.insurance)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.utilities = input(f"\nWhat is the total amount of utilities you pay on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.utilities = int(self.utilities)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.HOA = input(f"\nWhat is the total amount pay towards the HOA on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.HOA = int(self.HOA)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.lawn_snow_care = input(f"\nWhat is the total amount you pay on lawn care and snow removal rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.lawn_snow_care = int(self.lawn_snow_care)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.vacancy = input(f"\nWhat is the total amount you pay towards vacancy rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.vacancy = int(self.vacancy)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")
        
        while True:
            self.repairs = input(f"\nWhat is the total amount you pay towards repairs on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.repairs = int(self.repairs)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.CapEx = input(f"\nWhat is the total amount you pay towards capital expenditures on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.CapEx = int(self.CapEx)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.property_management = input(f"\nWhat is the total amount you pay on property managment on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.property_management = int(self.property_management)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.mortgage = input(f"\nWhat is the total mortgage on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.mortgage = int(self.mortgage)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        self.total_monthly_expenses = self.tax + int(self.insurance) + int(self.utilities) + int(self.HOA) + int(self.lawn_snow_care) + int(self.vacancy) + int(self.repairs) + int(self.CapEx) + int(self.property_management) + int(self.mortgage)

        print(f"\nYour total monthly expenses on the property are ${self.total_monthly_expenses}")

#annual cash flow is income *12 - expenses
    def cashFlow(self):
        self.total_monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
        print(f"\nYour total monthly cash flow is ${self.total_monthly_cash_flow}.")
        self.total_annual_cash_flow = self.total_monthly_cash_flow * 12
        print(f"\nYour total annual cash flow is ${self.total_annual_cash_flow}. ")
       
#calculate investment
    def investment(self):
        print(f"\nLet's figure out your investment total.")

        while True:
            self.down_payment = input(f"\nHow much did you put down on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.down_payment = int(self.down_payment)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.closing_costs = input(f"\nHow much were your closing costs on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.closing_costs = int(self.closing_costs)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.rehab_budget = input(f"\nHow much did you budget for rehab on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.rehab_budget = int(self.rehab_budget)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")

        while True:
            self.other = input(f"\nAre there any other expenses torward the purchase of the property you would like to enter rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. For none type '0'")
            try:
                self.other = int(self.other)
                break
            except:
                print(f"\nHey fast fingers...you have to enter a number with no commas, decimals, or special characters. Try again.")
        
        self.total_investment = int(self.down_payment) + int(self.closing_costs) + int(self.rehab_budget) + int(self.other)
        print(f"\nYour total investment on the property is ${self.total_investment}")
    
    def ROI(self):
        self.return_on_investment = self.total_annual_cash_flow / self.total_investment
        print(f"\nThe ROI for this property is ${self.return_on_investment}")
        cont=input(f"\nWould you like to start over? Type 'Yes' or 'No'")
        while True:
            if cont.lower() == 'yes':
                continue
            if cont.lower() == 'no':
                break

def run():
    while True:
        response = input("Would you like to calculate your ROI? Type 'Yes' or 'No'")
        if response.lower() == 'yes':

            yourROI.income()
            yourROI.expenses()
            yourROI.cashFlow()
            yourROI.investment()
            yourROI.ROI()

        elif response.lower() == 'no':
            print(f"Good. I didn't feel like calculating it anyway.")
            break
        else:
            print(f"Not a valid input - try again.")


yourROI = RetInvestment()
run()