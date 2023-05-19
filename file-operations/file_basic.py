file = 'test.txt'

def _write_file_test():
    # python文件可以用open和close打开和关闭文件资源，
    # 但一般用with关键字：能在文件不用时自动close, 避免异常导致文件close不了，因此使用with时只有open没有close
    # 打开文件格式： open('文件路径', '读写属性') as 文件遍历
    with open(file, 'w') as f:
        data = """
        file test line 1
        file test line 2
        file test line 3
        """
        f.write(data)
        
    with open(file, 'a') as f:
        data = "file test line 4"
        f.write(data)
        
def _read_file_test():
    with open(file, 'r') as f:
        #读文件返回对象是列表，可以直接for遍历每一行
        for line in f:
            print(line.rstrip()) #文件内容本身带换行，print会自己加换行，rstrip消除额外换行

def _read_file_test2():
    with open(file, 'r') as f:
        #先读出列表，再遍历每一行
        lines = f.readlines()
        for line in lines:
            print(line.rstrip())
        
if __name__ == '__main__':
    _write_file_test()
    _read_file_test()
    _read_file_test2()
            
