class AbstractFactory(object):
    def create_chair(self):
        raise NotImplementedError()

    def create_sofa(self):
        raise NotImplementedError()

    def create_table(self):
        raise NotImplementedError()

class Chair(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

class Sofa(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

class Table(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair('victorian chair')

    def create_sofa(self):
        return Sofa('victorian sofa')

    def create_table(self):
        return Table('victorian table')

class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair('modern chair')

    def create_sofa(self):
        return Sofa('modern sofa')

    def create_table(self):
        return Table('modern table')

class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair('futuristic chair')

    def create_sofa(self):
        return Sofa('futuristic sofa')

    def create_table(self):
        return Table('futuristic table')

factory_1 = VictorianFactory()
factory_2 = ModernFactory()
factory_3 = FuturisticFactory()

print(factory_1.create_chair())
print(factory_1.create_sofa())
print(factory_1.create_table())
print(factory_2.create_chair())
print(factory_2.create_sofa())
print(factory_2.create_table())
print(factory_3.create_chair())
print(factory_3.create_sofa())
print(factory_3.create_table())