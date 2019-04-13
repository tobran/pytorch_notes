import torch

class des:
	def __init__(self,x):
	
		self.x = x
	
	def describe(self):
		print("Type: {}".format(self.x.type()))
		print("Shape/size: {}".format(self.x.shape))
		print("Values: \n{}".format(self.x))