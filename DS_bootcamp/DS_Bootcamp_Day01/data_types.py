def data_types():
    var_int = 21 
    var_str = "school"
    var_float = 3.15 
    var_bool = True
    var_list = [1, 2, 3]
    var_dict = {'name' : 'Alina'}
    var_tuple = (1, 2, 3)
    var_set = {1, 2, 3}

    list_types = [
        type(var_int),
        type(var_str),
        type(var_float),
        type(var_bool),
        type(var_list),
        type(var_dict),
        type(var_tuple),
        type(var_set)
    ]
    names = [t.__name__ for t in list_types]
    print(names)

if __name__ == '__main__':
    data_types()