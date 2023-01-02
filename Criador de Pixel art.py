import sys,time,os

message="\nOO\033[8;33;41mOO\033[mOO\033[8;33;41mOO\033[mOO\
\n\033[8;33;41mOOOOOOOO\033[1;33;41mOO\033[m\nOO\033[8;33;41mOOOOOO\033[mOO\nOOOO\033[8;33;41mOO\033[mOOOO"


def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.009)
        else:
            time.sleep(1)


os.system("12") #clear
typewriter(message)

print('\n')
print('\033[1;33;36mPixel\033[1;33;33mart\033[m \033[4;33;37mcom python\033[m')
