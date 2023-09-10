
class Address(object):
    def __init__(self, first_name, middle_name, last_name, salutation):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salutation = salutation


    def __repr__(self):
        return '<Address({self.salutation} {self.first_name} {self.middle_name} {self.last_name!r})>'.format(self=self)
