n_list = ["happy", [2, 0 , 1, 5]]
print(n_list[1][3])


my_list = ['H', 'A', 'P', 'P', 'Y']
print(my_list[-3])

mult_list = [['B','A','R','K'], 
            ['L','E','A','F'], 
            ['G','R','A','S','S'], 
            ['D','I','R','T']]
print(mult_list[3][2])
x = sum(sublist.count('A') for sublist in mult_list)
print(x)
print(mult_list)

num_list = [1,3,5,7,9]
num_list.insert(1,2)
num_list.remove(3)
print(num_list.pop())
print(num_list)

# del num_list
