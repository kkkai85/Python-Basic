# Python 資料型態: 數字、字串、布林值、列表List、固定列表Tuple、集合Set、字典

# 數字，在Python 3中，整數就是整數，不再區分整數與長整數，整數的長度不受限制（除了硬體上的限制之外）。
print("十進制: " + str(10))
print("二進制: " + str(0b10))
print("八進制: " + str(0o10))
print("十六進制: " + str(0x10))
print("123: " + str(type(123)))
print("123.321: " + str(type(123.321)))

# 字串，在Python中字串有多種的表示方式。最基本的實字表示方式，就是使用雙引號或單引號來包括字元序列。
string = "'Hello Python'"
print(string)
print("字串長度: ", len(string))
print("判斷字串中是否包含另一個字串: ", 'Python' in string)

# 格式化字串方法，可以根據位置、關鍵字來進行字串格式化。
format_string = "Hello {H}".format(H = "Python")
print("格式化字串: " + format_string)

# 布林值
True
False

# 列表Tuple() 小括號，有順序、不可動的列表
(3, 4, 5)
("Hello", "Tuple")

# 列表List[] 中括號，有順序、可動的列表
[3, 4, 5] 
["Hello", "List"]

# 集合Set{} 大括號，集合，無序、元素不重複
{3, 4, 5}
{"Hello", "Set"}

# 字典Dictionary 鍵值對應 {"鍵":"值","Key":"Value"}
{"apple":"蘋果", "data":"資料"}