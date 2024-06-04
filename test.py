def add(a):
    delim = a[2]
    a = a[4:]
    a = a.replace('\n', delim)
    list = a.split(delim)

    sum = 0
    for i in list:
        if (i != ""):
            j = int(i)
            if j < 0:
                raise Exception("negative numbers not allowed " + i)
            else:
                sum += j

    return sum
