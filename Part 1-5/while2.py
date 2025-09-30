import time

number = 6
print("Countdown!")
while True:
  number = number-1
  time.sleep(0.5)
  print(number)
  if number <= 0:
    break

print("Now!")