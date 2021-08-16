class Filter:
    def __init__(self, filter_types):
        self.filter_types = filter_types

    def __call__(self, func):
        def wrap(list):
            list_1 = []
            for el in list:
                if isinstance(el, self.filter_types):
                    list_1.append(el)
            return func(list_1)
        return wrap


decor_filter = Filter
print(decor_filter)
