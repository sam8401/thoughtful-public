from sort_fun import sort



print('Running tests against sort_fun.py')


# test normal package ('STANDARD')

label = sort(10, 10, 10, 10)

assert label == 'STANDARD' 

label = sort(149.9999, 10, 10, 19.9999)

assert label == 'STANDARD' 

label = sort(100, 100, 99.9999, 10)

assert label == 'STANDARD' 

# test heavy package ('SPECIAL')

label = sort(10, 10, 10, 21)

assert label == 'SPECIAL' 

# test bulky package ('SPECIAL')

label = sort(100, 100, 100, 10)

assert label == 'SPECIAL' 

label = sort(150, 10, 100, 10)

assert label == 'SPECIAL' 

# test heavy and bulky package ('REJECTED')

label = sort(102.3, 100, 100, 25)

assert label == 'REJECTED' 

label = sort(152.5, 10, 100, 20.5)

assert label == 'REJECTED'


print('... DONE')