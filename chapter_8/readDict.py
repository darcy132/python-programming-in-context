
import ast

class StringDictConverter:
    def __init__(self, input_string):
        self.input_string = input_string

    def convert_to_dict(self):
        try:
            # 使用ast模块的literal_eval函数将字符串转换为字典
            dictionary = ast.literal_eval(self.input_string)
            if isinstance(dictionary, dict):
                return dictionary
            else:
                raise ValueError("输入字符串不是有效的字典表示形式")
        except (ValueError, SyntaxError) as e:
            print(f"转换失败：{e}")
            return None
        
def getFreq(t):
    return t[1]

def readFile(textFile):
    with open(textFile,'r') as f:
        a = f.read()
        b = StringDictConverter(a)
        return_dict = b.convert_to_dict()
        lfList = list(return_dict.items())
        lfList.sort(key = getFreq,reverse=True)
        for key in lfList:
            print("{0} {1:.3f}".format(key[0]))

if __name__ == "__main__":
    readFile("letterFrequency.txt")

