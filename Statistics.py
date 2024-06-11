import statistics
scores = [6,7,2,6,3,5,5,5,2,5,6,1,2]
a = statistics.mean(scores)
print(a)
b = statistics.median(scores)
print(b)
c = statistics.mode(scores)
print(c)
# Compute the Low median
list_1= [20,40,60,80,100]
list_2 = [30,70,90]
print("Low median of list_1 is: ",statistics.median_low(list_1))
print("Low median of list_2 is: ",statistics.median_low(list_2))
# High Median
list_1= [15,30,45,60]
list_2 = [20,40]
print("High median of list_1 is: ",statistics.median_high(list_1))
print("High median of list_2 is: ",statistics.median_high(list_2))
# Variance
grades = [70, 90, 50, 85, 65, 83, 94]
grades_mean = statistics.mean(grades)
print("variance of data is: ",statistics.variance(grades,grades_mean))
# Standard Deviation
grades = [89, 91, 95, 92, 93, 94, 98, 90]
stdevgrades = statistics.stdev(grades)
print("The Standard deviation of the list is: ", stdevgrades)