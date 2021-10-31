import utile
'''
q1 = utile.Charge([0, 0], 1, 1)
q2 = utile.Charge([100, 100], 1, -1)
F1 = utile.Force(utile.electricalForce, q1, q2)
F2 = utile.Force(utile.electricalForce, q2, q1)

OBJECTS = [[q1, F1], [q2, F2]]
'''
m1 = utile.Particle([0, 50], 1,v0 = utile.Vector([10, 10]) )
F1 = utile.Force(utile.Gravity, m1)
OBJECTS = [[m1, F1]]
