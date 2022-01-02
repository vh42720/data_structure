"""
Lesson 1 - Binary Search

Input
---------
cards - A list of numbers sorted in decreasing order.
query - A number, whose position in the array is to be determined.

Output
---------
position: The position of query in the list cards

Restriction
---------
If multiple queries => return the first occurrence

Algorithm
---------
Linear Search Algorithm - Time complexity: O(N) and Space complexity: O(1)
Binary Search Algorithm - Time complexity: O(log N) and Space complexity: O(1)

"""

import timeit


def evaluate_test_case(locate_card_func, test_case, show_input=True):
	"""Evaluate and print results"""
	if show_input:
		print('Input:', TEST_DEF[test_case]['input'])
	print('Expected Output:', expected_output := TEST_DEF[test_case]['output'])

	start = timeit.default_timer()
	result = locate_card_func(**TEST_DEF[test_case]['input'])
	stop = timeit.default_timer()

	print('Actual Output:', actual_output := result)
	print('Execution Time:', ("%.17f" % (stop - start)).rstrip('0').rstrip('.'))

	if expected_output == actual_output:
		print('Test Result: PASSED')
	else:
		print('Test Result: FAILED')

	print('=========================')


def locate_card_linear(cards, query):
	"""Linear Search Algorithm"""
	position = 0

	while position < len(cards):
		if cards[position] == query:
			return position
		position += 1

	return -1


def locate_card_binary_search(cards, query):
	"""Binary Search Algorithm"""
	low, high = 0, len(cards) - 1

	while low <= high:
		# find mid index
		mid = (low + high) // 2
		mid_num = cards[mid]

		if mid_num == query:
			if mid - 1 >= 0 and cards[mid - 1] == query:
				high = mid - 1
			else:
				return mid
		elif mid_num < query:
			high = mid - 1
		elif mid_num > query:
			low = mid + 1

	return -1


# define test cases
TEST_DEF = {
	# region general
	'general': {
		'input': {
			'cards': [13, 11, 10, 7, 4, 3, 1, 0],
			'query': 7
		},
		'output': 3
	},
	# endregion
	# region query_is_first_element
	'query_is_first_element': {
		'input': {
			'cards': [4, 2, 1, -1],
			'query': 4
		},
		'output': 0
	},
	# endregion
	# region query_is_last_element
	'query_is_last_element': {
		'input': {
			'cards': [3, -1, -9, -127],
			'query': -127
		},
		'output': 3
	},
	# endregion
	# region contain_one_element_query
	'contain_one_element_query': {
		'input': {
			'cards': [6],
			'query': 6
		},
		'output': 0
	},
	# endregion
	# region does_not_contain_query
	'does_not_contain_query': {
		'input': {
			'cards': [9, 7, 5, 2, -9],
			'query': 4
		},
		'output': -1
	},
	# endregion
	# region cards_is_empty
	'cards_is_empty': {
		'input': {
			'cards': [],
			'query': 7
		},
		'output': -1
	},
	# endregion
	# region repeat_numbers_in_cards
	'repeat_numbers_in_cards': {
		'input': {
			'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
			'query': 3
		},
		'output': 7
	},
	# endregion
	# region query_occurs_multiple_times
	'query_occurs_multiple_times': {
		'input': {
			'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
			'query': 6
		},
		'output': 2
	},
	# endregion
	# region large_list
	'large_list': {
		'input': {
			'cards': list(range(10000000, 0, -1)),
			'query': 2
		},
		'output': 9999998
	},
	# endregion
}


def main():
	# single test
	# evaluate_test_case(locate_card_linear, test_case='general')

	# compare linear vs binary search
	evaluate_test_case(locate_card_linear, test_case='large_list', show_input=False)
	evaluate_test_case(locate_card_binary_search, test_case='large_list', show_input=False)

	# all cases
	# for test_case, test_dict in TEST_DEF.items():
	# 	evaluate_test_case(locate_card_binary_search, test_case)


if __name__ == '__main__':
	main()
