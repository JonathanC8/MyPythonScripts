arrayx = [5,10,11,8,8,6,8,22,58,10,10]

def mode():
    print("The mode is:")
    length = len(arrayx)-1
    for x in range(length):
        y=0
        for i in range(length):
            if arrayx[i] == arrayx[x]:
                y+=1
                if y == 2:
                    print(arrayx[x])

def median():
    med = len(arrayx)
    if med%2 >= 1:
        med = int(len(arrayx)/2)
        med = arrayx[med]
    else:
        med = int((len(arrayx)/2)-1)
        med = (arrayx[med]+arrayx[med+1])/2
    print("The median is:")
    print(med)

keepRun = ""

while keepRun != "stop":
	mode()
	median()
	keepRun = input()