# #KODE1
# # def sequenceGenerator(start, stop):
# #     x = []
# #     for i in range (start, stop+1):
# #         x.append(i)
# #     return x
# # print (sequenceGenerator(1,10))

# # #KODE1
# SequenceGenerator = lambda start, stop: list(range(start, stop + 1))
# print(SequenceGenerator(0, 9))


# # #KODE2
# def fizzBuzz(a, b):
#     x = []
#     for num in range(a, b):
#         if num % 3 == 0 and num % 5 == 0:
#             x.append('FizzBuzz')
#         elif num % 3 == 0:
#             x.append('Fizz')
#         elif num % 5  == 0:
#             x.append('Buzz')
#         else:
#             x.append(num)
#     return x

# CobaKode = fizzBuzz (0,9)
# print (CobaKode)

# # #KODE2
# fizzBuzz = lambda a, b: [i if i % 3 != 0 and i % 5 != 0 else ('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)) 
#                          for i in range(a, b)]
# CobaKode = fizzBuzz (0,9)
# print (CobaKode)

# # #KODE3
# # def twoNumber(l):
# #     res = []
# #     for i in l:
# #         if l.index(i) == len(l)-1:
# #             break
# #         z = i + l[i+1]
# #         res.append(z)
# #     return res    

# # CobaKode3 = twoNumber ([2,3,4,5,6,7,8,9])
# # print (CobaKode3)


# #KODE3
TwoNumber = lambda l: [l[i] + l[i + 1] for i in range(len(l) - 1)]
CobaKode3 = TwoNumber ([6,7,8,9,10,11,12,13])
print (CobaKode3)

#KODE1
# List<int> sequenceGenerator(int start, int stop) => [for (var i = start; i <= stop; i++) i];
# List<int> result1 = sequenceGenerator(6,7,8,9,10,11,12,13);

#KODE2
# List<String> fizzBuzz(int a, int b) => [for (int i = a; i < b; i++) (i % 3 == 0 && i % 5 == 0) ? "FizzBuzz" : (i % 3 == 0) ? "Fizz" : (i % 5 == 0) ? "Buzz" : i.toString()];
# List<String> result2 = fizzBuzz(0, 5);

#KODE3
# List<int> twoNumber(List<int> l) => [for (var i = 0; i < l.length - 1; i++) l[i] + l[i + 1]];
# List<int> result3 = twoNumber([0, 1, 2, 3, 4, 5]);


# # void main(){
# #   print(result1);
# #   print(result2);
# #   print(result3);
# # }

# def fizz_buzz(a, b):
#     return list(map(lambda num: 'FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 
#                     else 'Buzz' if num % 5 == 0 else num, range(a, b)))

# CobaKode = fizz_buzz(0, 9)
# print(CobaKode)
