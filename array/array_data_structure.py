"""
Array Data Structure

---------
https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
"""

expense_dict = {
	'January': 2200,
	'February': 2350,
	'March': 2600,
	'April': 2130,
	'May': 2190
}

expense_list = [i for i in expense_dict.values()]


def question_1():
	# 1. In Feb, how many dollars you spent extra compare to January?
	print(f'Fed spending extra ${expense_list[1] - expense_list[0]} compared to Jan')

	# 2. Find out your total expense in first quarter (first three months) of the year.
	print(f'First quarter spending: ${sum(expense_list[:2])}')

	# 3. Find out if you spent exactly 2000 dollars in any month
	print(f'Month that you spent exactly 2000: {[i + 1 for i, v in enumerate(expense_list) if v == 2000]}')

	# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
	expense_dict['June'] = 1980
	expense_list.append(1980)
	print(f'Expense at the end of June: ${expense_list[-1]}')

	# 5. You returned an item that you bought in a month of April and got a refund of 200$.
	# Make a correction to your monthly expense list based on this
	expense_list[3] -= 200
	print(f'Expenses after $200 return in April: ${expense_list[3]}')


def question_2():
	heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

	# 1. Length of the list
	print(f'Length of the list is: {len(heroes)}')

	# 2. Add 'black panther' at the end of this list
	heroes.append('black panther')
	print(f'Heroes list after insert black panther: {heroes}')

	# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
	heroes.pop()
	heroes.insert(heroes.index('hulk') + 1, 'black panther')
	print(f'Heroes list after insert black panther after hulk: {heroes}')

	# 4. Now you don't like thor and hulk because they get angry easily. So you want to remove thor and hulk
	# from list and replace them with doctor strange (because he is cool). Do that with one line of code.
	heroes[heroes.index('thor'):heroes.index('hulk') + 1] = ['doctor strange']
	print(f'Heroes list after insert doctor strange: {heroes}')

	# 5. Sort the heroes list in alphabetical order(Hint.Use dir() functions to list down all functions available in list)
	heroes.sort()
	print(f'Heroes list after sorting: {heroes}')


def main():
	print(f'Question 1\n')
	question_1()
	print('\n-------------------------\n')
	print(f'Question 2\n')
	question_2()


if __name__ == '__main__':
	main()
