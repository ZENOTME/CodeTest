#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import time
if not os.path.isfile('/home/dong/CodeTest/moudle/main.cpp'):
    main=open('/home/dong/CodeTest/moudle/main.cpp','w')
    main.write('#include <iostream>\n')
    main.write('using namespace std;\n')
    main.write('int main()\n')
    main.write('{\n')
    main.write('\n')
    main.write('}')
    main.close()


main=open('/home/dong/CodeTest/moudle/main.cpp')
content=main.read()
main.close()


main=open('/home/dong/CodeTest/moudle/main.cpp','w')
print('****Write your code inside main function****')
#add code
strsum='\n'
str=''
while not str=='\n':
     str=sys.stdin.readline()
     strsum=strsum+str

pos=content.find('{\n')
new_content=content[:pos+1]+strsum+content[pos+1:]

main.write(new_content)
main.close()

#complie
os.system('g++  /home/dong/CodeTest/moudle/main.cpp -o /home/dong/CodeTest/moudle/a.out')
output=os.popen('/home/dong/CodeTest/moudle/a.out')
print(output.read())
os.system('rm /home/dong/CodeTest/moudle/main.cpp')
os.system('rm /home/dong/CodeTest/moudle/a.out')

