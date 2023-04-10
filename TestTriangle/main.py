def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


if __name__ == '__main__':
    assert is_triangle(3, 4, 5) == True
    assert is_triangle(2, 2, 5) == False
    assert is_triangle(1, 1, 1) == True
    assert is_triangle(0, 5, 5) == False
    assert is_triangle(-3, 4, 5) == False


