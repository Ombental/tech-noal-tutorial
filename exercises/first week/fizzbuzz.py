results1 = [['Fizz', '', ''][i % 3] + ['Buzz', '', '', '', ''][i % 5] if i % 3 == 0 or i % 5 == 0 else str(i) for i in range(1, 101)]
results2 = ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else str(i) for i in range(1, 101)]
for result in results1:
    print(result)