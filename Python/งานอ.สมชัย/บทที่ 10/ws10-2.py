try:
    num_dist = {1:'one', 2:'two', 3:'three'}
    num_list = [1, 2, 3]

    for n in range(len(num_list)):
        print(num_list[n])
    for n in range(len(num_dist)):
        print(num_dist[n])
except KeyError:
    print('You use key not found.')
except IndexError:
    print('You define index error.')
print('This is test use exception.')