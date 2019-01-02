from functools import reduce
def is_armstrong(number):
    number = str(number)
    li = []
    for oneNumber in number:
        li.append(int(oneNumber)) 
    exponentiation= map(lambda x: x**len(li), li)
    result = reduce((lambda x, y: x + y), exponentiation)
    number = int(number)
  
    if result == number:
        return True
    else:
        return False


