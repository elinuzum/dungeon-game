from base import Item

class SmallPotion(Item):
	"""docstring for SmallPotion"""
	def __init__(self, arg):
		super(SmallPotion, self).__init__()
		self.hp = 20
		self.receive_message = "received a small potion + 20 HP"
		self.drop_message = "item is gone"


class LargePotion(Item):
	"""docstring for LargePotion"""
	def __init__(self, arg):
		super(LargePotion, self).__init__()
		self.hp = 40
		self.receive_message = "received a large potion + 40 HP"
		self.drop_message = "item is gone"		


class DropofPotion(Item):
	"""docstring for DropofPotion"""
	def __init__(self, arg):
		super(DropofPotion, self).__init__()
		self.hp = 10
		self.receive_message = "received a drop of potion + 10 HP"
		self.drop_message = "item is gone"