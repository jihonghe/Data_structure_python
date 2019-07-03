# -*- coding: utf-8 -*-
"""
------------------------------------------------
File Name   :   link_list.py
Author      :   jihonghe
GitHub      :   github.com/jihonghe
Contact     :   jihonghe_hjh@163.com
Create Time :   2019/7/3 上午11:11
Description :   
------------------------------------------------
"""


class SllNode:
	"""
	单链表节点（Single linked list node）：
	"""

	def __init__(self, elem=None):
		self._elem = elem
		self._next = None


class SLinkedList:
	"""
	单链表：
	"""

	def __init__(self):
		"""
		初始化空链表，设置链表信息：设置长度和头结点
		设置长度：在获取链表长度或其他涉及链表长度的操作时，可以不用遍历链表，以空间换时间
		"""
		self._length = 0
		self._head = None
