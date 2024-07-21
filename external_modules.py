# external Modules

# There are many modules you can import 

# To use modules you have to install the via pip in the powershell/terminal

import matplotlib.pyplot as plt

# data

x = [i for i in range(0,11)]
y = [y ** 2 for y in x]
print(x,y)

plt.plot(x,y)
plt.show() # shows graph