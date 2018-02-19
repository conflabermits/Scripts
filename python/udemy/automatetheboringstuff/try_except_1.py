def div42by(divideBy):
    try:
        return 42 / divideBy
    #except ZeroDivisionError:
    except:
        #print('Error: You tried to divide by zero.')
        print('There was some kind of error.')
        return ''

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

