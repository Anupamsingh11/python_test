from test import add 



def test1():
    assert add("//,\n") == 0

def test2():
    assert add("//,\n1") == 1

def test3():
    assert add("//,\n1,5") == 6

def test4():
    assert add("//,\n1\n5,10") == 16

def test5():
    assert add("//;\n1;2") == 3

def test6():
    assert add("//;\n1;-2") == -1


if __name__=="__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()