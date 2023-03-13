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
        self.rent = int(input("\nHow much rent are you charging your tenant? Enter numbers only no comma, decimal, or special character."))
        self.laundry = input("How much are you charging your tenant for laundry? Enter numbers only no comma, decimal, or special character. If none, enter '0'. ")
        self.storage = input("How much are you charging your tenant for storage? Enter numbers only no comma, decimal, or special character. If none, enter '0'.")
        self.misc = input("Please enter the total of any misc. charges to your tenant that have not been previously asked? Enter numbers only no comma, decimal, or special character. If none, enter '0'.")
        self.total_monthly_income = int(self.rent) + int(self.laundry) + int(self.storage) + int(self.misc)
        print(f"\nYour total monthly income on the property is ${self.total_monthly_income}.")


#combine all expenses
    def expenses(self):
        print(f"\nLet's figure out your total expenses.")
        self.tax = input(f"\nWhat is the total amount of taxes you pay on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. ")
        self.insurance = input(f"What is the total amount you pay to insure the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. ")      
        self.utilities =input(f"What is the total amount of utilities you pay on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character.")
        self.HOA =input(f"What is the total amount pay towards the HOA on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. If none, enter '0'.")
        self.lawn_snow_care =input(f"What is the total amoun you pay on lawn care and snow removal rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. If none, enter '0'.")
        self.vacancy =input(f"What is the total amount you pay towards vacancy rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. If none, enter '0'.")
        self.repairs =input(f"What is the total amount you pay towards repairs on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. If none, enter '0'.")
        self.CapEx=input(f"What is the total amount of you pay towards capital expenditures on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. If none, enter '0'.")
        self.property_management=input(f"What is the total amount you pay on property management on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character.")
        self.mortgage=input(f"What is the total mortgage for the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character.")
        self.total_monthly_expenses = self.tax + int(self.insurance) + int(self.utilities) + int(self.HOA) + int(self.lawn_snow_care) + int(self.vacancy) + int(self.repairs) + int(self.CapEx) + int(self.property_management) + int(self.mortgage)
        print(f"\nYour total monthly expenses on the property are ${self.total_monthly_expenses}")

#annual cash flow is income *12 - expenses
    def cashFlow(self):
        self.total_monthly_cash_flow = self.total_monthly_expenses - self.total_monthly_income
        print(f"\nYour total monthly cash flow is ${self.total_monthly_cash_flow}.")
        self.total_annual_cash_flow = self.total_monthly_cash_flow * 12
        print(f"\nYour total annual cash flow is ${self.total_annual_cash_flow}. ")
       
#calculate investment
    def investment(self):
        print(f"\nLet's figure out your investment total.")
        self.down_payment = input(f"\nHow much did you put down on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character.")
        self.closing_costs = input(f"How much were your closing costs on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character.")
        self.rehab_budget = input(f"How much did you budget for rehab on the property rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character.")
        self.down_payment = input(f"Are there any other expenses torward the purchase of the property you would like to enter rounded to the nearest dollar? Enter numbers only no comma, decimal, or special character. If none, enter '0'.")
        self.total_investment = int(self.down_payment) + int(self.closing_costs) + int(self.rehab_budget) + int(self.down_payment)
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