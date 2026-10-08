import calculator

def test_add():
    assert calculator.add(1, 2) == 3

def test_sub():
    assert calculator.sub(2, 1) == 1

def test_mul():
    assert calculator.mul(2, 3) == 6

def test_div():
    assert calculator.div(6, 3) == 2
