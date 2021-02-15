Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> immport os
SyntaxError: invalid syntax
>>> import os
>>> os.getcwd()
'C:\\Users\\vedant\\AppData\\Local\\Programs\\Python\\Python38-32'
>>> os.chdir('../../../../../')
>>> os.getcwd()
'C:\\Users\\vedant'
>>> os.chdir('C:\\Users\\vedant\\desktop')
>>> os.getcwd()
'C:\\Users\\vedant\\desktop'
>>> try:
	data = open('missing.txt')
	print(data.readline() , end='')
except IOError:
	print('file error')
finally:
	data.close()

	
file error
Traceback (most recent call last):
  File "<pyshell#17>", line 7, in <module>
    data.close()
NameError: name 'data' is not defined
>>> try:
	data = open('missing.txt')
	print(data.readline() , end='')
except IOError:
	print('file error')
finally:
	in 'data' in locals:
		
SyntaxError: invalid syntax
>>> try:
	data = open('missing.txt')
	print(data.readline() , end='')
except IOError:
	print('file error')
finally:
	fn 'data' in locals:
		
SyntaxError: invalid syntax
>>> try:
	data = open('missing.txt')
	print(data.readline() , end='')
except IOError:
	print('file error')
finally:
	if 'data' in locals:
		data.close()

		
file error
Traceback (most recent call last):
  File "<pyshell#22>", line 7, in <module>
    if 'data' in locals:
TypeError: argument of type 'builtin_function_or_method' is not iterable
>>> try:
	data = open('missing.txt')
	print(data.readline() , end='')
except IOError:
	print('file error')
finally:
	if 'data' in locals():
		data.close()

		
file error
>>> try:
	data = open('missing.txt')
	print(data.readline() , end='')
except IOError as err:
	print('file error:' + str(err))
finally:
	if 'data' in locals():
		data.close()

		
file error:[Errno 2] No such file or directory: 'missing.txt'
>>> 