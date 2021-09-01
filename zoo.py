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
# BONUS: Debe crear una forma interactiva (while True ;)) oara poder ir creando animales e ir agregándolos al ZOO.

class Animals:
	def __init__(self, name, age, healt, happyness):
		self.name = name
		self.age = age
		self.healt = healt
		self.happyness = happyness
	def display_info(self):
		print("-"*5, type(self).__name__, "-"*5)
		print(f"Nombre: {self.name} \nEdad: {self.age} \nSalud: {self.healt} \nFelicidad: {self.happyness}")
	def eat(self):
		self.healt += 10
		self.happyness += 10

class Bear(Animals):
	def __init__(self, name, age=12, healt=50, happyness=40, weight=300, hibernating="No"):
		super().__init__(name, age, healt, happyness)
		self.weight=weight
		self.hibernating = hibernating
	def eat(self):
		super().healt += 15
		super().happyness += 15
	def display_info(self):
		super().display_info()
		print(f"Peso: {self.weight} \nHibernando: {self.hibernating}\n")


class Tiger(Animals):
	def __init__(self, name, age=12, healt=45, happyness=45, fur="Anaranjado"):
		super().__init__(name, age, healt, happyness)
		self.fur= fur
	def eat(self):
		super().healt += 15
		super().happyness += 20
	def display_info(self):
		super().display_info()
		print(f"Pelaje: {self.fur}\n")

class Wolf(Animals):
	def __init__(self, name, age=12, healt=55, happyness=60, typeof="Lupus"):
		super().__init__(name, age, healt, happyness)
		self.typeof = typeof
	def eat(self):
		super().healt += 20
		super().happyness += 20
	def display_info(self):
		super().display_info()
		print(f"Tipo: {self.typeof}\n") 

class Zoo:
	def __init__(self, zoo_name):
		self.animals = []
		self.name = zoo_name
	def print_all_info(self):
		print("-"*30, self.name, "-"*30)
		for animal in self.animals:
			animal.display_info()
	def add_animals(self):
		while True:
			print(f"\n" + "-"*90 + "\n Ingrese el tipo de animal (Oso, Tigre, Lobo) junto con su nombre, ejemplo Oso Baloo")
			a = input(": ")
			a = a.split(" ")
			if a[0].lower() == "oso":
				self.animals.append(Bear(a[1]))
				print (f"{a[1]} ha sido agregado correctamente al zoo ")
			elif a[0].lower() == "tigre":
				self.animals.append(Tiger(a[1]))
				print (f"{a[1]} ha sido agregado correctamente al zoo ")
			elif a[0].lower() == "lobo":
				self.animals.append(Wolf(a[1]))
				print (f"{a[1]} ha sido agregado correctamente al zoo ")
			else :
				print(f"Error de ingreso, {a} \n")
			c= input("Desea ingresar otro animal (S/N):")
			if c.upper() == "N":
				break



zoo1 = Zoo("Pepe's Zoo")
zoo1.add_animals()
zoo1.print_all_info()