import pygame as pg

class Display():
	def __init__(self, dim, col=[255, 255, 255]):
		self.dim = dim
		self.disp = pg.display.set_mode(tuple(dim))
		self.col = col

	def mapPos(self, pos):
		#mapping position from a display with (0, 0) in the middle
		#to a this display
		
		middim = [self.dim[0] / 2, self.dim[1] / 2]
		xpos, ypos = pos[0] + middim[0], middim[1] - pos[1]
		return [xpos, ypos]

	def refresh(self):
		self.disp.fill(tuple(self.col))

class Obj:
	def __init__(self, disp, pos, rad, col=[255, 0, 0]):
		self.disp = disp
		self.pos = disp.mapPos(pos[:])
		self.rad = rad
		self.col = col[:]

	def draw(self):
		pg.draw.circle(self.disp.disp, self.col, self.pos, self.rad)
		return True

	def update(self, func, *args):
		self.pos = self.disp.mapPos(func(*args))
		return True


