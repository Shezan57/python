#step-1: defining a function called create_list

def create_list(numbers):
    return [number*2 for number in numbers]

# calling the create_list function with a list of numbers and printig the return value

numbers = [1,2,3,4,5]
print(create_list(numbers))

#step-2: defining a function called create_tuple

def create_tuple(numbers):
    return tuple(number*2 for number in numbers)

# calling the create_tuple function with a list of numbers and printig the return value

print(create_tuple(numbers))
