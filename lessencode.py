def recog(main, e):
    t = 0
    for i in main:
        if i in e:
            t += 1
    if t == len(main):
        return 'Yes'
    else:
        return 'No'
def under(string):
    e = []
    for i in string:
        e.append(i)
    e = list(dict.fromkeys(e))
    return e
numbers, main = input().split()
main = under(main)
listres = []
for i in range(0, int(numbers)):
    string = input()
    e = under(string)
    result = recog(main, e)
    listres.append(result)
for result in listres:
    print(result)