class LinkedList:

  def __init__(self, values=None):
    self.head = None
    if values:
      for item in reveresed(values):
        self.insert(item)

  def insert(self, value):
    self.head = Node(value, self.head)

  def append(self, value):
    node = Node(value)
    if not self.head:
      self.head = node
      return
    current = self.head
    while current.next:
      current.next = node

  def __iter__(self):
    def value_generator():
      current = self.head
      while current:
        yield current.value
        current = current.next
    return value_generator()

  def __len__(self):
    return len(list(iter(self)))

  def __str__(self):
    out = ""
    for value in self:
      out += f"{ {value} } ->"
    return out + "None"

  def __eq__(self, compare):
    return list(self == list(compare))

  def __getitem__(self, index):
    if index < 0:
      raise IndexError
    for i, value in enumerate(self):
      if i == index:
        return value
    raise IndexError

class Node:

  def __init__(self, value, next = None):
    self.value = value
    self.next = next