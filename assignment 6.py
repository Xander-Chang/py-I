#回家功課

#1. 請使用P.23的Person類別衍生一個新的Employee類別，新類別有薪資(salary)與職等(level)的私有資料屬性。程式需求如下：
#請用getter與setter的方式來存取這兩個私有資料
#建立3個Employee的物件以{工號:Employee}的格式存放進字典
#使用者輸入工號可以顯示Employee的屬性資料
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

class Employee(Person):
    def __init__(self, name, age, salary, level):
        self.__salary = salary
        self.__level = level
        super().__init__(name, age)
    def getsalary(self):
        return self.__salary
    def getlevel(self):
        return self.__level
    
staff1 = Employee('sam', 18, 23000, 1)
staff2 = Employee('xander', 27, 60000, 5)
staff3 = Employee('sally', 24, 100000, 7)
dict = {1:staff1, 2:staff2, 3:staff3}
num = int(input('請輸入工號:\t'))
if(num in dict):
    
    #解一
    #私有屬性(方法解:方法要有'括號')
    """
    print('工號:\t{0}\n姓名:\t{1}\n年齡:\t{2}\n薪水:\t{3}\n職等:\t{4}'.format(num,(dict[num].name),(dict[num].age),(dict[num].getsalary()),(dict[num].getlevel())))
    #print('工號:\t',num,'\n姓名:\t',dict[num].name,'\n年齡:\t',(dict[num].age),'\n薪水:\t',(dict[num].getsalary()),'\n職等:\t',(dict[num].getlevel()))    
    """
    #解二
    #私有屬性(屬性解:用固定的破解格式去呼叫)
    """
    print('工號:\t',num,'\n姓名:\t',dict[num].name,'\n年齡:\t',(dict[num].age))
    print('薪水:\t',(dict[num]._Employee__salary),'\n職等:\t',(dict[num]._Employee__level))
    """
else:
    print('error')
'''


#老師解
'''
 class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    
 class Employee(Person):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age)
        self.__salary = salary
        self.__level = level
    @property
    def Salary(self):
        return self.__salary
    @Salary.setter
    def Salary(self, salary):
        self.__salary = salary
    @property
    def Level(self):
        return self.__level
    @Level.setter
    def Level(self, level):
        self.__level = level
        
 emp1 = Employee('John', 20, 30000, 1)
 emp2 = Employee('Mary', 30, 40000, 2)
 emp3 = Employee('Tom', 40, 50000, 3)
 empDict = {1:emp1, 2:emp2, 3:emp3}
 num = int(input('請輸入工號:'))
 if (num in empDict):
    print('工號:', num)
    print('姓名:', empDict[num].name)
    print('年齡:', empDict[num].age)
    print('薪水:', empDict[num].Salary)
    print('職等:', empDict[num].Level)
 else:
    print('無此工號員工!')
 '''





#2. 請使用輾轉相除法的遞迴運算設計GCD(p, q)函式來求得p與q兩個整數的最大公因數。   #看不懂????
'''
 def GCD(p, q):
    if (p == 0 or q == 0):
        return 0
    else:
        rem = p % q
        if (rem == 0):
            return q
        else:
            return GCD(q, rem)
        
n1 = 60
n2 = 96
res = GCD(n1, n2)
print('GCD({0}, {1}) = {2}'.format(n1, n2, res))
 '''


