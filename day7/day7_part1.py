import re

def get_rules():
    rules = {}

    with open("input.txt", "r") as file:
        rules_list = file.read().splitlines()

    for rule in rules_list:
        bags = re.findall(r"\w+ \w+(?= bag)", rule)
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
def contains_shiny_gold_bag(bag):
    if bag == "no other":
        return False
    
    if "shiny gold" in rules[bag]:
        return True
    
    for other_bag in rules[bag]:
        if contains_shiny_gold_bag(other_bag):
            return True
    else:
        return False


def how_many_contain_shiny_gold_bag(bags):
    total = 0

    for bag in bags:
        if contains_shiny_gold_bag(bag):
            total += 1

    return total


rules = get_rules()
print(how_many_contain_shiny_gold_bag(rules))
