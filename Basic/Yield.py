"""
可以在函式中包括yield來「產生」值，
表面上看來，yield就像是return會傳回值，但又不中斷函式的執行。
"""
def myrange(n):
    x = 0
    while True:
        yield x
        x += 1
        if x == n:
            break

for i in myrange(8):
    print(i, end = '')

print()