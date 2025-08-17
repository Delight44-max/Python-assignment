def capitalize_name(name):
    return name.capitalize()

def capitalize_names(names):
    return list(map(capitalize_name, names))

if _name_ == "_main_":
    names = ['john', 'mary', 'steve']
    print(capitalize_names(names)) 