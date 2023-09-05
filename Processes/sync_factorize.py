import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def sync_factorize(numbers):
    results = []
    for number in numbers:
        results.append(factorize(number))
    return results


if __name__ == '__main__':
    numbers = [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
               380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    start_time = time.time()
    results = sync_factorize(numbers)
    end_time = time.time()

    print(f"Час виконання: {end_time - start_time} секунд")
