a = [
    [1,2,3,4],
    [2,2,2,2],
    [3,4,2,3]
]

# for 按照行便利
#     FOR 按照列
#         i行j列的值

for i in range(0,len(a)):
    # for j in a[i]:
        # print(j,end=' ')
    for j in range(0,len(a[i])):
        print(a[i][j],end=' ')
    print('')
    