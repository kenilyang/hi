w = input('請輸入您的身高：')
h = input('請輸入您的體重：')
s = input('請輸入您的性別：')
name = input('請輸入您的姓名：')
bmi = int(h) / int(w)
if s == '男' :
	print(name, '您的姓別為', s,'您的BMI為' ,bmi)
elif s == '女' :
    print(name, '您的姓別為', s,'您的BMI為' ,bmi)
else :
    print('請輸入 (男 / 女)')
