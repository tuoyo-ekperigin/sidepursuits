
class Organization(object):

    def __init__(self, _id, name, address):
        self.id = _id
        self.name = name
        self.address = address

    def __repr__(self):
        return '<Organization(name={self.name!r})>'.format(self=self)