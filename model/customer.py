import shortuuid


class Customer(object):
    def __init__(self, name, address, phone, email):
        self.id = shortuuid.uuid()
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __init__(self, _id, name, address, phone, email):
        self.id = _id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __repr__(self):
        return '<Customer(name={self.name!r})>'.format(self=self)
