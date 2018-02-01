#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#	参考书：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000

#	单行注释
'''
多
行
注
释
'''
"""多行
注释"""
#所谓多行注释，实为解释器忽略的字符串

#	导入
import math

#	第一次出现的赋值语句进行变量声明
age = "old world"
#	非强类型，可以改变数据的类型
age = 8
#	惯例用全大写表示希望的常量
PI = 3.14159265359
#	除法的结果永远是浮点数
9 / 3#3.0
#	//表示地板除，结果为整数，向下取余
5 // 2#2
5 % 2#1


if age >= 18:#条件判断
#	缩进表示同一代码段
    print("adult")
else:
    print("not adult")
#	r开头表示不格式化 '''或"""表示多行文字
print(r'''hello,\n
world''')
#	True False and or not
if True or not False:
    print("True or not false")

#	单字符编码
ord('A')#65
ord('中')#20013
#	单字符解码
chr(66)#'B'
chr(25991)#'文'
#	字符串编码
#	b开头表示字节串
'ABC'.encode('ascii')#b'ABC'
'中文'.encode('utf-8')#b'\xe4\xb8\xad\xe6\x96\x87'
'中文'.encode('ascii')#ERROR
#	字符串解码
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')#'中'

#	字符串长度
len('ABC')#3
len('中文')#2
#	字节数
len(b'ABC')#3
len(b'\xe4\xb8\xad\xe6\x96\x87')#6
len('中文'.encode('utf-8'))#6

#	%作为间隔，后面传参
#	%s接受字符串，可以万用
'Hello, %s' % 'world'#'Hello, world'
#	%d表示传入整形，同C
'Hi, %s, you have $%d.' % ('Michael', 1000000)#'Hi, Michael, you have $1000000.'
#	%%转义为%
'growth rate: %d %%' % 7#'growth rate: 7 %'
#	另一种方式
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)#'Hello, 小明, 成绩提升了 17.1%'

#	tuple用()声明，指向不可变，单元素tuple：(元素,)
#	list用[]声明
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
#	-1表示倒数第一个
t[2][-1] = 'Y'
print(t)#('a', 'b', ['X', 'Y'])

#	使用elif
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#	input接受输入，输出字符串
s = input('birth: ')
#	int函数执行类型转换到int
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')


names = ['Magnus', 'Jessee', 'Ayas']
#	for可以用in来遍历
for name in names:
    print(name)

#	list(range(5))返回[0,1,2,3,4]
list(range(5))

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#	while语句进行条件循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

#	{}定义字典dict
d = {'Magnus': 20, 'Jessee': 15, 'Ayas': 10}
#	提取dict
print(d['Magnus'])#20
#	提取不存在的元素会报错，提取前需要先判断
'Hifuno' in d
#	get返回key，不存在返回none或者自定义值
d.get('Mayina')
d.get('Alice', -1)

#	删除一个key
d.pop('Bob')

#	set函数根据传入的一个list定义集合set，每个元素都是唯一且无序的
s = set([1, 1, 2, 2, 3, 3])#{1, 2, 3}

#	add添加元素
s.add(4)#{1, 2, 3, 4}
#	remove移除元素
s.remove(4)#{1, 2, 3}

#	集合可以进行集合之间的运算
s2 = set([2, 3, 4])
#	交集
s & s2#{2, 3}
#	并集
s | s2#{1, 2, 3, 4}

#	调用函数
#	数学函数
abs(100)#100
abs(-20)#20
abs(12.34)#12.34
max(1, 2)#2
max(2, 3, 1, -5)#3

#	类型转换函数
int('123')#123
int(12.34)#12
float('12.34')#12.34
str(1.23)#'1.23'
str(100)#'100'
bool(1)#True
bool('')#False

#	变量a指向abs函数
a = abs 
#	所以也可以通过a调用abs函数
a(-1)#1

#	hex函数输出字符串形式的十六进制数字
print(hex(255)#0xff

#	定义函数，同一缩进表示同一代码段，构成函数体
def my_abs(x):
#	类型检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#	从文件中引用函数		
#from abstest import my_abs

#	pass语句什么都不做
def nop():
    pass

#	可定义默认函数，在必选函数之后
#	函数可以返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
#	函数返回多个值实为返回一个tuple
x, y = r = move(100, 100, 60, math.pi / 6)
print(x, y)#151.96152422706632 70.0
print(r)#(151.96152422706632, 70.0)

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
	
power(5)#25
power(5, 2)#25

#	默认参数的指向 *必须* 是 *不可改变的* ，否则会不稳定
#	None无法被改变
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#	可变参数：参数数量可变
#	必须在必选参数和默认参数之后
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

calc(1, 2)#5
calc()#0

#	可以将list传入函数
nums = [1, 2, 3]
#	用*解开list
calc(*nums)#14

#	关键词参数：参数数量可变，可带有关键词，自动组装为dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#	用 关键词=值 进行传参
person('Bob', 35, city='Beijing')#name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#	命名关键词参数：在关键词参数定义之后，添加命名的关键词参数，限制传参
#	需要在关键词参数之后，可以用 * 直接定义关键词参数而不接受参数
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer', city='Beijing')#Jack 24 Beijing Engineer

#	函数参数表定义顺序：必选参数、默认参数、可变参数、关键字参数和命名关键字
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


#	阶乘：递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
fact(1)#1
fact(5)#120
fact(100)#93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

#	避免堆栈溢出，使用尾递归
#	
#	尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#	这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
#	都只占用一个栈帧，不会出现栈溢出的情况。
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
fact(1000)#402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


L = ['Magnus', 'Jessee', 'Ayas', 'Mayina', 'Hifuno']
#	切片：取0到2的参数，不包括第3个，如果是0可以省略
L[0:3]#['Magnus', 'Jessee', 'Ayas']
L[:3]#['Magnus', 'Jessee', 'Ayas']

L[-1:]#['Hifuno']
L[-2:]#['Mayina', Hifuno']
L[-2:-1]#['Mayina']

L = list(range(100))
#	前10个数，0到9：
L[:10]#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#	后10个数，-9到0：
L[-10:]#[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#	前11-20个数，10到19：
L[10:20]#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

#	所有数，每5个取一个：
L[::5]#[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
#	只写[:]可以原样复制一个list：
L[:]#[0, 1, 2, 3, ..., 99]

#	tuple也是一种list，操作的结果仍是tuple：
(0, 1, 2, 3, 4, 5)[:3]#(0, 1, 2)
#	字符串也是一种list，每个元素就是一个字符。切片操作结果仍是字符串：
'ABCDEFG'[:3]#'ABC'
'ABCDEFG'[::2]#'ACEG'