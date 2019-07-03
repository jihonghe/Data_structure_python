# -*- coding: utf-8 -*-
"""
------------------------------------------------
File Name   :   sequence_list.py
Author      :   jihonghe
GitHub      :   github.com/jihonghe
Contact     :   jihonghe_hjh@163.com
Create Time :   2019/7/3 上午12:55
Description :
------------------------------------------------
"""

class SeqList:
	"""
	分离式顺序表：表元素并不保存在顺序表实例的内存中，而是仅仅记录一个索引值
	"""
	def __init__(self, capacity=10):
		"""
		创建一体式结构顺序表
		:param capacity: 顺序表容量
		"""
		self._capacity = capacity
		self._length = 0
		self._data = [None] * capacity

# 表元素的查找与访问：travel(), get(index), search(element), search_start(element, start)

	def travel(self):
		"""
		遍历表元素
		:return: None
		"""
		for e in self._data:
			print(e, end=', ')
		print()

	def get(self, index):
		"""
		根据给出的索引index返回顺序表中对应的元素，如果index不是整型或者不合法则抛出对应的异常
		:param index: 元素索引
		:return: index正确则返回对应的元素，否则抛出异常
		"""
		if not isinstance(index, int):
			raise TypeError
		elif self._is_legal_index_(index):
			return self._data[index]
		else:
			raise IndexError

	def search(self, element):
		"""
		查找给出的元素在顺序表中第一次出现的位置，返回对应的索引值
		:param element: 给出的元素
		:return: 如果元素在表中，则返回元素在顺序表中的索引值，否则返回 -1
		"""
		first = 0

		while first < self._length:
			if self._data[first] == element:
				return first
			first += 1

		return -1

	def search_start(self, element, start):
		"""
		从顺序表的指定位置之后查找元素出现的位置
		:param element: 查找元素
		:param start: 从 0 开始
		:return: 若start不合法，则抛出异常；否则查找目标元素位置，找到了则返回对应的索引值，没找到则返回-1
		"""
		if self._is_legal_index_(start):
			first = start + 1
			while first < self._length:
				if self._data[first] == element:
					return first
				first += 1
			return -1
		else:
			raise IndexError

	"""
	表元素的变动操作：
		增：append(element), insert(element, index)
		删：del_first(), del_last(), del_by_index(index), del_by_element(element), clear()
		改：set(element, index)
	"""
	def append(self, element):
		"""
		在顺序表尾部插入元素
		:param element: 插入的目标元素
		:return: None
		"""
		if not self.is_full():
			self._data[self._length] = element
			self._length += 1
		else:
			raise Exception

	def insert(self, element, index):
		"""
		在顺序表指定位置插入元素
		:param element: 插入的目标元素
		:param index: 插入的位置
		:return: None
		"""
		if self._is_legal_index_(index) and not self.is_full():
			self._move_(op_index=index, op_type="insert")
			self._data[index] = element
			self._length += 1
		else:
			raise IndexError

	def del_first(self):
		"""
		删除顺序表第一个元素
		:return: 成功则返回 True，失败则返回 False
		"""
		if not self.is_empty():
			self._move_(op_index=0, op_type="delete")
			self._length -= 1
			return True
		else:
			print("Error: list is empty")
			return False

	def del_last(self):
		"""
		删除顺序表的最后一个元素
		:return: 成功则返回 True，失败则返回 False
		"""
		if not self.is_empty():
			self._data[self._length - 1] = None
			self._length -= 1
			return True
		else:
			print("Error: list is empty")
			return False

	def del_by_index(self, index):
		"""
		通过索引删除元素
		:param index: 待删除元素的索引
		:return: 删除成功则返回 True，失败则返回 False
		"""
		if self._is_legal_index_(index):
			if not self.is_empty():
				self._move_(op_index=index, op_type="delete")
				self._length -= 1
				return True
			else:
				print("Error: list is empty")
				return False
		else:
			print("Error: illegal index")
			return False

	def del_by_element(self, element):
		"""
		通过给出的元素删除在表中出现的第一个位置的元素
		:param element: 待删除的目标元素
		:return: 删除成功返回 True，失败返回 False
		"""
		e_index = self.search(element)
		if e_index != -1:
			self._move_(op_index=e_index, op_type="delete")
			self._length -= 1
			return True
		else:
			print("Error: element not found")
			return False

	def clear(self):
		"""
		清空列表元素
		:return: None
		"""
		for j in range(self._length):
			self._data[j] = None
		self._length = 0

	def set(self, element, index):
		"""
		根据给出的索引修改指定元素，若索引错误则抛出异常
		:param element:
		:param index:
		:return: None
		"""
		if self._is_legal_index_(index):
			self._data[index] = element
		else:
			raise IndexError

# 表信息的获取与判断：len(), is_empty(), is_full()是获取表信息及简单判断的相关操作
	def len(self):
		"""
		返回顺序表长度
		:return: 顺序表长度
		"""
		return self._length

	def is_empty(self):
		"""
		判断表是否为空
		:return: 空 -> True，不为空 -> False
		"""
		return self._length == 0

	def is_full(self):
		"""
		判断表是否已满
		:return: 满 -> True，不满 -> False
		"""
		return self._length == self._capacity

	def _move_(self, op_index, op_type):
		if self._is_legal_index_(op_index):
			if op_type == "insert":
				tail_i = self._length
				while tail_i >= op_index:
					self._data[tail_i + 1] = self._data[tail_i]
					tail_i -= 1
			elif op_type == "delete":
				start, end = op_index + 1, self._length
				while start <= end:
					self._data[start - 1] = self._data[start]
					start += 1
				self._data[end] = None
		else:
			print("Error: index out of range")

	def _is_legal_index_(self, index):
		return 0 <= index < self._length


if __name__ == '__main__':
	# 初始化顺序表
	seq_list = SeqList(capacity=12)
	print("is_empty():", seq_list.is_empty())
	print("is_full():", seq_list.is_full())
	#assert seq_list.is_empty() == True
	#assert seq_list.is_full() == False
	# 添加元素
	for i in range(10):
		seq_list.append(i)
	print("len():", seq_list.len())
	#assert seq_list.len() == 10
	# 遍历和访问表元素
	seq_list.travel()
	print("get(index):", seq_list.get(2))
	print("search(index):", seq_list.search(6))
	print("search_start(element, start):", seq_list.search_start(9, 3))
	#assert seq_list.get(0) == 0
	#assert seq_list.search(10) == -1
	#assert seq_list.search_start(3, 1) != -1
	# 表元素变动操作
	print("length before insert:", seq_list.len())
	seq_list.insert(3, 8)
	print("length after insert:", seq_list.len())
	seq_list.del_first()
	print("length after delete:", seq_list.len())
	seq_list.travel()
	seq_list.del_last()
	seq_list.travel()
	seq_list.del_by_index(3)
	seq_list.travel()
	seq_list.del_by_element(7)
	#assert seq_list.len() == 11
	#assert seq_list.del_first() == True
	#assert seq_list.del_last() == True
	#assert seq_list.del_by_index(3) == True
	#assert seq_list.del_by_element(3) == True
	#assert seq_list.del_by_element(19) == False
	seq_list.clear()
	print("sequence is empty after clear():", seq_list.is_empty())
	#assert seq_list.len() == 0
