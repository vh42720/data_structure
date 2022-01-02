"""
Binary Search - Find Number of Rotation of a Rotated List

Input
---------
nums - A list of numbers obtained by rotating a sorted list - increasing order.

Output
---------
rotations: The number of time the sorted list is rotated.


Intuition
---------
Check middle value versus the last element of list => answer lies on left or right.

"""

import timeit


def evaluate_test_case(find_rotations_func, test_case, show_input=True):
	"""Evaluate and print results"""
	print('Test case:', test_case)

	if show_input:
		print('Input:', TEST_DEF[test_case]['input'])
	print('Expected Output:', expected_output := TEST_DEF[test_case]['output'])

	# find indexes
	start = timeit.default_timer()
	result = find_rotations_func(**TEST_DEF[test_case]['input'])
	stop = timeit.default_timer()

	print('Actual Output:', actual_output := result)
	print('Execution Time:', ("%.17f" % (stop - start)).rstrip('0').rstrip('.'))

	if expected_output == actual_output:
		print('Test Result: PASSED')
	else:
		print('Test Result: FAILED')

	print('=========================')


def find_rotations(nums):
	"""Binary Search Minimum Rotation"""
	low, high = 0, len(nums) - 1

	while low <= high:
		# find mid index
		mid = (low + high) // 2
		mid_num = nums[mid]

		if mid - 1 >= 0 and mid_num < nums[mid - 1]:
			return mid
		elif mid + 1 <= len(nums) - 1 and mid_num > nums[mid + 1]:
			return mid + 1
		elif mid_num <= nums[-1]:
			high = mid - 1
		else:
			low = mid + 1

	return 0


# define test cases
TEST_DEF = {
	# region general
	'general': {
		'input': {
			'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
		},
		'output': 3
	},
	# endregion
	# region rotated_once
	'rotated_once': {
		'input': {
			'nums': [29, 3, 5, 6, 7, 9, 11, 14, 19, 25]
		},
		'output': 1
	},
	# endregion
	# region no_rotation
	'no_rotation': {
		'input': {
			'nums': [3, 5, 6, 7, 9, 11, 14, 19, 25, 29]
		},
		'output': 0
	},
	# endregion
	# region rotated_n-1
	'rotated_n-1': {
		'input': {
			'nums': [5, 6, 7, 9, 11, 14, 19, 25, 29, 3]
		},
		'output': 9
	},
	# endregion
	# region empty_list
	'empty_list': {
		'input': {
			'nums': []
		},
		'output': 0
	},
	# endregion
	# region one_element
	'one_element': {
		'input': {
			'nums': [5]
		},
		'output': 0
	},
	# endregion
	# region repeated_numbers
	'repeated_numbers': {
		'input': {
			'nums': [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
		},
		'output': 6
	}
	# endregion
}


def main():
	# single test
	# evaluate_test_case(find_rotations, test_case='repeated_numbers')

	# all cases
	for test_case, test_dict in TEST_DEF.items():
		evaluate_test_case(find_rotations, test_case)


if __name__ == '__main__':
	main()
