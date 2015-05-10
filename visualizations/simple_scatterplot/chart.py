from quantbucket import Base
import numpy as np
import matplotlib.pyplot as plt
import StringIO

class Chart(Base):

	def main(self):
		x_field = self.fields_by_key('x')[0]
		y_field = self.fields_by_key('y')[0]	
		x = self.slice_data(x_field,int)
		y = self.slice_data(y_field,int)
		render = StringIO.StringIO()
		plt.scatter(x, y, alpha=0.5)
		plt.savefig(render,format='png')
		return render