# 输出小于100的斐波那契数列
# 代码学习： 这里的b相当于是当前位置的数，而a每次都保存了前一次的值
print('小于100的斐波那契数列')
a = 0
b = 1
while b < 100:
    print(b, end = " ")
    a, b = b, a + b
    
