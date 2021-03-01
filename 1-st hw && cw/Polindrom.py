import math
import time

start_time = time.time()


# Знайти найбільший існуючий поліндром який може утворитися
# завдяки добутку двох простих пятизначних чисел.

def find_poli():
    # ------check if num is a palindrome--------
    def is_polka(numm):
        if all(numm[j] == numm[(len(numm) - 1) - j] for j in range(len(numm))):
            return True
        return False

    # ----finding prime numbers--------
    lst = []
    for num in range(10001, 100000, 2):
        if all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2)):
            lst.append(num)

    # --------res = max palindrome-----------
    res = 0
    for x in lst:
        for y in lst:
            if is_polka(str(x * y)) and x * y > res:
                res = x * y

    print(res)

    """
    lfm = []
    for x in lst:
        for y in lst:
            if is_polka(str(x * y)):
                lfm.append(str(x * y))
    # ------------checking max num of  list
    print(max(lfm))
    """


find_poli()
print("--- %s seconds ---" % (time.time() - start_time))
