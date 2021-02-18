

class GetObservationsInRangeRequest:
    
    def __init__(self, date1, date2):
        self.date1 = date1
        self.date2 = date2

    def getDate1(self):
        return self.date1

    def getDate2(self):
        return self.date2
