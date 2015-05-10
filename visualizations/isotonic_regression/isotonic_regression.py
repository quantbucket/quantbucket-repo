from quantbucket import Base
import StringIO
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state

class Chart(Base):

	def main(self):
		x_field = self.fields_by_key('x')[0]
		y_field = self.fields_by_key('y')[0]	
		x = np.array(self.slice_data(x_field,int))
		y = np.array(self.slice_data(y_field,int))
		n = len(x)
		render = StringIO.StringIO()
		
		###############################################################################
		# Fit IsotonicRegression and LinearRegression models

		ir = IsotonicRegression()

		y_ = ir.fit_transform(x, y)

		lr = LinearRegression()
		lr.fit(x[:, np.newaxis], y)  # x needs to be 2d for LinearRegression

		###############################################################################
		# plot result

		segments = [[[i, y[i]], [i, y_[i]]] for i in range(n)]
		lc = LineCollection(segments, zorder=0)
		lc.set_array(np.ones(len(y)))
		lc.set_linewidths(0.5 * np.ones(n))

		fig = plt.figure()
		plt.plot(x, y, 'r.', markersize=12)
		plt.plot(x, y_, 'g.-', markersize=12)
		plt.plot(x, lr.predict(x[:, np.newaxis]), 'b-')
		plt.gca().add_collection(lc)
		plt.legend(('Data', 'Isotonic Fit', 'Linear Fit'), loc='lower right')
		plt.title('Isotonic regression')
		plt.savefig(render,format='png')
		return render