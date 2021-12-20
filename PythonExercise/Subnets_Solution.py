from itertools import combinations

class Subset_Solutions():
	def __init__(self, nums):
		self.nums = nums
	
	def BitSerialMapping(self):
		size = len(self.nums)
		upper_bound = 1 << size
		all_subset = [ ]
		for bit_sn in range(upper_bound):
			cur_subset = []
			for i in range (size):
				if bit_sn & (1<<i) != 0:
					cur_subset.append(self.nums[i])
			all_subset.append(cur_subset)
		return all_subset
	
	def ElementAdding(self):
		solution = [ [] ]
		for element in self.nums:
			solution += ([current + [element] for current in solution])
		return solution		

	def PythonTool(self):
		solution, size = [], len(self.nums)
		for k in range(size+1):
			solution += [list(comb) for comb in combinations(self.nums, k)]
		return solution


lst = Subset_Solutions([1,2,3])
print (lst.BitSerialMapping())
print (lst.ElementAdding())
print (lst.PythonTool())


