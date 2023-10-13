from worker import Worker
from datetime import datetime
from datetime import timedelta

class Vacation(Worker):
    def __init__(self, name, lastname, id, salary, adm_date, actual_date=datetime.today(), bonus_day=15, profit_day=120, holid_day=0):
        super().__init__(name, lastname, id, salary, adm_date, actual_date, bonus_day, profit_day)
        self.holid_day=holid_day
        self.mensaje = ''
        

    def dif_year(self):
       
        dif_date = int(self.actual_date.year - self.adm_date.year)
        if dif_date <= 0: 
            self.mensaje="El trabajador no ha cumplido el tiempo reglamentario para calculo de vacaciones"
            return
        else:
            return dif_date
        # - datetime.now().year

    def add_day(self):
        dif_y = self.dif_year()
        
        if self.mensaje == '':
            ad_day= self.bonus_day + dif_y + self.holid_day - 1
            return ad_day
    
    def end_date_vacation(self):
        # print(self.add_day())
        add_d=self.add_day()
        print(add_d)
        if self.mensaje == '':
            end_date= self.actual_date + timedelta(days=add_d) 
            return(end_date)
        else:
            return self.mensaje
    




cl = Vacation("Yelitza", "Suniaga", "15891543", 105.4, datetime.strptime('2022-07-15', '%Y-%m-%d'), datetime.strptime('2023-10-15', '%Y-%m-%d'),15,120,2)
v1=cl.end_date_vacation()
print(v1)
if cl.mensaje=='':
    print(cl.mensaje)

