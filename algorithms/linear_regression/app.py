from quantbucket import Algorithm
from scipy import stats
import numpy as np

class Application(Algorithm):

	def main(self):
		x = self.data(dataset_fields('x_axis')[0])
		y = self.data(dataset_fields('y_axis')[0])
		slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
		doc = {
			'slope' : slope,
			'intercept'  : intercept,
			'r_value' : r_value,
			'p_value' : p_value,
			'std_err' : std_err
		}
		return doc