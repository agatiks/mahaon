#-------------------------------------------------------------------------------
# Name:        модуль2
# Purpose:
#
# Author:      Ученик
#
# Created:     06.11.2017
# Copyright:   (c) Ученик 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Employee:
    def calculate_payroll(self):
        pass
class Hourly_employee(Employee):
    def __init__(self, hour):
        self.hour=hour
        self.calculate_payroll()
    def calculate_payroll(self):
        self.payroll=20.8*8*self.hour
    def print_info(self):
        print("Среднемесячная заработная плата - ", self.payroll)
class Fixedterm_employee(Employee):
    def __init__(self, term):
        self.term=term
        self.calculate_payroll()
    def calculate_payroll(self):
        self.payroll=self.term
    def print_info(self):
        print("Среднемесячная заработная плата - ", self.payroll)
Onton=Hourly_employee(1234)
Tania=Fixedterm_employee(567890)
Onton.print_info()
Tania.print_info()