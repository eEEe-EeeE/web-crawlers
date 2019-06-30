from attribute import IntegerField
from attribute import VarcharField
from model import Model


class User(Model):
    id = IntegerField('id')
    name = VarcharField('username')
    email = VarcharField('email')
    password = VarcharField('password')


if __name__ == '__main__':
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    u.save()

