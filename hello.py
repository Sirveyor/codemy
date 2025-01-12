
print("Hello World!\n")

''' Chapter Two Exercise
	1. Write some code that outputs more than one line of test to the 
		screen
'''
print("Chapter Two: Exc. 1.\n \
Hello\n World!")

'''Chapter Two Exercise
	2. Write a comment on the same line as another line of code.
'''
answer = 12 + 12 #this line adds 12 and 12 and assigns it to answer

print("Chapter Two Exc. 2. \n")
print(f'answer is {answer}\n')

'''
	Chapter Two Exercis4
	3. Write multi-line comment
'''
print("My multi-line comment is \n \
''' \n \
Chapter Two Exercise \n \
3. Write multi-line comment \n \
'''\n")

'''Chapter Two Excercise
	4. Write some code that creates an error, then google that error.
'''


code = '''
string \x1b[31m = \x1b[32m 'x34'\x1b[0m 
output \x1b[31m = \x1b[34m int\x1b[0m(string)
\x1b[34 print\x1b[0 (output)
'''
errmsg = '''Traceback (most recent call last):
  File \x1b[35m"/Users/covert/Dev/Learn/codemy/hello.py", \x1b[0m line\x1b[35m3 
  \x1b[0m in \x1b[35m <module>
    \x1b[0m output = int(string)
\x1b[35mValueError\x1b[0m:\x1b[35minvalid literal for int() with base 10: \'x34\'\x1b[0m'''

google = '''The error message means that the string provided to int could not
be parsed as an integer. The part at the end, after the :,
shows the string that was provided.'''

print("Chapter Two: Exc. 4.")
print(code)
print()
print(errmsg)
print("Google search -> stackoverflow:")
print(f'\x1b[31m{google}\x1b[0m')
#string = 'x34'
#Woutput = int(string)
#print(output)