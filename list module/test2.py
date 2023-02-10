#My module
class test:
    list = []
    def add(self,TEXT):
        # def add він добавляє предмети в list
        self.list.append(TEXT)
    
    def delf(self,TEXT):
        # def add він видаляє предмети в list
        self.list.remove(TEXT)
    
    def show(self):
        print(f"LIST: {self.list}")

#Test My module
test2 = test()
test2.add(TEXT="HELLO")
test2.show()
test2.delf(TEXT="HELLO")
test2.show()