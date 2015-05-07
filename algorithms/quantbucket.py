class Algorithm():
	def __init__(self,data,schema):
		self.data = data
		self.schema = schema
		self.output = self.main()

	def main(self):
		return []

	def fields_by_key(self,key):
		return self.schema[key]

	def slice_data(self,field):
		return [dic[field] for dic in listDict]