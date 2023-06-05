from customAdder import myAdder


def testing():
    obj = myAdder()
    solns = [[1, 2, 3], [5, 6, 11], [600, 200, 800]]
    for s in solns:
        a = s[0]
        b = s[1]
        c = s[2]
        c_pred = obj.add_2_numbers(a, b)
        if c != c_pred:
            assert False

    assert True