import CONST 
import math
import matplotlib.pyplot as plt


class Vector:
	def __init__(self, vec):
		self.vec = vec[:]
		#self.slope = self.vec[1] / self.vec[0]

	def __abs__(self):
		return math.sqrt((self.vec[0]) ** 2 + (self.vec[1]) ** 2)

	def __add__(self, other):
		return Vector([self.vec[0] + other.vec[0], self.vec[1] + other.vec[1]])

	def __sub__(self, other):
		return Vector([self.vec[0] - other.vec[0], self.vec[1] - other.vec[1]])

	def __neg__(self):
		return Vector([-self.vec[0], -self.vec[1]])

	def __mul__(self, other):
		if isinstance(other, Vector):
			return abs(self) * abs(other) * math.cos(angle(self, other))

		elif isinstance(other, (int, float)):
			return Vector([self.vec[0] * other, self.vec[1] * other])

	def __truediv__(self, other):

		if isinstance(other, (int, float)):
			return Vector([self.vec[0] / other, self.vec[1] / other])


	def angle(self, other):
		if 1 + self.slope * other.slope == 0 : 
			return math.pi / 2
		else:	
			return math.atan(abs((self.slope - other.slope) / (1 + self.slope * other.slope)))

class Particle:
	def __init__(self, pos, mass, v0=Vector([0, 0])):
		self.pos = Vector(pos[:])
		self.mass = mass
		self.v = v0

class Charge(Particle):
	def __init__(self, pos, mass, charge, v0=Vector([0, 0])):
		super().__init__(pos, mass, v0=v0)
		self.charge = charge

class Force:
	def __init__(self, forceObj, *args):
		self.forceObj = forceObj(*args)

	def applyForce(self, particle, dt):
		"""
		F = m.a therefore a = F/m 
		"""
		acc = self.forceObj.ForceVec / particle.mass
		particle.v += acc * dt
		particle.pos.vec[0] += particle.v.vec[0] * dt
		particle.pos.vec[1] += particle.v.vec[1] * dt

		return True

class electricalForce:
	def __init__(self, q1, q2):
		self.ForceVec = (q1.pos - q2.pos)  * CONST.K_e * q1.charge * q2.charge / (abs(q1.pos - q2.pos) ** 3)
		self.ForceAbs = abs(self.ForceVec)


class electricalField:
	def __init__(self, q1):
		self.FieldVecFunc = lambda pos : CONST.K_e * q1.charge * (q1.pos - pos) / (abs(q1.pos - pos) ** 3)
		self.FieldAbs = abs(self.FieldVec)

class Gravity:
	def __init__(self, particle):
		self.ForceVec = Vector([0, -CONST.g]) * particle.mass