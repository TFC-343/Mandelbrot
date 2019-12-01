# code by TFC(James Packham)
# 28-11-2019
#

# well, this code isn't perfect but i'll try to break down what i was thing when i wrote it


def complex_maths_float(string1, string2, operation='add'):
    # string1 and string2 are the 2 complex numbers we need to do maths to

    #

    if string1 == string1.split('+')[0]:
        string1 = string1.split('-')
        string1[1] = '-'+string1[1]
    else:
        string1 = string1.split('+')

    if string2 == string2.split('+')[0]:
        string2 = string2.split('-')
        string2[1] = '-' + string2[1]
    else:
        string2 = string2.split('+')

    # ^^^ sets up the code to use the correct syntax with negative numbers

    # more syntax with negative numbers

    if string1[0] == '':
        string1.pop(0)
        string1[1] = '-'+string1[1]
    if string2[0] == '':
        string2.pop(0)
        string2[1] = '-' + string2[1]

    # if it has an 'e' in it just pretend it doesn't
    # (i think this is what makes it not work as it means
    # really small numbers act as normal sized and really big numbers act normals sized making
    # my code think that it is or isn't in the set where it should be the opposite)
    # \/ \/ \/

    try:
        float(string1[0])
        float(string2[0])
    except ValueError:
        string1[0] = string1[0][:-1]
        string2[0] = string2[0][:-1]

    #

    # adds minuses or times what ever it is given

    if operation == 'add' or operation == '+':
        out = str(float(string1[0])+float(string2[0]))+'+'+str(float(string1[1][:-1])+float(string2[1][:-1]))+'i'
    if operation == 'subtract' or operation == '-':
        out = str(float(string1[0])-float(string2[0]))+'+'+str(float(string1[1][:-1])-float(string2[1][:-1]))+'i'
    if operation == 'multiply' or operation == 'times' or operation == '*' or operation == 'x':
        # this one is a little messy but does the trick
        a = float(string1[0])*float(string2[0])
        b = float(string1[0]) * float(string2[1][:-1])
        c = float(string2[0]) * float(string1[1][:-1])
        d = float(string1[1][:-1]) * float(string2[1][:-1])

        out = str(a-d)+'+'+str(b+c)+'i'

    # output the correct syntax with minus numbers

    out = out.replace('+-', '-')
    return out


# just compares 2 complex numbers
def comparative(string1, string2, operation):

    if string1 == string1.split('+')[0]:
        string1 = string1.split('-')
        string1[1] = '-'+string1[1]
    else:
        string1 = string1.split('+')

    if string2 == string2.split('+')[0]:
        string2 = string2.split('-')
        string2[1] = '-' + string2[1]
    else:
        string2 = string2.split('+')

    if string1[0] == '':
        string1.pop(0)
        string1[1] = '-'+string1[1]
    if string2[0] == '':
        string2.pop(0)
        string2[1] = '-' + string2[1]

    try:
        float(string1[0])
        float(string2[0])
    except ValueError:
        string1[0] = string1[0][:-1]
        string2[0] = string2[0][:-1]

    if operation == '>':
        a, b = 0, 0
        if float(string1[0]) > float(string2[0]):
            a = 1
        if float(string1[1][:-1]) > float(string2[1][:-1]):
            b = 1
        # print(a+b)
        return a+b

    if operation == '<':
        a, b = 0, 0
        if float(string1[0]) < float(string2[0]):
            a = 1
        if float(string1[1][:-1]) < float(string2[1][:-1]):
            b = 1
        return a+b  # this will out put a 1 if only 1 part of the
                    # complex number in string2 is bigger or smaller than string1
