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
#	所谓多行注释，实为解释器忽略的多行字符串

#	导入
import math
from collections import Iterable
from collections import Iterator
from functools import reduce
import functools

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

#	print为输出函数
#	r开头表示不格式化
#	'''或"""表示多行文字
print(r'''hello,\n
world''')

#	条件判断
#	缩进表示同一代码段
#	if else elif 使用 : 结尾
if age >= 18:
	print("adult")
else:
	print("not adult")

#	True真 False假 and和 or或 not非
if True or not False:
	print("True or not false")

#	使用elif避免else if带来缩进叠堆
age = 3
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')

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
#'中文'.encode('ascii')#ERROR
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

try:
#	input接受输入，输出字符串
	s = input('birth: ')
#	int函数执行类型转换到int
	birth = int(s)
	if birth < 2000:
		print('00前')
	else:
		print('00后')
except:
	pass

names = ['Magnus Frankline', 'Jessee Xaiwelles', 'Ayas Karloccethe']
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
try:
	d.pop('A')
except:
	pass

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
print(hex(255))#0xff

#	定义函数，同一缩进表示同一代码段，构成函数体
def my_abs(x):
	if not isinstance(x, (int, float)):#类型检查
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
#fact(1000)#402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


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

#	一个可以遍历的列表进行遍历称为迭代Iteration，前者称为可迭代对象
#	使用for...in...:来实现
#	dict无下标，但也可以迭代，结果将是无序的
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)
#a
#c
#b
#	字符串也是可迭代对象
for ch in 'ABC':
	print(ch)
#A
#B
#C

#	判断是否为可迭代对象
#from collections import Iterable
isinstance('abc', Iterable)#True
isinstance([1,2,3], Iterable)#True
isinstance(123, Iterable)#False

#	用enumerate将list转换成索引元素对
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
#0 A
#1 B
#2 C

#	在for循环中可以同时使用两个或多个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)
#1 1
#2 4
#3 9



#	快速一行生成一个list
list(range(1, 11))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#	在list中直接使用for循环，生成的元素写在for左侧
[x * x for x in range(1,11)]#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#	双层for循环
[m + n for m in 'ABC' for n in 'XYZ']#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
#	三层for循环
[x + y + z for x in 'AB' for y in 'MN' for z in 'XY']#['AMX', 'AMY', 'ANX', 'ANY', 'BMX', 'BMY', 'BNX', 'BNY'] 

#	for循环后可以跟一个真假值，通常if可以返回一个，为真时才会取值
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]

#	由于存储一个巨大的list不现实，可以改为边用边算的方式，称为生成器generator
#	将[]改为()可创建一个generator
L = [x * x for x in range(10)]#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))#<generator object <genexpr> at 0x1022ef630>

#	使用next函数获得下一个值
next(g)#0
next(g)#1
next(g)#4
next(g)#9
next(g)#16
next(g)#25
next(g)#36
next(g)#49
next(g)#64
next(g)#81
try:
	next(g)#溢出，抛出StopIteration异常
except:
	pass
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#StopIteration

#	斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#	1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#	a, b = b, a + b实际上是将b, a + b以tuple的形式赋值给a ,b，而不是三个独立的语句a，b = b，a + b
#	包含yield的函数是生成器函数
#	函数运行至yield时返回，下一次从yield的下一条语句进入
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
#	一个生成器
f = fib(6)#<generator object fib at 0x104feaaa0>


def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)
	return

o = odd()
next(o)
#step 1
#1
next(o)
#step 2
#3
next(o)
#step 3
#5
try:
	next(o)
except:
	pass
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#StopIteration
#	一旦生成器函数从return返回，next抛出StopIteration异常

#	可以捕获StopIteration异常，其值为函数返回值
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
#g: 1
#g: 1
#g: 2
#g: 3
#g: 5
#g: 8
#Generator return value: done

#	可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#	可以使用isinstance()判断一个对象是否是Iterator对象：
#from collections import Iterator
isinstance((x for x in range(10)), Iterator)#True
isinstance([], Iterator)#False
isinstance({}, Iterator)#False
isinstance('abc', Iterator)#False
#	使用iter将Iterable变成Iterator
isinstance(iter([]), Iterator)#True
isinstance(iter('abc'), Iterator)#True

if False:
	#for循环的实质：
	for x in [1, 2, 3, 4, 5]:
		pass

	it = iter([1, 2, 3, 4, 5])#首先获得Iterator对象
	while True:#循环
		try:
			x = next(it)# 获得下一个值：
		except StopIteration:
			break# 遇到StopIteration就退出循环
		pass



#	变量可以指向函数
abs#<built-in function abs>

#	一个最简单的高阶函数
def add(x, y, f):
	return f(x) + f(y)


#	Python内建了map()和reduce()函数。
#	map函数接受两个参数，函数和Iterable，返回Iterator
def f(x):
	return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)#[1, 4, 9, 16, 25, 36, 49, 64, 81]
#	map实质是抽象了计算过程，下例不如前者抽象易懂
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
	L.append(f(n))
print(L)

#	reduce把一个函数作用在一个序列上，这个函数必须接收两个参数，
#	reduce把结果继续和序列的下一个元素做累积计算
#	reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#from functools import reduce
def fn(x, y):
	return x * 10 + y
def char2num(s):
	return DIGITS[s]
reduce(fn, map(char2num, '13579'))#13579

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn, map(char2num, s))

def char2num(s):
	return DIGITS[s]
def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))
	
#	Python内建的filter()函数用于过滤序列。
#	和map()类似，filter()也接收一个函数和一个序列。
#	和map()不同的是，filter()把传入的函数依次作用于每个元素，
#	后根据返回值是True还是False决定保留还是丢弃该元素。
#	filter()函数返回的是一个Iterator

#	在一个list中，删掉偶数，只保留奇数
def is_odd(n):
	return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))#[1, 5, 9, 15]
#	把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()
list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))#['A', 'B', 'C']

#	用filter求素数
#	计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
#	首先，列出从2开始的所有自然数，构造一个序列：
#	2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#	取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
#	3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#	取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
#	5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#	取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
#	7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#	不断筛下去，就可以得到所有的素数。
#	用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n
#	注意这是一个生成器，并且是一个无限序列。
#	然后定义一个筛选函数：
def _not_divisible(n):
	return lambda x: x % n > 0
#	最后，定义一个生成器，不断返回下一个素数：
def primes():
	yield 2
	it = _odd_iter() # 初始序列
	while True:
		n = next(it) # 返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it) # 构造新序列
#	这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
#	由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
#	打印1000以内的素数:
for n in primes():
	if n < 1000:
		print(n)
	else:
		break
#	注意到Iterator是惰性计算的序列，所以可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

#	Python内置的sorted()函数就可以对list进行排序
sorted([36, 5, -12, 9, -21])#[-21, -12, 5, 9, 36]
#	sorted可以从一个命名关键词参数key接受一个函数参数
sorted([36, 5, -12, 9, -21], key=abs)#[5, 9, -12, -21, 36]
#	默认情况下，对字符串排序，是按照ASCII的大小比较的，
#	由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
sorted(['bob', 'about', 'Zoo', 'Credit'])#['Credit', 'Zoo', 'about', 'bob']
#	要进行反向排序，可以传入参数reverse=True
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)#['Zoo', 'Credit', 'bob', 'about']



#	返回求和的函数
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
#	当调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f1 = lazy_sum(1, 3, 5, 7, 9)#<function lazy_sum.<locals>.sum at 0x101c6ed90>
#	调用函数f1时，才真正计算求和的结果：
f1()#25
#	当调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f2 = lazy_sum(1, 3, 5, 7, 9)
f1==f2#False
#	f1()和f2()的调用结果互不影响。

#	注意到返回的函数在其定义内部引用了局部变量args，所以，
#	当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
#	另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
def count():
	fs = []
	for i in range(1, 4):
		def f():
			 return i*i
		fs.append(f)
	return fs
f1, f2, f3 = count()
#	在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
#	f1()，f2()和f3()的期望结果应该是1，4，9，但实际结果是：
f1()#9
f2()#9
f3()#9
#	全部都是9的原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
#	它们所引用的变量i已经变成了3，因此最终结果为9。
#	返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#	如果一定要引用循环变量，可以是再创建一个函数，用该函数的参数绑定循环变量当前的值，
#	无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
	return fs
f1, f2, f3 = count()
f1()#1
f2()#4
f3()#9
#	缺点是代码较长，可利用lambda函数缩短代码。

#	在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
#	在Python中，对匿名函数提供了有限支持。以map()函数为例，计算f(x)=x2时，
#	除了定义一个f(x)的函数外，还可以直接传入匿名函数：
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))#[1, 4, 9, 16, 25, 36, 49, 64, 81]
#	匿名函数lambda x: x * x实际上就是：
#def f(x):
#	return x * x

#	关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#	匿名函数只能有一个表达式，不用写return，返回值就是该表达式的结果。
#	用匿名函数的好处是因为函数没有名字不必担心函数名冲突。匿名函数也是一个函数对象，
#	可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x#<function <lambda> at 0x101c6ef28>
f(5)#25
#	匿名函数可以作为返回值返：
def build(x, y):
	return lambda: x * x + y * y

#	函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print('2002-1-17')
f = now
f()#2002-1-17
#	函数对象有一个__name__属性，可以拿到函数的名字：
now.__name__#'now'
f.__name__#'now'

#	要增强now()函数的功能，在函数调用前后自动打印日志，但又不修改now()函数的定义，
#	这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#	本质上，decorator就是一个返回函数的高阶函数。所以，要定义一个能打印日志的decorator，可以定义如下：
#import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
#	因为log是一个decorator，所以接受一个函数作为参数，并返回一个函数。
#	需要用Python内置的functools.wraps把原始函数的__name__等属性复制到wrapper()函数中，
#	否则，有些依赖函数签名的代码执行就会出错。

#	要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
	print('2015-3-25')
now()
#call now():
#2015-3-25
#	把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)
#	由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
#	只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
#	wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受 *任意* 参数的调用。
#	在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

#	如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
#	要自定义log的文本：
def log(text):
	@functools.wraps(func)
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
#	这个3层嵌套的decorator用法：
@log('execute')
def now():
	print('2015-3-25')
now()
#execute now():
#2015-3-25

#	和两层嵌套的decorator相比，3层嵌套的效果是这样的：
#now = log('execute')(now)
#	首先执行log('execute')，返回decorator函数，变成decorator(now)，返回值最终是wrapper函数。

#	functools.partial创建一个偏函数，不需要自己定义int2()，可以直接创建一个新的函数int2
#import functools
int2 = functools.partial(int, base=2)
int2('1000000')#64
int2('1010101')#85
int2('1000000', base=10)#1000000
#	functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
#	返回一个新的函数，调用这个新函数会更简单。

class Person(object):
	def __init__(self, name, rank):
		self.name = name
		self.rank = rank
	def print_person(self):
		print('%s: %s' % (self.name, self.rank))

p1 = Person('Magnus Frankline', 1)
p2 = Person('Jessee Xaiwelles', 2)
p2 = Person('Ayas Karloccethe', 3)
p1.print_person()
p2.print_person()
p3.print_person()