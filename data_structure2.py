

# autos = {
#     "auto1": {
#         'brend': 'Chevrolet',
#         'yil': 2023,
#         'speed': 100,
#         'repaired_date': [2019, 2022, 2023]
#     },

#     "auto2": {
#         'brend': 'Chevrolet',
#         'yil': 2020,
#         'speed': 200,
#         'repaired_date': [2015, 2020]
#     }
# }

# print(autos.keys())

# print(autos['auto2'].values())


# a = {
#     'first': 1,
#     'second': 2,
#     'third': None
# }



# VAZIFALAR

# 2-MISOL

# dictionery = {'a': 100, 'b': 200, 'x': 300, 'y': 200}

# key = input('kalit so\'z kiriting: ')

# if key in dictionery.keys():
#     print('bu so\'z allaqachon lug\'atimizda bor')
# else:
#     value = input('qiymat kiriting :')
#     dictionery[key] = value

# print(dictionery)





# a = {
#     'first': 1,
#     'second': None,
#     'third': 3
# }

# kalitlar = list(a.keys()) # ['first', 'second', 'third'] # 3 ta

# if a[kalitlar[0]] == None:
#     a.pop(kalitlar[0])
# if a[kalitlar[1]] == None:
#     a.pop(kalitlar[1])
# if a[kalitlar[2]] == None:
#     a.pop(kalitlar[2])

# print(a)



# 6 - misol

# a =  [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# result = {} # {'yellow':[1,3]}

# if a[0][0] not in result.keys():
#     result[a[0][0]] = [result[0][1]] 
# else:
#     result[a[0][0]].append(a[0][1])

# if a[1][0] not in result.keys():
#     result[a[1][0]] = [result[1][1]] 
# else:
#     result[a[1][0]].append(a[1][1])

# if a[2][0] not in result.keys():
#     result[a[2][0]] = [result[2][1]] 
# else:
#     result[a[2][0]].append(a[2][1])


# 13 - misol

# students = [
#    {'student_id': 1, 'name': 'Jean Castro', 'class':'V'}, 
#    {'student_id': 2, 'name': 'Lula Powell', 'class':'V'},
#    {'student_id': 3, 'name':'Brian Howell','class':'VI'},
# ]


# key = input('kalit so\'z kiriting: ') # name
# value = input('Qiymat kiriting: ')

# if students[0][key] == value:
#     print(True)
# elif students[1][key] == value:
#     print(True)
# elif students[2][key] == value:
#     print(True)


# for i  in a:
#     ...




# n = 6 # i + j = 5
# # 3 , 5, 7, 9
# a = 3
# for i in range(1, n): 
#     for j in range(1, n): 
#         if i + j >= a:
#             print('', end='')
#         else:
#             print("*", end='')
#     a += 2
#     print("\n")




# a = [4, 8, 11, 43, 20]
# natija = a[0]* a[1] * a[2] * a[3] * a[4]

# if a[0] % 2 == 1:
#     natija += a[0]

# if a[1] % 2 == 1:
#     natija += a[1]

# if a[2] % 2 == 1:
#     natija += a[2]

# if a[3] % 2 == 1:
#     natija += a[3]

# if a[4] % 2 == 1:
#     natija += a[4]

# print(natija)



# a = []
# if not bool(a):
#     print('Bosh')
# else:
#     print('Boshmas')


# None, 0,  
# bool()


# 7 - misol

# a = [4, True, False, 50, None, 'Python']

# i = 2

# if type(a[i]) == int:
#     print(a[i])
# else:
#     print('Not Found') 


# a = ['Anvar', 'Zokir', 'Jamshid', 'Akobir', 'Mirzohid']

# print(sorted(a, key=len, reverse=True))




# peoples = {
#     'Javohir': 20, 
#     'Sanjar': 25, 
#     'Jamshid': 27
# } 
# ismlar = list(peoples.keys()) # ['Javohir', 'Sanjar', 'Jamshid']
# yoshlar = list(peoples.values()) # [20, 25, 27]

# result = f"Ism        Yosh\n{ismlar[0]}    {yoshlar[0]}\n{ismlar[1]}    {yoshlar[1]}\n{ismlar[2]}    {yoshlar[2]}"

# print(result)




# students = {
#   'Theodore': 19,
#   'Roxanne': 22,
#   'Mathew': 21,
#   'Betty': 20
# }

# ismlar = list(students.keys()) # ['Theodore', 'Roxanne', 'Mathew', 'Betty']
# yoshlar = list(students.values()) # [19, 22, 21, 20]

# eng_kichkina = min(yoshlar)  # 19
# eng_kottasi = max(yoshlar) # 22

# eng_kichkina_index = yoshlar.index(eng_kichkina) # 0
# eng_kotta_index = yoshlar.index(eng_kottasi) # 1

# print(ismlar[eng_kotta_index], ismlar[eng_kichkina_index])





# a = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

# print(list(a.items()))



# *******
#      *    # 0 + 5
#     *     # 1 + 4
# *******
# *******
# *******
# *******

# # 9 - misol

# for i in range(7):
#     for j in range(7):
#         if i in [0,6] or i + j == 5:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")




# [
#     [0,0,0,0],
#     [0,1,2,3],
#     [0,2,4,6]
# ]

# row = 3
# column = 4
# result = []  

# for i in range(row):
#     a = []
#     for j in range(column):
#         a.append(i*j) #[0,0,0,0]
#     result.append(a)

# print(result)