class Algorithm():
	def __init__(self,data,schema):
		self.data = data
		self.schema = schema
		self.output = self.main()

	def main(self):
		return []

	def dataset_fields(self,key):
		fields = self.schema(key)
		return fields