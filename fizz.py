def fizzBuzz(num):
    for i in range(0,100):
        if num == 1:
            return 1
        if num % 3 == 0:
            return "fizz"
        elif num % 5 == 0:
            return "buzz"
