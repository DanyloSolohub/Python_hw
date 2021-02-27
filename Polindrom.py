import math


# Знайти найбільший існуючий поліндром який може утворитися
# завдяки добутку двох простих пятизначних чисел.

def find_poli():
    # ----finding prime numbers--------
    lst = []
    for num in range(30001, 33500, 2):
        if all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2)):
            lst.append(num)

    # ------check if it is a palindrome--------
    def is_polka(numm):
        if all(numm[j] == numm[(len(numm) - 1) - j] for j in range(len(numm))):
            return True
        return False

    # --------list with multiplication of prime number-----------
    lfm = []

    for x in lst:
        for y in lst:
            lfm.append(str(x * y))
    # ------------checking the lis and finding the polyndrome
    res = 0
    for k in range(len(lfm)):
        if is_polka(lfm[k]) and int(lfm[k]) > res:
            res = int(lfm[k])
    print(res)


find_poli()
