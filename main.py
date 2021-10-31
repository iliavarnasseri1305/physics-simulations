import utile 
import math
import numpy as np
import graphic_utiles as graph
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import variables as var
# varaibles
dt = .1 
#q1 = utile.Charge([0, 0], 1, 1)
#q2 = utile.Charge([100, 100], 1, -1)
#F1 = utile.Force(utile.electricalForce, q1, q2)
#F2 = utile.Force(utile.electricalForce, q2, q1)
#objects = [[q1, F1], [q2, F2]]
XData = [particle.pos.vec[0] for particle, force in var.OBJECTS]
YData = [particle.pos.vec[1] for particle, force in var.OBJECTS]
fig = plt.figure(figsize=(10,10))
ax = plt.axes(xlim=(0,100),ylim=(0,100))
scatter=ax.scatter(XData, YData)



def update(frame_number):
	for obj in var.OBJECTS:
		obj[1].applyForce(obj[0], dt)
	PosData = [q.pos.vec[:] for q, f in var.OBJECTS]
	scatter.set_offsets(PosData[:])
	return scatter, 

anim = anim.FuncAnimation(fig, update, interval=30)
plt.show()

