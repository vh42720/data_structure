"""
Lesson 1 - Binary Search - Find Range of Index for a Target

Input
---------
nums - A list of numbers sorted in ascending order.
target - A number, whose starting and ending position in the array is to be determined.

Output
---------
start_idx: The starting position of target in nums array
end_idx: The ending position of target in nums array

"""

import timeit


def evaluate_test_case(locate_start_idx_func, locate_end_idx_func, test_case, show_input=True):
	"""Evaluate and print results"""
	print('Test case:', test_case)

	if show_input:
		print('Input:', TEST_DEF[test_case]['input'])
	print('Expected Output:', expected_output := TEST_DEF[test_case]['output'])

	# find indexes
	start = timeit.default_timer()
	start_idx = locate_start_idx_func(**TEST_DEF[test_case]['input'])
	end_idx = locate_end_idx_func(**TEST_DEF[test_case]['input'])
	stop = timeit.default_timer()
	result = {'start_idx': start_idx, 'end_idx': end_idx}

	print('Actual Output:', actual_output := result)
	print('Execution Time:', ("%.17f" % (stop - start)).rstrip('0').rstrip('.'))

	if expected_output == actual_output:
		print('Test Result: PASSED')
	else:
		print('Test Result: FAILED')

	print('=========================')


def locate_start_idx(nums, target):
	"""Binary Search Starting Index"""
	low, high = 0, len(nums) - 1

	while low <= high:
		# find mid index
		mid = (low + high) // 2
		mid_num = nums[mid]

		if mid_num == target:
			if mid - 1 >= 0 and nums[mid - 1] == target:
				high = mid - 1
			else:
				return mid
		elif mid_num > target:
			high = mid - 1
		elif mid_num < target:
			low = mid + 1

	return -1


def locate_end_idx(nums, target):
	"""Binary Search Starting Index"""
	low, high = 0, len(nums) - 1

	while low <= high:
		# find mid index
		mid = (low + high) // 2
		mid_num = nums[mid]

		if mid_num == target:
			if mid + 1 <= len(nums) - 1 and nums[mid + 1] == target:
				low = mid + 1
			else:
				return mid
		elif mid_num > target:
			high = mid - 1
		elif mid_num < target:
			low = mid + 1

	return -1




# define test cases
TEST_DEF = {
	# region general
	'general': {
		'input': {
			'nums': [0, 1, 3, 7, 7, 10, 11, 13],
			'target': 7
		},
		'output': {
			'start_idx': 3,
			'end_idx': 4
		}
	},
	# endregion
	# region query_is_first_element
	'query_is_first_element': {
		'input': {
			'nums': [-1, 1, 2, 4],
			'target': 4
		},
		'output': {
			'start_idx': 3,
			'end_idx': 3
		}
	},
	# endregion
	# region query_is_last_element
	'query_is_last_element': {
		'input': {
			'nums': [-127, -127, -9, -1, 3],
			'target': -127
		},
		'output': {
			'start_idx': 0,
			'end_idx': 1
		}
	},
	# endregion
	# region contain_one_element_query
	'contain_one_element_query': {
		'input': {
			'nums': [6],
			'target': 6
		},
		'output': {
			'start_idx': 0,
			'end_idx': 0
		}
	},
	# endregion
	# region does_not_contain_query
	'does_not_contain_query': {
		'input': {
			'nums': [-9, 2, 5, 7, 9],
			'target': 4
		},
		'output': {
			'start_idx': -1,
			'end_idx': -1
		}
	},
	# endregion
	# region cards_is_empty
	'cards_is_empty': {
		'input': {
			'nums': [],
			'target': 7
		},
		'output': {
			'start_idx': -1,
			'end_idx': -1
		}
	},
	# endregion
	# region repeat_numbers_in_nums
	'repeat_numbers_in_cards': {
		'input': {
			'nums': [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 8, 8],
			'target': 6
		},
		'output': {
			'start_idx': 7,
			'end_idx': 11
		}
	},
	# endregion
	# region large_list
	'large_list': {
		'input': {
			'nums': list(range(0, 10000001, 1)) + ([10000001]*20) + [10000002, 10000003, 10000004, 10000005],
			'target': 10000001
		},
		'output': {
			'start_idx': 10000001,
			'end_idx': 10000020
		}
	},
	# endregion
}


def main():
	# single test
	# evaluate_test_case(locate_start_idx, locate_end_idx, test_case='large_list', show_input=False)
	# evaluate_test_case(locate_start_idx, locate_end_idx, test_case='general')

	# all cases
	for test_case, test_dict in TEST_DEF.items():
		evaluate_test_case(locate_start_idx, locate_end_idx, test_case, show_input=False)


if __name__ == '__main__':
	main()
