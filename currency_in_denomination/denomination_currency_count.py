""" main implementation of the logic """
class CurrencyCombination():
    """ Implmentation to calculate the different combination of currency
        denomination for given amount of money"""
    def __init__(self, rupee, denomination):
        self.currency_combination = denomination
        self.amount = rupee
        self.result_list = []

    def calculate(self):
        """ Main functionality"""
        no_of_iteration = len(self.currency_combination)
        for i in range(no_of_iteration):
            if self.currency_combination[i] <= self.amount:
                self.result_list.append("------------------------------------")
                total = 0
                j = i
                reminder = self.currency_combination[i]
                no_of_iteration = len(self.currency_combination)
                while j < no_of_iteration:
                    if reminder >= self.currency_combination[j]:
                        remaining = self.amount - total
                        reminder = remaining % self.currency_combination[j]
                        currency_count = (remaining - reminder) / self.currency_combination[j]
                        total += currency_count * self.currency_combination[j]
                        self.result_list.append("Denomination of {} in  {} number".\
                            format(self.currency_combination[j],currency_count))
                    j += 1

    def display(self):
        """ Display the results """
        print('Denomination are:{}'.format(self.currency_combination))
        print("Entered amont of money is:{}".format(self.amount))
        print("Currency combinations are as follows")
        for result in self.result_list:
            print(result)


def main():
    """ main functionality to call the method"""
    denomination = [2000,500,100,50,20,10,5,2,1]
    try:
        rupee = int(input("Enter the ruppes: "))
        curr_combi_obj = CurrencyCombination(rupee, denomination)
        curr_combi_obj.calculate()
        curr_combi_obj.display()
    except  ValueError  as error:
        print(error)
        print("Entered number is not integer. Please try again")

if __name__ == "__main__":
    main()
