class Atm(object) :

    def __init__(self,card_number,pin_number,nameOnCard,cashWithdraw,expireDate,balanceLeft) :
        self.card_number = card_number
        self.pin_number = pin_number
        self.nameOnCard = nameOnCard
        self.cashWithdraw = cashWithdraw
        self.expireDate = expireDate
        self.balanceLeft = balanceLeft

    def CashWithdrawl(self,nameOnCard,cashWithdraw) :
        if self.cashWithdraw >= 10000 and self.cashWithdraw <20000 :
            print("Your cash withdraw is Excellent")
        elif self.cashWithdraw >=20000 : 
            print("Your cash withdraw is Awesome")
        else :
            print("Your cash withdraw is good")
    
    def BalanceEnquiry(self,balanceLeft,card_number,pin_number,nameOnCard,expireDate) :
        print("Balance Inquiry : ")
        print("your left balance is " , self.balanceLeft)
        print("Your card number is " , self.card_number)
        print("Your pin number is " , self.pin_number)
        print("Your name on card is " , self.nameOnCard)
        print("Your card expire date is " , self.expireDate)
    
    
Atm1 = Atm(1212121212,1000,"Soham Upadhyay",15000,"10/2030",65000)
Atm1.CashWithdrawl("Soham Upadhyay",15000)
Atm1.BalanceEnquiry(65000,1212121212,1000,"Soham Upadhyay","10/2030")