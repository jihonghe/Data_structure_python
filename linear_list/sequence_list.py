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

class SeqList(object):
	"""一体式结构：顺序表的表信息（容量，当前长度）与元素的存储区是相邻的，即划分一块内存用于存储表信息及表数据
	"""
	def __init__(self, length = 0, capacity=10):
		"""
		创建一体式结构顺序表
		:param length: 当前元素个数
		:param capacity: 顺序表容量
		"""
		self.capacity = capacity
		self.length = length
		self.data = [None] * capacity

# 表元素的查找与访问：travel(), get(index), search(element), search_start(element, start)

	def travel(self):
		"""
		遍历表元素
		:return: None
		"""
		for e in self.data:
			print(e, end=', ')

	def get(self, index):
		"""
		根据给出的索引index返回顺序表中对应的元素，如果index不是整型或者不合法则抛出对应的异常
		:param index: 元素索引
		:return: index正确则返回对应的元素，否则抛出异常
		"""
		if not isinstance(index, int):
			print("Parameter index must be int")
		elif self._is_legal_index_(index):
			return self.data[index]
		else:
			print("Error: %d out of range" % index)

	def search(self, element):
		"""
		查找给出的元素在顺序表中第一次出现的位置，返回对应的索引值
		:param element: 给出的元素
		:return: 如果元素在表中，则返回元素在顺序表中的索引值，否则返回 -1
		"""
		first = 0

		while first < self.length:
			if self.data[first] == element:
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
			while first < self.length:
				if self.data[first] == element:
					return first
				first += 1
			return -1
		else:
			print("Error: %d out of range" % start)

	"""
	表元素的变动操作：
		增：append(element), insert(element, index)
		删：del_first(), del_last(), del_by_index(index), del_by_element(element)
	"""
	def append(self, element):
		"""
		在顺序表尾部插入元素
		:param element: 插入的目标元素
		:return: None
		"""
		if not self.is_full():
			self.data[self.length] = element
			self.length += 1
		else:
			print("The sequence is already full")

	def insert(self, element, index):
		"""
		在顺序表指定位置插入元素
		:param element: 插入的目标元素
		:param index: 插入的位置
		:return: None
		"""
		if self._is_legal_index_(index) and not self.is_full():
			self._move_(op_index=index, op_type="insert")
			self.data[index] = element
			self.length += 1
		else:
			print("Error: index out of range")

	def del_first(self):
		"""
		删除顺序表第一个元素
		:return: 成功则返回 True，失败则返回 False
		"""
		if not self.is_empty():
			self._move_(op_index=0, op_type="delete")
			self.length -= 1
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
			self.data[self.length - 1] = None
			self.length -= 1
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
			if self.is_empty():
				self._move_(op_index=index, op_type="delete")
				self.length -= 1
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
			self.length -= 1
			return True
		else:
			print("Error: element not found")
			return False

# 表信息的获取与判断：len(), is_empty(), is_full()是获取表信息及简单判断的相关操作
	def len(self):
		"""
		返回顺序表长度
		:return: 顺序表长度
		"""
		return self.length

	def is_empty(self):
		"""
		判断表是否为空
		:return: 空 -> True，不为空 -> False
		"""
		return self.length == 0

	def is_full(self):
		"""
		判断表是否已满
		:return: 满 -> True，不满 -> False
		"""
		return self.length == self.capacity

	def _move_(self, op_index, op_type):
		if self._is_legal_index_(op_index):
			if op_type == "insert":
				# 此处用len()函数的原因：防止因为length的在调用_move_()方法之前发生改变带来的错误
				tail_i = len(self.data) - 1
				while tail_i >= op_index:
					self.data[tail_i + 1] = self.data[tail_i]
					tail_i -= 1
			elif op_type == "delete":
				start, end = op_index + 1, len(self.data) - 1
				while start <= end:
					self.data[start - 1] = self.data[start]
					start -= 1
				self.data[end] = None
		else:
			print("Error: index out of range")

	def _is_legal_index_(self, index):
		return 0 <= index < self.length