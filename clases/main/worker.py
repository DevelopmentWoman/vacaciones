from datetime import date
from datetime import datetime
class Worker():
    def __init__(self, name, lastname, id, salary,adm_date, actual_date=datetime.today(), bonus_day=15, profit_day=120):
        self.name = name
        self.lastname = lastname
        self.id = id
        self.salary = salary
        self.adm_date = adm_date
        self.bonus_day = bonus_day
        self.profit_day= profit_day
        self.actual_date = actual_date

    
    def integral_salary(self):
        sal = (self.salary/30)+ self.vacation_rate() +self.profit_rate()
        return sal

    
    def vacation_rate(self):
        sal = (self.salary/30*self.bonus_day)/360
        return sal

    def profit_rate(self):
        sal = (self.salary/30*self.profit_day)/360
        return sal
    
    # def integral_bonus(self):





# cl = Worker("Yelitza", "Suniaga", "15891543", 105.4, datetime.strptime('2007-07-15', '%Y-%m-%d'))
# v1=cl.dif_year()
# print(v1)


