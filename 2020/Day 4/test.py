test_list = [{"a": 1, "b": 2, "c": 3}]

x = test_list[0]
y = {"d": 4}

z = {**x, **y}

print(z)