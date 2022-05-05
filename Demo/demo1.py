# encoding: UTF-8

a = 'Hallo Welt!'
print(type(a))

a = 123
print(type(a))

a = 1.23
print(type(a))

a = 1, 2, 'A', 'B'
print(type(a))

a = {"Key1":"Value1", "Key2":"Value2"}
print(type(a))
print(a)

print(a["Key1"])
print(a["Key2"])

a["Key1"] = "Korr1"
print(a["Key1"])
print(a["Key2"])

a["Key3"] = "Value3"
print(a["Key3"])

print(a)

for i in range(1, 11):
    for j in range(1, i+1):
        print(j, end="")
    print("\n", end="")