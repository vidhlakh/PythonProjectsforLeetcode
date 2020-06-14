import random
class RandomizedSet:
    
    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.set1 = set()
        

    # def insert(self, val: int) -> bool:
    #     """
    #     Inserts a value to the set. Returns true if the set did not already contain the specified element.
    #     """
    #     if val in self.set1:
    #         return False
    #     else:
    #         self.set1.add(val)
    #         return True

    # def remove(self, val: int) -> bool:
    #     """
    #     Removes a value from the set. Returns true if the set contained the specified element.
    #     """
    #     if val in self.set1:
    #         self.set1.remove(val)
    #         return True
    #     else:
    #         return False

    # def getRandom(self) -> int:
    #     """
    #     Get a random element from the set.
    #     """
    #     return random.sample(self.set1,1)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list1 = []
        self.dct1 = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dct1:
            return False
        
        self.dct1[val] =len(self.list1)
        self.list1.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dct1:
            last, indvalToDel = self.list1[-1],self.dct1[val]
            self.list1[indvalToDel],self.dct1[last] = last,indvalToDel
            self.list1.pop()
            del self.dct1[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list1)
# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.insert(2)
param_6 = obj.getRandom()
print("Inserted :",param_1)
print("Removed:",param_2)
print("Inserted :",param_3)
print("Random value",param_4)
print("Inserted :",param_5)
print("Random value",param_6)
