#WAF to print the elements of a list in a single line.(list is the parameter)

heroes = ["Nani","AA","Pawan Kalyan","VD","NTR"]

def print_list(heroes):
    for items in heroes:
        print(items,end=" ")  

print_list(heroes)