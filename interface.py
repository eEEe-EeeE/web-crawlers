from attribute import IntegerField
from attribute import Varchar


class User(object):
    id = IntegerField('id')
    name = Varchar('username')
