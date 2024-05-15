# fib = 0
# fib1 = 1
# fib2 = 0
# n = 9
# count = 0


# while fib2 < n:
#     fib2 = fib + fib1
#     fib = fib1
#     fib1 = fib2
#     count += 1
#     if fib2 > n: 
#         print("-1")
#     elif fib2 == n:
#         print (count)
# print (fib2)



# def sum_str(*args):
#     str=""
#     for i in args:
#         str+=i
#     print(str)
# sum_str("o","s","a","m","a")


# import mudol1
# print(mudol1.max1(10,3))

# рекурция

# 


# def quick_sort(array):
#     if len(array) <=1:
#         return array
#     else:
#         pivot=array[0]
#     less=[i for i in array[1:] if i<= pivot]
#     greater=[i for i in array[1:] if i > pivot]
#     return quick_sort(less)+[pivot]+quick_sort(greater)
# print(quick_sort([8,10,14,2,7,9,0]))

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid=len(nums)//2
#         left=nums[:mid]
#         right=nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i=j=k=0
#         while i < len(left) and j < len(right):
#             if left[i]< right[j]:
#               nums[k]=left[i]
#               i+=1
#             else:
#                 nums[k]=right[j]
#                 j+=1
#             k+=1
#         while i < len(left):
#             nums[k]=left[i]
#             i+=1
#             k+=1
#         while j < len(right):
#             nums[k]=right[j]
#             j+=1
#             k+=1
# list1=[12,11,16,3,2,7,6,0]
# merge_sort(list1)
# print(list1)

#Интерполяция               
# a=3
# b=4
# c=5
# print(a,b,c)
# print ('{}-{}-{}'.format(a,b,c))
# print(f'first-{a} second-{b} third-{c}')


# print("введите первое число")
# a= int(input())
# print("введите второе число")
# b= int(input())
# c=a+b
# print("сумма равно:" +str(c))

# n = 555
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(summa)


#Пользователь вводит число, необходимо найти минимальный делитель данного числа
#Решение:

# n = int(input())
# flag = True
# i=2
# while flag:
#         if n % i == 0:              # если остаток при делении числа n на i равен 0
#                      flag = False
#                      print(i)
#         elif i > n // 2:                          # делит
#                         print(n)
#                         flag = False   
#         i += 1


# list_1 = list() # создание пустого списка
# for i in range(5): # цикл выполнится 5 раз
#  n = int(input()) # пользователь вводит целое число
#  list_1.append(n) # сохранение элемента в конец списка
#  print(list_1)


# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# del dictionary['left'] 
# print(dictionary)

# k="ноутбук"
# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_ru:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)


# x="osama"
# b=[]
# for i in x:
#     if i not in b:
#         b.append(i)


# print(b)






var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел

# elementsset1 = set(map(int, var2.split()))
# elementsset2 = set(map(int, var3.split()))

# intersectionset = sorted(list(elementsset1.intersection(elementsset2)))

# result = ' '.join(map(str, intersectionset))
# print(result)

#variant2

# elementsset1 = set(int(x) for x in var2.split())
# elementsset2 = set(int(x) for x in var3.split())

# intersectionset = sorted(list(elementsset1.intersection(elementsset2)))

# result = ' '.join([str(x) for x in intersectionset])
# print(result)
 
 #var3

# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')






