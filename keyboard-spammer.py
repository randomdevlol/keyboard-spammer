from sys import argv
from time import sleep
from keyboard import write,press_and_release

words = argv[1:]

sleep(5)

for word in words:
    # press_and_release('t')
    write(word)
    press_and_release('enter')
    sleep(0.1)