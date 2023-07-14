file1 = open('start.txt', 'r')
file2 = open('finish.txt', 'r')
start = file1.readlines()
# print(start)
finish = file2.readlines()
data = ['Srimanth\n', 'Praveen\n']

for x in data:
    si = (start.index(x))
    stime = start[si + 1].strip()

    fi = (finish.index(x))
    ftime = finish[fi + 1].strip()

    att = ((int(ftime) - int(stime)) * 100) / 60
    print('{0} - Attendence Percentage = {1}'.format(x, str(att)))
