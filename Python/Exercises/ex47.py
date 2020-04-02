from time import sleep
for cont in range(0, 51):
    sleep(0.3)
    numero=cont % 2
    if numero == 0:
        print(cont)
    