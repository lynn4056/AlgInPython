__author__ = 'Lynn'

i = 0
while i < 3:
    i += 1
    print("This is the {0}th loop" .format(i))

data = (1, 8, 9, 4, 5)
biggest = data[0]
print (biggest)
for val in data:
    if val > biggest:
        biggest = val
    print("The current biggest value is {0}".format(biggest))

