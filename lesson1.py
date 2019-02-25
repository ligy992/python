coding: utf8
#coding=utf-8;
# -*- coding:utf-8 -*- 
print "您好";

print '100+200=',100+200

name =raw_input('please your input name:');
print 'hello',name;

a = 2;
if a >= 3 :
	print a ;
else :
  print -a;

print 'i\'m ok!';
print 'i\'m ok\n are you ok';

print len(classname);
print classname[0];

classname = ['name','pcd','pig'];
# print classname;
classname.append('Adam'); 
classname.insert(1,'lgy');
classname.pop(0);
classname[1]='add';
print classname;

a=3;
if a>=30:
	print a;
elif a>=60:
  print -a;
else:
 	print 1;
 	
 	
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name;
    
sum=0
# for x in [1,2,3,4,5,6,7,8,9]:
for x in range(101):
  sum=sum+x;
  print sum;
  
  
sum=0
n=99
while n>0:
	sum=sum+n
	n=n-2
print sum;


birth =int(raw_input('birth:'));
if birth>2000:
	print '00后'
else:
	print '00前'
	
	
score={'sda':99,'djao':98,'csi':97}
score.pop('sda')
print score;


score['fds']=91
print score['fds'];


s=set([1,2,3,4,5,6])
s.add(7)
s.remove(2)
print s


s=set([1,2,3,4,5,6])
s2=set([1,2,3,8,9,10])
print s&s2
print s|s2

a=['a','b','c']
a.sort()
print a


a='abc'
a.replace('a','A')
b=a.replace('a','A')
print a
print b


# coding=utf-8;
# 函数形参
def printMax(a,b):
  if a>b:
  	print a,'is maximum';
  else:
  	print b,'is maximum';

printMax(3,4) 
x=5
y=7
printMax(x,y);

# 局部变量
def func(x):
	print 'x is',x
	x=2
	print "changed local x to",x

x = 50
func(x)
print 'x is still',x

# 全局变量
def func():
	global x
	print 'x is',x
	x=2
	print 'changed local x to',x
x=50
func()
print 'value of x is',x

# 默认参数值
def say(message,times=1):
	print message * times
say('hello')
say('world',5)


# 返回商和余数

a=5
b=2
s=divmod (a,b)
print s


# 四舍五入
a=1.234567
b=2
s=round(1.234567,2)
print s

# 圆周率模块调用
import math;
print math.pi


"""请计算:19+2*4-8/2"""
a=19+2*4-8/2
print a

dir(module)  # 可以通过它查看任何模块中所包含的工具。
help (math pow)  # 查询模块中pow函数的使用说明，其中pow可换成任意一种函数类型

lang='study python'
print lang[0]
print lang[1]
print lang.index('p')
print lang[2:6]
print lang[1:]
print lang[:]
print lang[:5]


str1='abc'
str2='abcde'
print str1+str2

# 使用break语句
s=1
running = True
while  running:
	s=raw_input('enter somethong:')
	if  s=='quit':
		break
	print 'length of thr string is',len(s)
print'done'



 number=23
 guess = int(raw_input('please input number:'))
 if guess == number:
 	print 'Congratulations, you guessed it.' 
 elif guess < number:
 	print 'No, it is a little higher than that'
 else :
 	print 'No, it is a little lower than that'

 print 'Done'


# 使用continue语句，continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后 继续 进行下一轮循环。
s=1
running = True
while  running:
	s=raw_input('enter somethong:')
	if  s=='quit':
		break
	if len(s)<3:
		print'input is of sufficient length'


# 占位符
a="%d years" % 15
print a

# split将字符串根据某个分割符进行分割
a="i love you"
print a.split(" ")


# S.strip() 去掉字符串的左右空格
# S.lstrip() 去掉字符串的左边空格
# S.rstrip() 去掉字符串的右边空格
a=' hello ' 
print a.strip()
print a.lstrip()
print a.rstrip()


def maximum(x,y):
  if x>y:
	return x
  else:
	return y

print maximum(2,3);


def printmax(x,y):
	'''prints the maximum of two mumber.
	the two values must be intehers.'''
	x=int(x)
	y=int(y)
	if x>y:
		print x,'is maximum'
	else:
		print y,'is maximum'
printmax(3,5)
print printmax.__doc__ 


# 模块引用
#!/usr/bin/python
# Filename: using_sys.py
import sys

print 'The command line arguments are:'
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n' 


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
