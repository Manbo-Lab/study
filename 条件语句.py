score = int(input("请输入您的成绩: "))
if score >= 90: 
    print("优秀")
elif score >= 80:
    print("良好")
else:
    print("需要努力")
#if-elif-else语句的执行顺序是从上到下，满足条件的代码块会被执行，其他的代码块会被忽略。
#if下面是elif，elif下面是else，else是可选的，elif可以有多个。
