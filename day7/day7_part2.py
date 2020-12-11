import re

def get_rules():
    rules = {}

    with open("input.txt", "r") as file:
        rules_list = file.read().splitlines()

    for rule in rules_list:
        bags = re.findall(r"\d? ?\w+ \w+(?= bag)", rule)
        bag = bags[0]
        bag_contents = bags[1:]
        
        rules[bag] = bag_contents 

    return rules


def memoize(f):
    cache = {}

    def memoized_function(bag):
        if bag in cache:
            return cache[bag]
        result = f(bag)
        cache[bag] = result
        return result
    
    return memoized_function


@memoize
def contains_how_many_bags(bag):
    total = 0
    for other_bag in rules[bag]:
        
        if other_bag == " no other":
            return 0

        number = int(other_bag[0])
        style = other_bag[2:]

        total += number + (number * contains_how_many_bags(style))

    return total


rules = get_rules()
print(contains_how_many_bags("shiny gold"))
