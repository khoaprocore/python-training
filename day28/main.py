def bracket_hash(formula):
    element = ""
    element_hash = {}

    for x in formula:
        if x.isupper():
            if element!="":
                element_hash[element] = 1
                element = ""
            element = x

        elif x.islower():
            element += x            

        else: 
            element_count = int(x)
            element_hash[element] = element_count
            element_count = 0
            element = ""

    if element!="":
        element_hash[element] = 1

    return element_hash


print(bracket_hash("PbSO4"))

