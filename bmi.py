user_age = int(input("请输入您的年龄: "))
user_weight = float(input("请输入您的体重(kg): "))
user_height = float(input("请输入您的身高(m): "))
BMI = user_weight / (user_height ** 2)
#.2f表示保留两位小数(f = float)，.2表示保留两位小数
# {}表示占位符，format()会将BMI的值填充到占位符
print("您的BMI指数为: {:.2f}".format(BMI))