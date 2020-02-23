

# class CanSum:
#   def __init__(self):
#     pass

# def sum(*args):
	# result = 0
	# for num in args:
	# 	result += num
 #    return result

class CanSum:
	
	def sum(*args):
		result = 0
		for num in args:
			result += num
		return result

# print(sum(1,2,3))
newCalculation = CanSum()
print(newCalculation.sum(1,2,3,4,5))

  