

import tkinter as tk
from tkinter import ttk


SCREEN = "push_swap visualizer"
GEOMETRY = "900x850"

class TestNum:
	def __init__(self, nums:list):
		self.nums = nums
		self.initid_nums = list()
	def init_pos(self):
		for num in self.nums:
			pos = 0
			for j in self.nums:
				if num > j:
					pos += 1
			self.initid_nums.append(pos)
		return self.initid_nums
	def diplay(self):
		for i in range(len(self.nums)):
			print(f"number: {self.nums[i]}, pos: {self.initid_nums[i]}")

arr = [2, 4, 0, -1, 45, 1]
nums = TestNum(arr)
nums.init_pos()
nums.diplay()


class PsVis(tk.Tk):

	def __init__(self, nums):
		super().__init__()
		self.nums = TestNum(nums)
		self.nums.init_pos()
		self.title(SCREEN)
		self.geometry(GEOMETRY)
		self.configure(bg='black')
		self.style = ttk.Style()
		label = tk.Label(width=10, height=1, bg='red')
		label.pack(padx=10, side=tk.TOP, anchor='sw')

window =PsVis(arr)
window.mainloop()

		
		
