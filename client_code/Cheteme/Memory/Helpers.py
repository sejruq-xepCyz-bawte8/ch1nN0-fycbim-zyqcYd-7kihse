def convert_objlist_to_list(self, proxy):
    list = [next(iter(d)) for d in proxy]
    return list


