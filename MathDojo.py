# # PART 1
# class MathDojo(object):
#     def __init__(self):
#         self.result = 0

#     def add(self, *val):
#         for i in val:
#             if type(i)==tuple:
#                 for j in i:
#                     self.result += j
#             else:
#                 self.result += i
#         return self

#     def subtract(self, *val):
#         for i in val:
#             if type(i)==tuple:
#                 for j in i:
#                     self.result -= j
#             else:
#                 self.result -= i
#         return self
# md = MathDojo()
# print md.add(2).add(2,5).subtract(3,2).result

# PART 2
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *val):
        for i in val:
            if type(i)==tuple or type(i)==list:
                for j in i:
                    self.result += j
            else:
                self.result += i
        return self

    def subtract(self, *val):
        for i in val:
            if type(i)==tuple or type(i)==list:
                for j in i:
                    self.result -= j
            else:
                self.result -= i
        return self
md = MathDojo()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result





