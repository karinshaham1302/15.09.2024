# start

sum_temp: float = 0.0

for _ in range(1, 5 + 1):
    temperature: float = 0.0
    while True:
        temperature = float(input('what is the temperature?'))
        if -50 <= temperature <= 45:
            break
        print('not in the range')
    sum_temp += temperature

avg_temp: float = sum_temp / 5
print(f'the average is: {avg_temp}')

# stop
