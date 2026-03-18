def filter_numbers(numbers, threshold=0, greater=True):
    filter_list = []
    if greater==True:
        for i in numbers:
            if i > threshold:
                print(i)
                filter_list.append(i)
    else:
        for i in numbers:
            if i < threshold:
                print(i)
                filter_list.append(i)
    return print(filter_list)


filter_numbers([1, -5, 10, 0, 3], threshold=0, greater=True)
print()
filter_numbers([122, -5, 10, 0, 3], threshold=0, greater=False)
print()
filter_numbers([1, -5, 10, 0, 50], threshold=3, greater=True)
print()
filter_numbers([1, -15, 10, 0, -100], threshold=-10, greater=False)
print()
filter_numbers([1, -15, 10, 3, -100], threshold=-14, greater=False)