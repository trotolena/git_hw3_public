a = 2
b = 6
suma = 0
ints = [2, 3, 4, 5, 6]
avg = sum(ints) / len(ints)
print(avg)
for i in range(a, b+1):
    print('i =', i)
if sum(ints) % avg == 0:
    print(sum(ints))

# я не розумію цього завдання до кінця
a = 0
b = 50
sequence = range(a, b+1)
result_sum = 0

arif = sum(sequence) /len(sequence)

for i in sequence:
    if not i % arif:
        result_sum += i