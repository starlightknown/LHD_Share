import random
answer = random.randint(1, 20)
print('Im guessing a number from1 to 20')
count = 0
prediction = input()

while(True):
    count = count +1
    print('can you guess it?')
    if prediction > answer:
        print('the answer is high')
    elif prediction < answer:
        print('the answer is low')
    else:
        print('its correct!')
        break
    print(f'you have attempted for {count} times')

