# text='Hello wornuhijkgld\n'
# # r du w xie a zhuijia
# my_file=open("hhh.txt","a")
# my_file.write(text)
# my_file.close()

my_file=open("hhh.txt","r")
'''read'''
#content=my_file.read()
'''readline'''
# content_line = my_file.readline()
# print("content_line",content_line,end='\n')

'''readlines'''
content_lines = my_file.readlines()
for line in content_lines: #list
   print(line)
