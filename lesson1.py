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
