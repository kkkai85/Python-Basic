print("Function max")
def max(m, n):
    if m > n:
        return m
    else:
        return n

print(max(10, 5))

"""
由於def是個陳述，執行到def的函式定義時，就建立了空串列物件，而這個物件會一直存在;
如果你沒有指定arr的串列物件 時，所使用的就一直會是一開始指定的預設空串列物件;
也因此，隨著每次呼叫都不指定arr的值，你附加的對象，都是同一個物件。
"""
print("Function appendList")
def appendList(element, arr = []):
    arr.append(element)
    return arr

print(appendList(10))
print(appendList(10, [1, 2, 3]))
print(appendList(10))


# 若事先不知道要傳入的引數個數，可以在定義函式的參數時使用*，代表該參數接受不定長度引數。
print("Function sum")
def sum(*numbers):
    total = 0
    for num in numbers:
        total += num

    return total

print(sum(1, 2, 3))
print(sum(1, 2, 3, 4, 5, 6))

# 區域函式，以直接存取包裹它的外部函式之參數（或宣告在區域函式之前的區域變數），如此可減少呼叫函式時引數的 傳遞。
print("區域函式")
def selection(number):
    # 找出未排序中最小值
    def min(m, j):
        if j == len(number):
            return m
        elif number[j] < number[m]:
            return min(j, j + 1)
        else:
            return min(m, j + 1)
    
    for i in range(0, len(number)):
        m = min(i, i + 1)
        if i != m:
            number[i], number[m] = number[m], number[i]

number = [1, 5, 2, 3, 9, 7]
selection(number)
print(number)

# 變數範圍
"""
函式中的x，其實是在函式範圍中所建立的新x，其覆蓋了外部的x範圍，
所以你所設定的是區域變數x，指定值給變數時，就是在該範圍中建立該變數。
如果取用變數時，也是從當時的範圍開始尋找，若沒有，才找尋外部範圍。

記得變數範圍的建立是在指定時發生，而不是在取用時發生。
"""
print("變數範圍")
x = 10
y = 10
def test1():
    x = 20
    print("In test1")
    print(x)
    print(y)

test1()
print(x)
print(y)

# 變數指定值的同時就確立其所在的範圍。
# 如果希望指定值的變數是全域範圍的話，則可以使用global指明。
def test2():
    global x
    x = 20
    print("In test2")
    print(x)

test2()
print(x)