class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
        
    def pay(self):
        self.payment = "yes"
        
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid" + str(self.amount)
        else:
            return self.name + " is not paid yet" 
    
israel = Payslips("Israel", "no", 5000)
judah = Payslips("Judah", "no", 3000)

print(israel.status(), "\n", judah.status())

israel.pay()
print("After payment")
print(israel.status(), "\n", judah.status())