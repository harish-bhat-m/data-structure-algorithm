
class CurrencyCombination(object):
	""" Implmentation to calculate the different combination of currency
	    denomination for given amount of money"""
	def __init__(self, amount, currency_combination):
		"""Initilization function"""
		self.currency_combination = currency_combination
		self.amount = amount
		self.__calculate()

	def __calculate(self):
		""" Main functionality"""
		print('Denomination are:{}'.format(self.currency_combination))
		print("Entered amont of money is:{}".format(self.amount))
		print("Currency combinations are as follows")
		for i in range(len(self.currency_combination)):
			if self.currency_combination[i] <= self.amount:
				print("------------------------------------")
				total = 0
				j = i
				reminder = self.currency_combination[i]
				while j < len(self.currency_combination):
					if reminder >= self.currency_combination[j]:
						remaining = self.amount - total
						reminder = remaining % self.currency_combination[j]
						currency_count = (remaining - reminder) / self.currency_combination[j]
						total += currency_count * self.currency_combination[j]
						print("Denomination of {} in  {} number".\
							format(self.currency_combination[j],currency_count))
					j += 1

demomination = [2000,500,100,50,20,10,5,2,1]
try:
	rupee = int(input("Enter the ruppes: "))
	CurrencyCombination(rupee, demomination)
except  Exception as error: 
	print("Entered number is not integer. Please try again")
