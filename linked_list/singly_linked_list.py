"""
Singly Linked List - Implementation
"""


class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node


class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		node = Node(data, self.head)
		self.head = node

	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None)
			return

		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next = Node(data, None)

	def insert_values(self, data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)

	def get_element(self, index):
		if index < 0 or index >= self.get_length():
			raise IndexError('Invalid Index')

		if self.head is None:
			return

		count = 0
		itr = self.head

		while itr:
			if count == index:
				return itr.data

			count += 1
			itr = itr.next

	def get_length(self):
		count = 0
		itr = self.head
		while itr:
			count += 1
			itr = itr.next

		return count

	def remove_at(self, index):
		if index < 0 or index >= self.get_length():
			raise IndexError('Invalid Index')

		if index == 0:
			self.head = self.head.next
			return

		count = 0
		itr = self.head
		while itr:
			if count == index - 1:
				itr.next = itr.next.next
				break

			count += 1
			itr = itr.next

	def remove_by_value(self, data):
		if self.head is None:
			return

		itr = self.head

		if self.head.data == data:
			self.head = itr.next
			return

		while itr.next:
			if itr.next.data == data:
				itr.next = itr.next.next
				break
			itr = itr.next

	def reverse(self):
		if self.head is None:
			return

		itr = self.head
		prev = None

		while itr:
			next_node = itr.next
			itr.next = prev
			prev = itr
			itr = next_node
		self.head = prev

	def insert_at(self, index, data):
		if index < 0 or index > self.get_length():
			raise IndexError('Invalid Index')

		if index == 0:
			self.insert_at_beginning(data)
			return

		count = 0
		itr = self.head
		while itr:
			if count == index - 1:
				itr.next = Node(data, itr.next)
				break

			itr = itr.next
			count += 1

	def insert_after_value(self, data_after, data_to_insert):
		if self.head is None:
			return

		if self.head.data == data_after:
			self.head.next = Node(data_to_insert, self.head.next)
			return

		itr = self.head
		while itr:
			if itr.data == data_after:
				itr.next = Node(data_to_insert, itr.next)
				break
			itr = itr.next

	def print(self):
		if self.head is None:
			print('Linked list is empty')
			return

		itr = self.head
		ll_str = ''

		while itr:
			ll_str += str(itr.data) + ' -> '
			itr = itr.next

		print(ll_str)


def main():
	ll = LinkedList()
	ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
	ll.print()
	ll.remove_by_value('orange')
	ll.remove_by_value('figs')
	ll.print()
	ll.insert_after_value('banana', 'orange')
	ll.print()
	print(ll.get_element(3))
	ll.reverse()
	ll.print()


if __name__ == '__main__':
	main()
