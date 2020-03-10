import time
name = "Welcome:"
print("Please type your name")
inp_name = input()
print(name, inp_name)
wel_word = "You got:"

result = ['A', 'B', 'C', 'D', 'F']  # store grade results into the list
c = result.append('E')
print(result)
# point = 0
print("Please key your point")
got = input()
me = int(got)


if 49 < me < 55:
    print(wel_word, result[3])

elif 54 < me < 65:
    print(wel_word, result[2])

elif 64 < me < 75:
    print(wel_word, result[1])

elif 74 < me < 101:
    print(wel_word, result[0])

else:
    print("you point is out of the scope")













