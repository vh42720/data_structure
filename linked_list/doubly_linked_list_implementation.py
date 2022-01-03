"""
Doubly Linked List - Implementation
"""


class Node:
	def __init__(self, data=None, next_node=None, prev_node=None):
		self.data = data
		self.next = next_node
		self.prev = prev_node


class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		if self.head is None:
			self.head = Node(data, self.head, None)
		else:
			node = Node(data, self.head, None)
			self.head.prev = node
			self.head = node

	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, self.head, None)
			return

		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next = Node(data, None, itr)

	def insert_values(self, data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)

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
				node = Node(data, itr.next, itr)
				if itr.next:
					itr.next.prev = node
				itr.next = node
				break

			itr = itr.next
			count += 1

	def insert_after_value(self, data_after, data_to_insert):
		if self.head is None:
			return

		if self.head.data == data_after:
			node = Node(data_to_insert, self.head.next, self.head)
			if self.head.next:
				self.head.next.prev = node
			self.head.next = node
			return

		itr = self.head
		while itr:
			if itr.data == data_after:
				node = Node(data_to_insert, itr.next, itr)
				if itr.next:
					itr.next.prev = node
				itr.next = node
				break

			itr = itr.next

	def get_length(self):
		count = 0
		itr = self.head
		while itr:
			count += 1
			itr = itr.next

		return count

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

	def get_last_node(self):
		itr = self.head
		while itr.next:
			itr = itr.next

		return itr

	def remove_at(self, index):
		if index < 0 or index >= self.get_length():
			raise IndexError('Invalid Index')

		if index == 0:
			self.head = self.head.next
			self.head.prev = None
			return

		count = 0
		itr = self.head
		while itr:
			if count == index:
				itr.prev.next = itr.next
				if itr.next:
					itr.next.prev = itr.prev
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

	def print_forward(self):
		if self.head is None:
			print('Linked list is empty')
			return

		itr = self.head
		ll_str = ''

		while itr:
			ll_str += str(itr.data) + ' -> '
			itr = itr.next

		print(ll_str)

	def print_backward(self):
		if self.head is None:
			print('Linked list is empty')
			return

		itr = self.get_last_node()
		ll_str = ''

		while itr:
			ll_str += str(itr.data) + ' -> '
			itr = itr.prev

		print('Linked list in reverse:', ll_str)


def main():
	ll = DoublyLinkedList()
	ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
	ll.print_forward()
	ll.print_backward()
	ll.insert_at_end('figs')
	ll.print_forward()
	ll.insert_at(0, 'jackfruit')
	ll.print_forward()
	ll.insert_at(6, 'dates')
	ll.print_forward()
	ll.insert_at(2, 'kiwi')
	ll.print_forward()
	ll.insert_after_value('kiwi', 'peach')
	ll.print_forward()
	ll.remove_by_value('peach')
	ll.print_forward()


if __name__ == '__main__':
	main()
