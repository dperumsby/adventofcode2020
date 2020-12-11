# XMASCracker Script

def load_encrypted_data():
    with open("input.txt", "r") as file:
        encrypted_data = file.read().splitlines()
        encrypted_data = [int(number) for number in encrypted_data]
    return encrypted_data


def first_exception(encrypted_data):
    index = 25

    for number in encrypted_data[25:]:
        previous25 = encrypted_data[index-25: index]
            
        for summand in previous25:
            if number - summand in previous25:
                break
        else:
            return number
            
        index += 1


def find_encryption_weakness(encrypted_data, first_exception):    
    for start_index in range(len(encrypted_data)):
        end_index = start_index + 1
        cont_range = []
        cont_sum = 0

        while cont_sum <= first_exception:
            if cont_sum == first_exception:
                return min(cont_range) + max(cont_range)
            
            end_index += 1
            cont_range = encrypted_data[start_index: end_index + 1]
            cont_sum = sum(cont_range)


encrypted_data = load_encrypted_data()
exception = first_exception(encrypted_data)

print(exception) # 15353384
print(find_encryption_weakness(encrypted_data, exception)) # 2466556
