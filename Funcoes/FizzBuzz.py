def fizzbuzz(n):
    res1 = n % 3
    res2 = n % 5

    if res1 == 0 and res2 != 0:
        return "Fizz"
    elif res1 != 0 and res2 == 0:
        return "Buzz"
    elif res1 == 0 and res2 == 0:
        return "FizzBuzz"
    else:
        return n
