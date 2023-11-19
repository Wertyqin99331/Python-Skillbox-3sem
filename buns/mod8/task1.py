class Transport:
	def __init__(self, coordinates, speed, brand, year, number):
		self.coordinates = coordinates
		self.speed = speed
		self.brand = brand
		self.year = year
		self.number = number

	@property
	def coordinates(self):
		return self._coordinates

	@coordinates.setter
	def coordinates(self, coordinates):
		self._coordinates = coordinates

	@property
	def speed(self):
		return self._speed

	@speed.setter
	def speed(self, speed):
		if type(speed) != int or speed < 0:
			raise ValueError('Speed was wrong')

		self._speed = speed

	@property
	def brand(self):
		return self._brand

	@brand.setter
	def brand(self, brand):
		if type(brand) != str:
			raise ValueError('Brand was wrong')

		self._brand = brand

	@property
	def year(self):
		return self._year

	@year.setter
	def year(self, year):
		if type(year) != int or year < 0:
			raise ValueError('Year was wrong')

		self._year = year

	@property
	def number(self):
		return self._number

	@number.setter
	def number(self, number):
		if type(number) != int:
			raise ValueError('Number was wrong')

		self._number = number

	def _str_(self):
		return f"brand - {self.brand}, year - ({self.year}), number - {self.number}, speed - {self.speed}, coordinates - {self.coordinates}"

	def is_in_area(self, pos_x, pos_y, length, width):
		if pos_x > self.coordinates.x or (pos_x + width) < self.coordinates.x or pos_y > self.coordinates.y or (
			pos_y + length) < self.coordinates.y:
			return False

		return True


class Passenger:
	def __init__(self):
		self._passengers_capacity = None
		self._number_of_passengers = None

	@property
	def passengers_capacity(self):
		return self._passengers_capacity

	@passengers_capacity.setter
	def passengers_capacity(self, passengers_capacity):
		if type(passengers_capacity) != int or passengers_capacity < 0:
			raise ValueError('Passengers capacity was wrong')

		self._passengers_capacity = passengers_capacity

	@property
	def number_of_passengers(self):
		return self._number_of_passengers

	@number_of_passengers.setter
	def number_of_passengers(self, number_of_passengers):
		if type(number_of_passengers) != int or number_of_passengers < 0:
			raise ValueError('Number of passengers was wrong')

		self._number_of_passengers = number_of_passengers


class Cargo:
	def __init__(self, carrying):
		self.carrying = carrying

	@property
	def carrying(self):
		return self._carrying

	@carrying.setter
	def carrying(self, carrying):
		self._carrying = carrying


class Plane(Transport):
	def __init__(self, coordinates, speed, brand, year, number, height):
		super().__init__(coordinates, speed, brand, year, number)
		self._height = height

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		self._height = height


class Auto(Transport):
	def __init__(self, coordinates, speed, brand, year, number):
		super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
	def __init__(self, coordinates, speed, brand, year, number, name, port):
		super().__init__(coordinates, speed, brand, year, number)
		self._name = name
		self._port = port

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def port(self):
		return self._port

	@port.setter
	def port(self, port):
		self._port = port


class Car(Auto):
	def __init__(self, coordinates, speed, brand, year, number):
		super().__init__(coordinates, speed, brand, year, number)


class Bus(Auto, Passenger):
	pass


class CargoAuto(Auto, Cargo):
	pass


class Boat(Ship):
	pass


class PassengerShip(Ship, Passenger):
	pass


class CargoShip(Ship, Cargo):
	pass


class Seaplane(Plane, Ship):
	pass
