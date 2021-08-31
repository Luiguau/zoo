# Asignatura: Zoo
# Objetivos:
#     Practica la utilización de la herencia
#     Más práctica con asociaciones entre clases.
#     Practica métodos primordiales
#     Mira el polimorfismo en acción

# Imagina un juego donde puedes crear un zoológico y comenzar a criar diferentes tipos de animales. Digamos que por cada zoológico que crees puede haber varios animales diferentes. Comience creando una clase Animal y luego al menos 3 clases específicas de animales que hereden de Animal. (Tal vez leones, tigres y osos, ¡Dios mío!) Cada animal debe tener al menos un nombre, una edad, un nivel de salud y un nivel de felicidad. La clase Animal debe tener un método display_info que muestre el nombre, la salud y la felicidad del animal. También debe tener un método de alimentación que aumente la salud y la felicidad en 10.

# En al menos una de las clases de Animal child que ha creado, agregue al menos un atributo único. Dele a cada animal diferentes niveles predeterminados de salud y felicidad. Los animales también deben responder al método de alimentación con diferentes niveles de cambios en la salud y la felicidad.

# Una vez que haya probado sus diferentes animales y se sienta más cómodo con la herencia, cree una clase de zoológico para ayudar a manejar a todos sus animales.

# Una forma de armar este zoológico es haciendo lo siguiente:
# class Zoo:
#     def __init__(self, zoo_name):
#         self.animals = []
#         self.name = zoo_name
#     def add_lion(self, name):
#         self.animals.append( Lion(name) )
#     def add_tiger(self, name):
#         self.animals.append( Tiger(name) )
#     def print_all_info(self):
#         print("-"*30, self.name, "-"*30)
#         for animal in self.animals:
#             animal.display_info()
# zoo1 = Zoo("John's Zoo")
# zoo1.add_lion("Nala")
# zoo1.add_lion("Simba")
# zoo1.add_tiger("Rajah")
# zoo1.add_tiger("Shere Khan")
# zoo1.print_all_info()

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
	def __init__(self, name, age=12, healt=45, happyness=45, fur="Anaranjado"):
		super().__init__(name, age, healt, happyness)
		self.fur= fur

class Wolf(Animals):
	def __init__(self, name, age=12, healt=55, happyness=60, typeof="lupus"):
		super().__init__(name, age, healt, happyness)
		self.typeof = typeof


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