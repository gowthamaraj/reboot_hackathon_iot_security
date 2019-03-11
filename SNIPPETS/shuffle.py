import random

fid = open("data_set.txt", "r")
li = fid.readlines()
fid.close()
print(li)

random.shuffle(li)
print(li)

fid = open("shuffled_data_set.txt", "w")
fid.writelines(li)
fid.close()