import numpy as np
import matplotlib.pyplot as plt
import math   

apple_width  = np.random.randint(3, 7, 50)
apple_height = np.random.randint(4, 8, 50)

banana_width  = np.random.randint(2, 5, 50)
banana_height = np.random.randint(10, 16, 50)

x_train = []
for i in range(50):
    x_train.append([apple_width[i], apple_height[i]])
for i in range(50):
    x_train.append([banana_width[i], banana_height[i]])

y_train = []
for i in range(50):
    y_train.append(0)
for i in range(50):
    y_train.append(1)

new_fruit = [4, 9]   

distances = []

for fruit in x_train:
    dw = fruit[0] - new_fruit[0]   
    dh = fruit[1] - new_fruit[1]  
    d = math.sqrt(dw**2 + dh**2)   
    distances.append(d)


print("Distancce: ", len(distances))      
print("Distance apple: ", distances[:5])
print("Distance banana", distances[-5:])
print("Min distance: ", min(distances))
print("Max distance: ", max(distances))

for i in range(50):
    plt.scatter(apple_width[i], apple_height[i], color='red')

for i in range(50):
    plt.scatter(banana_width[i], banana_height[i], color='gold')


plt.scatter(new_fruit[0], new_fruit[1], color='blue', marker='o', s=100)

plt.xlabel('Width')
plt.ylabel('Height')
plt.title('Apple vs Banana + New Fruit')
plt.show()
