import re

# python 簡單匹配
print("1================================")
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat."
print(pattern1 in string)   # True
print(pattern2 in string)   # False

# 使用正則尋找配對
print("2================================")
print(re.search(pattern1, string))
print(re.search(pattern2, string))

# 使用[] 匹配
print("3================================")
ptn = r"r[au]n" # "run" or "ran"
print(re.search(ptn, string))

# [] 更多用法
print("4================================")
print(re.search(r"r[A-Z]n", "run rUn"))     # 匹配大寫英文
print(re.search(r"r[a-z]n", "run rUn"))     # 匹配小寫英文
print(re.search(r"r[0-9]n", "run r0n"))     # 匹配數字0-9
print(re.search(r"r[0-9a-z]n", "run r0n"))  # 匹配數字0-9或是小寫英文

# 匹配數字相關
print("5================================")
print(re.search(r"r\dn", "run r1n"))    # \d 表示任何數字
print(re.search(r"r\Dn", "run r1n r*n"))    # \D 表示除了數字以外其他字符

# 特殊符號\t、\n、\r、\f、\v
print("6================================")
print(re.search(r"r\sn", "run r\nn"))    # \s 表示任何特殊符號
print(re.search(r"r\Sn", "run r\rn"))    # \S 表示除了特殊符號以外其他字符


# 所有字母數字和"_"
print("7================================")
print(re.search(r"r\wn", "rUn r\nn"))    # \s 表示任何特殊符號
print(re.search(r"r\Wn", "run r\rn"))    # \S 表示除了特殊符號以外其他字符

# 空白字符
print("8================================")
print(re.search(r"\bruns\b", "dog runs to cat"))        # \b : empty string (only at the start or end of the word)
print(re.search(r"\B runs \B", "dog   runs  to cat"))   # \B : empty string (but not at the start or end of a word)


# 特殊字符"\"、"."
print("9================================")
print(re.search(r"runs\\", "runs\ to me"))     # \\ : match \
print(re.search(r"r.n", "r[ns to me"))         # . : match anything (except \n)

# 句首句尾
print("10================================")
print(re.search(r"^dog", "dog runs to cat"))   # ^string，表示string 在句首
print(re.search(r"cat$", "dog runs to cat"))   # string$，表示string 在句尾

# 是否
print("11================================")
print(re.search(r"Mon(day)?", "Monday"))       # 表示Monday or Mon
print(re.search(r"Mon(day)?", "Mon"))

# 多行匹配
print("12================================")
string = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I", string))
print(re.search(r"^I", string, flags = re.M))