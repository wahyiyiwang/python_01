
#封装，不希望某部分数据被外界访问，可以使用_或__把变量或方法设置私有

class Students():

    name = "王五"
    __score = "80"

    def set__score(self,score):
        self.__score =score

    def get__score(self):
        return self.__score

print(Students.name)
s = Students()
s.get_score()