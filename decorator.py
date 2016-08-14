def table(func):
    def math(b, c, d):
        print('it is small math operation')
        if (c+d)>b:
            print ('c+d must be less than b')
            return
        return func(b, c, d)
    return math

@table
def operation(b, c, d):
    print( b-(c+d))

operation(10, 15, 4)
    

