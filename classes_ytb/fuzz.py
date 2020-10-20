"""
Fizz Buzz Problemi:
1'den 50 ye kadar olan sayıları ekrana yazdıran bir program yazalım. Ancak programımız, 3'e bölünen rakamlar yerine "Fizz",
5'e bölünebilen sayılar yerine "Buzz", her iklsine de bölünebilenlere ise "FizzBuzz" yazacak. Programı Jupyter Notebook'ta ve aşağıda belirtilen 3 farklı şekilde yazalım.
For döngüsü kullanılarak,
While döngüsü ile,
List comprehension ile
"""

for i in range(1, 51):
    if i % 15 == 0:
        print(i, "Fizzbuzz")
    elif i % 5 == 0:
        print(i, "Buzz")
    elif i % 3 == 0:
        print(i, "Fizz")

i = 1

while (i<51):
    if i % 15 == 0:
        print(i, "Fizzbuzz")
    elif i % 5 == 0:
        print(i, "Buzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    i += 1

a =[(str(i) + "FizzBuzz" if i%15==0 else ((str(i)+ 'Buzz' if i%5==0 else (str(i) + "Fizz" if i % 3 == 0 else None)))) for i in range(1, 51)]

print(a)