class Truck:
    def __init__(self,ID,location,time_of_depart,truck_current_time=None):
        self.ID=ID
        self.packages=[]
        self.location=location
        self.miles = 0.0
        self.time_of_depart=time_of_depart
        self.truck_current_time=truck_current_time


    #def get_mileage_at_time(self,truck, user_time):



