

# def function_name(a1, a2):
#     # function body

#     return 

# def add(son1, son2):
#     return son1 + son2


# natija = add(10, 12)
# print(natija)





# def say_hello():
#     print('hello world')

# say_hello()
# say_hello()




# def add_numbers(num1, num2):
#     sum = num1 + num2
#     if sum == 9:
#         return sum + 1
#     return sum

# result = add_numbers(4,5)

# print(result)


# arbitraty arguments *args

# def my_sum(*sonlar): # args = [4,5,6,7,8,9,10,12, 13]
#     result = 0
#     for i in sonlar:
#         result += i
#     return result


# my_sum(4,5,6,7,8,9,10,12, 13)



# keyword args 

# def auto_info(**auto_malumotlar):
#     """
#     Bu mening birinchi funksiyam:
#     auto_malumotlar : bu kwargs argument bunga
#     xoxlagancha element bersangiz bo'ladi
#     """
#     for i in auto_malumotlar.items():
#         print(i)


# auto_info(speed=200, brand='Chevrolet', yil=2000, color='black')



# def juftmi(son):
#     if son % 2 == 0:
#         return True
#     return False


# print(juftmi(4))



# def isPerfect(son): # 28 = 1 + 2 + 4 + 7 + 14
#     result = 0
#     for i in range(1, son):
#         if son % i == 0:
#             result += i
    
#     return result == son
        
# print(isPerfect(27))
# print(isPerfect(6))



# 4 - misol 

# 3 ta ihtiyoriy sonning eng kattasi 

# 3, 4, 5

# a,b,c = 4,3,5

# def my_max(a,b):
#     if a > b:
#         return a
#     return b

# result = my_max(my_max(a,b), c)


# def eng_kattasi(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     return c


a = 'Madam'

# a[::-1] == a 

# def isPalindrom(a: str):
#     # a = 'madam'

#     i = 0 
#     n = len(a) - 1
#     a = a.lower()
#     while i < n:
#         if a[i] != a[n]:
#             return False
#         i += 1
#         n -= 1
#     return True

# print(isPalindrom('Madam'))



# def getConcatenation(nums: list): # [1,2,1]
#     a = nums.copy() 
#     nums.extend(a)
#     return nums


# result = getConcatenation([1,2,1])
# print(result)




nums = [1,2,3,4, 4,3,2,1] # [1,4,2,3,3,2,4,1]
# n = 4

# result = []

# for i in range(n):
#     result.append(nums[i])
#     result.append(nums[n + i])

# print(result)


# jewels = 'ab'  
# stones = 'aaabbbss sdfsdfd sdfdssdf'

# print(stones.split())

# result = 0

# for i in jewels:
#     if i in stones:
#         result += stones.count(i) # 3 + 3



# s = "Hello World"
# a = s.split() # ['hello', 'world']
# print(len(a[-1]))




# son qabul qilsin va 10 qo'shsin

# funksiya
# def add(son):
#     return son + 10


# result = lambda son: son + 10 

# print(result(20))



items = [3, 2, 10, 21, 23]

# def square(son):
#     return son ** 2
# list(map(square, items))

# a = list(map(lambda son: son ** 2, items)) #map >>> [9, 4, 100, 441, 469]

# print(a)

matnlar = ['python', 'code', 'developer', 'backend']

# matnni uzunligi 4 ga teng yo'ki kichik bo'lsa 0 aks holda matnning uzunligini 
# def uzunlik(matn):
#     if len(matn) <= 4:
#         return 0
#     return len(matn)

# a = lambda matn: 0 if len(matn) <= 4 else len(matn)

# result = list(map(a, matnlar))
# print(result)


# x = [2,3,4,7,1,11]
# y = [44,32,12,54,32,21]


# result = list(map(lambda a,b: a+ b, x,y))


# y = [44,32,12,54,32,21]

# def juftmi(son):
#     if son % 2 == 0:
#         return True
#     return False

# a = lambda son: True if son % 2 == 0 else False

# result = list(filter(a, y))

# print(result)



# s = ['Python', True, 10, 20, False, None]


# a = lambda element: True if type(element) == int else False


# result = list(filter(a, s))

# print(result)

# from functools import reduce

# result = reduce(lambda x, y: x + y, range(1, 101))
# print(result)




# chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}

# a = lambda x: (x.upper(), x.lower())

# def juft(x):
#     return x.upper(), x.lower()

# result = set(map(a, chars))

# print(result)




# student_data  = [
#     ('Alberto Franco', '15/05/2002','35kg'), 
#     ('Gino Mcneill','17/05/2002','37kg'), 
#     ('Ryan Parkes','16/02/1999', '39kg'), 
#     ('Eesha Hinton','25/09/1998', '35kg')
# ]

# ismlar = list(map(lambda x: x[0] , student_data))
# tugilgan_yillar = list(map(lambda x: x[1] , student_data))
# kgs = list(map(lambda x: x[2] , student_data))





nums1 = [1,2,3,4,5,6,7,8]
nums2 = [2,2,3,1,2,6,7,9]


result = list(map(lambda x,y: x == y, nums1, nums2))

print(result.count(True))
