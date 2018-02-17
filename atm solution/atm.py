class ATM:
    def __init__(self,balance,bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def withdraw(self,request):
        print "Welcome to ", self.bank_name
        print "Current balance = ",self.balance
        print "=================================="
        if   request > self.balance:
            print("Can't give you all this money !!")
        elif request < 0:
            print("More than zero plz!")
        else:
            banknotes = [100,50,20,10,5,4,3,2,1]
            r = request
            for banknote in banknotes:
                while request >= banknote:
                    print "give ", banknote
                    request -= banknote
            self.balance = self.balance - r
            self.withdrawals_list.append(r)
        print "=================================="

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print withdrawal


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
