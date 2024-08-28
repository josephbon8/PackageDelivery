class PackageData:
    def __init__(self, ids, address, deadline, city, zipcode, state, status, weight):
        self.ids = ids
        self.weight = weight
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.status = status
        self.state = state
        self.delivery_time = None
        self.time_left_hub = None
        self.truck_id = None

    def get_status(self, user_time):
        new_status = "en route by truck " + str(self.truck_id)
        if self.time_left_hub is not None and user_time < self.time_left_hub or self.time_left_hub == None:
            new_status = "At Hub"

        elif self.time_left_hub is not None and user_time > self.delivery_time:
            new_status = "Delivered by truck " + str(self.truck_id) + " at " + str(self.delivery_time)
        return "%s, %s,%s,%s,%s,%s,%s,%s,%s,%s" % (
            self.ids, self.address, self.deadline, self.city, self.zipcode, self.state, new_status,
            self.weight, self.time_left_hub, self.delivery_time)

    def __str__(self):
        return "%s, %s,%s,%s,%s,%s,%s,%s,%s,%s" % (
            self.ids, self.address, self.deadline, self.city, self.zipcode, self.state, self.status,
            self.weight, self.time_left_hub, self.delivery_time)

    def get_address(self):
        return "%s" % self.address
# package = PackageData(1, "155 Nightstreet", "EOD", "Raleigh", 21222, "On route", "N/A", 3.4)
# package.__str__()
