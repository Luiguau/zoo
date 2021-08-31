class Animals:
	def __init__(self, name, age, healt, happyness):
		self.name = name
		self.age = age
		self.healt = healt
		self.happyness = happyness
	def display_info(self):
		print("-"*5, type(self).__name__, "-"*5)
		print(f"Nombre: {self.name}, \nEdad: {self.age}, \nSalud: {self.healt}, \nFelicidad: {self.happyness}")

class Bear(Animals):
	def __init__(self, name, age=12, healt=50, happyness=40, weight=300, hibernating=False):
		super().__init__(name, age, healt, happyness)
		self.weight=weight
		self.hibernating = hibernating
class Tiger(Animals):
	def __init__(self, name, age=12, healt=45, happyness=45):
		super().__init__(name, age, healt, happyness)
		

class Wolf(Animals):
	def __init__(self, name, age=12, healt=55, happyness=60):
		super().__init__(name, age, healt, happyness)


class Zoo:
	def __init__(self, zoo_name):
		self.animals = []
		self.name = zoo_name
	def add_bear(self, name):
		self.animals.append( Bear(name) )
	def add_tiger(self, name):
		self.animals.append( Tiger(name) )
	def add_wolf(self, name):
		self.animals.append( Wolf(name) )
	def print_all_info(self):
		print("-"*30, self.name, "-"*30)
		for animal in self.animals:
			animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_bear("Baloo")
zoo1.add_bear("Bubu")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_wolf("Warwick")
zoo1.add_wolf("Law")
zoo1.print_all_info()