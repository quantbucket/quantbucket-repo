from quantbucket import Algorithm
from scipy import stats
import numpy as np

class Application(Algorithm):

	def main(self):
		x_axis_field = self.fields_by_key('x_axis')[0]
		y_axis_field = self.fields_by_key('y_axis')[0]
		x = self.slice_data(x_axis_field,int)
		y = self.slice_data(y_axis_field,int)
		slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
		doc = {
			'slope' : slope,
			'intercept'  : intercept,
			'r_value' : r_value,
			'p_value' : p_value,
			'std_err' : std_err
		}
		return doc