string = input()
alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alpha in alpha_list:
    string = string.replace(alpha, '*')
print(len(string))