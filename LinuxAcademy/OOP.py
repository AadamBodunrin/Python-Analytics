# Creating classes

class Car:
    """
    Car models a car w/ tires and an engine
    """

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def description(self):
        return("A car with an {} engine and {} tires.".format(self.engine, self.tires))

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0

civic = Car('4-cylinder', ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'])
print(civic.engine)
print(civic.tires)
print(civic.description)
print(civic.description())


import math 
class Tire:
    """
    Tire represents a tire that 
    would be used with an automobile
    """

    def __init__(self, tire_type,width, ratio, diameter, brand = "", construction = "R" ):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction
    
    def circumference(self):
        """
        The cicumference of the tires in inches
        >>> tire = Tire("P", 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        side_wall_inches = self._side_wall_inches()
        total_diameter = side_wall_inches* 2 + self.diameter
        return (round(total_diameter * math.pi, 1))

    def __repr__(self):
        """
        Represent the tire's information in the standard 
        notation present on the side of the tire. Example: 'P215/65R15'
        """
        return ("{}{}/{}".format(self.tire_type, self.width, self.ratio) 
        + "{}{}".format(self.construction, self.diameter))
    
    def _side_wall_inches(self):
        return (self.width * (self.ratio/100)) / 25.4
    
class SnowTire(Tire):
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        super().__init__(tire_type, width, ratio, diameter, brand, construction)
        #python2 Tire.__init__(self, tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness
        
    def circumference(self):
        """
        The circumference of a tire w/ show chains in inches.
        >>> tire = SnowTire('P', 205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        """
        side_wall_inches = self._side_wall_inches()
        total_diameter = (side_wall_inches + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)
        
    def __repr__(self):
        return super().__repr__() + " (Snow)"


tire = Tire("P", 205, 65, 15)
tires = [tire, tire, tire, tire]
honda = Car(tires = tires , engine = "4-cylinder")
print(honda.description())
print(honda.wheel_circumference())

tir = SnowTire("P", 205, 65, 15, 2)
tir = [tir, tir, tir, tir]
conda = Car(tires = tir , engine = "4-cylinder")
print(conda.wheel_circumference())
print(tir)
