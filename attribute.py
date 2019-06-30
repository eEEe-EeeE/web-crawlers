
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s, %s>' % (self.__class__.__name__, self.name)


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'int')


class VarcharField(Field):
    def __init__(self, name):
        super(VarcharField, self).__init__(name, 'varchar')

