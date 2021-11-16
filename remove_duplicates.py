# Lista inicial: [1,1,2,2,4]
# Lista final: [1,2,4]

# def remove_duplicates(some_list):
#     without_duplicates = []
#     for element in some_list:
#         if element not in without_duplicates:
#             without_duplicates.append(element)
#     return without_duplicates

def remove_duplicates(some_list):
    return set(some_list)

def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))

if __name__ == "__main__":
    run()

