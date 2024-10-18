def print_params(a = 1, b = 'строка', c = True):
    print(a)
    print(b)
    print(c)
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['False', True, 1]
values_dict = {'a' : False , 'b' : 17, 'c' : 'apple' }
print_params(* values_list)
print_params(** values_dict)

values_list_2 = [100, 'Python']
print_params(*values_list_2, 42)





