"""
Binary Search - Find Index of Target from Rotated List

Input
---------
nums - A list of numbers obtained by rotating a sorted list - increasing order.
target - A number, whose position in the array is to be determined.

Output
---------
position: The position of query in the list cards.

Restriction
---------
If multiple queries => return the first occurrence.

"""

import timeit


def evaluate_test_case(find_position_func, test_case, show_input=True):
	"""Evaluate and print results"""
	print('Test case:', test_case)

	if show_input:
		print('Input:', TEST_DEF[test_case]['input'])
	print('Expected Output:', expected_output := TEST_DEF[test_case]['output'])

	# find indexes
	start = timeit.default_timer()
	result = find_position_func(**TEST_DEF[test_case]['input'])
	stop = timeit.default_timer()

	print('Actual Output:', actual_output := result)
	print('Execution Time:', ("%.17f" % (stop - start)).rstrip('0').rstrip('.'))

	if expected_output == actual_output:
		print('Test Result: PASSED')
	else:
		print('Test Result: FAILED')

	print('=========================')


def find_position(nums, target):
	"""Binary Search Target in Rotated Sorted List"""
	low, high = 0, len(nums) - 1

	while low <= high:
		# find mid index
		mid = (low + high) // 2
		mid_num = nums[mid]
		last_num = nums[-1]

		if mid_num == target:
			return mid
		elif target < mid_num <= last_num:
			high = mid - 1
		elif mid_num < target < last_num:
			low = mid + 1
		elif mid_num <= last_num < target:
			high = mid - 1
		elif last_num <= mid_num < target:
			low = mid + 1
		elif last_num < target < mid_num:
			high = mid - 1
		elif target < last_num <= mid_num:
			low = mid + 1

	return -1


# define test cases
TEST_DEF = {
	# region general
	'general': {
		'input': {
			'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14],
			'target': 7
		},
		'output': 6
	},
	# endregion
	# region rotated_once
	'rotated_once': {
		'input': {
			'nums': [29, 3, 5, 6, 7, 9, 11, 14, 19, 25],
			'target': 11
		},
		'output': 6
	},
	# endregion
	# region no_rotation
	'no_rotation': {
		'input': {
			'nums': [3, 5, 6, 7, 9, 11, 14, 19, 25, 29],
			'target': 25
		},
		'output': 8
	},
	# endregion
	# region rotated_n-1
	'rotated_n-1': {
		'input': {
			'nums': [5, 6, 7, 9, 11, 14, 19, 25, 29, 3],
			'target': 7
		},
		'output': 2
	},
	# endregion
	# region empty_list
	'empty_list': {
		'input': {
			'nums': [],
			'target': 2
		},
		'output': -1
	},
	# endregion
	# region one_element
	'one_element': {
		'input': {
			'nums': [5],
			'target': 5
		},
		'output': 0
	},
	# endregion
	# region no_element
	'no_element': {
		'input': {
			'nums': [5, 6, 7, 9, 11, 14, 19, 25, 29, 3],
			'target': 2
		},
		'output': -1
	},
	# endregion
}


def main():
	# single test
	# evaluate_test_case(find_position, test_case='no_element')

	# all cases
	for test_case, test_dict in TEST_DEF.items():
		evaluate_test_case(find_position, test_case)


if __name__ == '__main__':
	main()
