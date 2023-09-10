import datetime as dt

class Appointment(object):
    def __init__(self, customer, employee, date, address):
        self.customer = customer
        self.employee = employee
        self.date = date
        self.address = address
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<Appointment(name={self.customer} employee={self.employee} date={self.date!r})>'.format(self=self)

