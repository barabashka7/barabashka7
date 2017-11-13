class Employee:
    def calculate_payroll(self):
        pass
    def print_info(self):
        pass
class Hourlyemployee(Employee):
    def calculate_payroll(self,k):
        self.opl=20.8*8*k
    def print_info(self):
        print(self.opl)

class Fixedtermemployee(Employee):
    def calculate_payroll(self,k):
        self.opl=k
    def print_info(self):
        print(self.opl)
ob1=Hourlyemployee()
ob1.calculate_payroll(1000)
ob1.print_info()
ob2=Fixedtermemployee()
ob2.calculate_payroll(50000)
ob2.print_info()
