# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Choi",
    "age" :32  }

v_list = [3,5,7]  #타언어에서는 배열이라고 함.
v_tuple = 3,5,7
v_set = {7,8,9}

print(type(v_tuple))
print(type(v_dict))

i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999999
big_int2 = 777777777777777777
f1 = 1.234
f2 = 3.745
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1**f2)
print(f3+i2)   #자동으로 실수로 형변환으로 이뤄짐.


result = f3+i2
print(result, type(result))