# File 實體物件的設計: 包裝檔案讀取的程式
class File:
	def __init__(self, filename):
		self.filename = filename
		self.file = None	# 尚未開啟檔案: 初期是None，代表Null

	def open(self):
		self.file = open(self.filename, mode = "r", encoding = "utf-8")

	def read(self):
		return self.file.read()

# 讀取第一個檔案
file1 = File("FileIO.txt")
file1.open()
print(file1.read())