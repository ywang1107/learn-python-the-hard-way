# test the randomness to be rich

# initialize to be equal rich
# there are 100 people each with 100 bucks
people = [100 for i in range(100)]

import random 
# for every year, each one will give 1 to random pick people
# continues for 100000 years, when people with 0 stop giving
for i in range(100000):
    for idx,human in enumerate(people):
        if human > 0:
            people[random.randint(0,99)] += 1
            people[idx] -= 1

people = sorted(people)

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 

y_pos = np.arange(len(people))
 
plt.bar(y_pos, people, align='center', alpha=0.5)
# plt.xticks(y_pos,[i for i in range(1,101)] )
plt.ylabel('Wealth')
 
plt.show()