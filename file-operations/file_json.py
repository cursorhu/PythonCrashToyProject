import json
file = 'test.json'
file2 = 'test.txt'

def _write_file_test():
    with open(file, 'w') as f:
        #json dump支持将数据(包括格式)直接写入文件，而不需要将数据转成字符串写入
        data = [1,3,5,7,{"key1":1, "key2":2}]
        json.dump(data, f) #data写入文件，注意和json.dumps区分
    
    #json.load是要按格式层层解析的，因此无法解析多组类型数据的组合(不存在的数据类型)，只能解析多组类型数据的嵌套(例如外层list,内层map)
    # with open(file, 'a') as f:
    #     data = {"key1":1, "key2":2}
    #     json.dump(data, f)
           
def _read_file_test():
    with open(file, 'r') as f:
        data = json.load(f) #读文件到data，注意和json.loads区分
    print(data)

def _write_file_test2():
    with open(file2, 'w') as f:
        # write() argument must be str, not list
        data = "[1,3,5,7,{\"key1\":1, \"key2\":2}]" 
        f.write(data)
        
def _read_file_test2():
    with open(file2, 'r') as f:
        data = f.read()
    print(data)
    
if __name__ == '__main__':
    _write_file_test()
    _read_file_test()
    _write_file_test2()
    _read_file_test2()
    
            
