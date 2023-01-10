import random  # randint is inclusive
import matplotlib.pyplot as plt
import math




lower_bound = 0
upper_bound = 4
degree = 1




def pdf(x):
    mean = 2
    standard_deviation = 1

    exponent = -(x-mean)**2/(2*(standard_deviation**2))



    return 1/((1*math.pi)**(1/2))*(math.e)**(exponent)

y_vals =[]
x_vals =[]

for i in range(10):
    y_vals.append(pdf(i))
    x_vals.append(i)

print(y_vals)



# # add labels
# plt.xlabel("Day")
# plt.ylabel("Number of people")


# # give each scatter a name for the legend
sick=plt.scatter(x_vals, y_vals, color='k', s=5)
# immune=plt.scatter(x_values, data[1], color='g', s=3)
# # append legend
# plt.legend((sick, immune),("Sick people", "Immune people"))

# plt.title("Cases vs immunity overtime")
# # plot
# plt.plot(x_values,data[0], color='k')
# plt.plot(x_values, data[1], color='g')
# plt.show()


weights = []
indexes = [0]
index = 0

for i in range(lower_bound, upper_bound):

    val = int(pdf(i)*1000)
    weights.append(val)
    index+=val
    indexes.append(index)
    



# indexes=[]


print(weights)
print(indexes)


def get_index():
    bucket = 0
    choice = random.randint(0, index)





    for i in range (len(indexes)):
        if choice < indexes[i]:
            return i


nums = []
for i in range(1000):
    nums.append(get_index())

results = [0, 0, 0, 0, 0, 0]

for n in nums:
    results[n]+=1

print(results)