def lwk(string,length):
    l=(('  #      '),('  #      '),('  #      '),('  #      '),('  #      '),('  #      '),('  #      '),('  #      '),('  #####  '))
    w=(('  #   #  '),('  #   #  '),('  #   #  '),('  # # #  '),('  # # #  '),('  ## ##  '),('  ## ##  '),('  #   #  '),('  #   #  '))
    k=(('  #   #  '),('  #   #  '),('  #  #   '),('  # #    '),('  ##     '),('  # #    '),('  #  #   '),('  #   #  '),('  #   #  '))
    dictionary={'l':l,'w':w,'k':k}
    screen=[' ']*9
    for j in range(9):
        for i in range(length):
            screen[j]=screen[j]+dictionary[string[i]][j]
        print screen[j]
    return screen

def main():
    name=raw_input('please exchange the order of lwk:')
    length=len(name)
    lwk(name,length)

main()






