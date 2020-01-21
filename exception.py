def divide(a, b):
    try:
        answer = a / b
    except TypeError:
        answer = 'Type of opperand is incorrect'
    except:
        answer = 'Error in input data'
    else:
        ('Else clause')
    finally:
        print('Finally')
    return answer
