import support
from support import Exam
# you can also import everything like 'from support import *'

test1 = support.Test()
exam1 = Exam()

print(test1.a) # output : 123
test1.some_method() # output is 'some method printed'

print(support.sumOfNumbers(2,4)) # 6
 
print(support.var) # something


exam1.some_method() # exam method printed
print(exam1.b) # 44

