#updates 
from soupclass8 import C_sort, w_csv


class Main(object):
	def __init__(self, fnames):
		self.fnames = fnames #(new, old)
		self.new_f = dictionarify(self.fnames[0])
		self.target_f = dictionarify(self.fnames[1])
	def update(self, unique_id, *argv):
		#checks to see if the criteria are all there
		new_csv = self.new_f
		for i in range(0, len(argv)):
			try:
				new_csv[0][argv[i]]
				self.target_f[0][argv[i]]
			except KeyError as KE:
				print("{0} not found.".format(argv[i]))
		#takes the product id for the current entry in target_f and adds it to the matching new_csv dictionary
		for i in range(0, len(new_csv)):
			target_id = new_csv[i][unique_id]
			for i_2 in range(0, len(self.target_f)):
				if self.target_f[i_2][unique_id] == target_id:
					new_csv[i]['Product Id'] = self.target_f[i_2]['Product Id']
		w_csv(new_csv, 'Updates.csv')

		return new_csv



'''def locate_item(d, crit, value):
	#d is the list of dictionaries, crit is the key and value is of course the desired value
	for i in range(0, len(d)):
		d[i].get(crit)'''












def dictionarify(x):
	#should produce list of dictionaries from a csv, with the column headers as the keys
	item = C_sort(x)
	items = item.contents
	crit = item.contents[0]
	results = []
	for i in range(1, len(items)):
		d = dict.fromkeys(crit, 0)
		for i_2 in range(0, len(items[i])):
			d[crit[i_2]] = items[i][i_2]
		results.append(d)
	return results

test = Main(('newinfo.csv','target.csv'))
crits = ['Card Effect','Critical','Finish']
result = test.update('Card Number', crits)
