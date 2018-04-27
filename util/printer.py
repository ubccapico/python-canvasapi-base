import collections

def print_odict(odict, depth=0, name=""):
    if type(odict) == str or type(odict) == int:
        print("{}{}".format("   " * depth, odict))
    elif type(odict) == list:
        for i in range(len(odict)):
            if type(odict[i]) == str or type(odict[i]) == int:
                print("{}{}[{}] = {}".format("   " * (depth), name, i, odict[i]))
            else:
                print("{}{}[{}]".format("   " * (depth), name, i))
                print_odict(odict[i], depth+1)
    elif type(odict) == collections.OrderedDict or type(odict) == dict:
        for key in odict.keys():
            if type(odict[key]) == list or type(odict[key]) == dict or type(odict[key]) == collections.OrderedDict:
                print("{}{}[{}]".format("   " * depth, name, key))
                print_odict(odict[key], depth+1)
            else:
                print("{}{}[{}] = {}".format("   " * depth, name, key, odict[key]))


def print_list(item_list, numbered=True):
    """prints all items in a list
    Keyword arguments:
    item_list -- list to be printed
    numbered -- whether to add numbers to the list (default True)"""
    
    longest_label = len(str(len(item_list)))
    longest_item = get_longest_item(item_list)
    
    border = "o-"
    if numbered:
        border += ("-" * longest_label) + "--o-"
    border +=  ("-" * longest_item) + "-o"

    print(border)    
    count = 0
    for item in item_list:
        s = "| "
        if numbered:
            count += 1
            s += (' ' * (longest_label - len(str(count))))
            s += "{}) | ".format(count)
        s += str(item)
        s += (' ' * (longest_item - len(str(item))))
        s += " |"
        print(s)
    print(border)


def get_longest_item(item_list):
    """gets longest length of item in list"""    
    length = 0
    for item in item_list:
        if len(str(item)) > length:
            length = len(str(item))
    return length
