"""""
my_list = [100, 200, 300, 199, 99, 9]
a_list = [101, 202, 303]

my_list.extend(a_list)

def sum_list(k_list):
    sum = 0
    for item in k_list:
        sum = sum + item
    print(sum)
    
sum_list(my_list)

for item in my_list:
    print(item)
"""""

my_dict = {"a": 10, "b": 20, "c": 30}

def count_dict(k_dict):
    count=0
    for key in k_dict:
        count = count + k_dict[key]
    print(count)

count_dict(my_dict)
