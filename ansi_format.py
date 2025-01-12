def print_format_table():
	'''
	prints table of formatted text format options
	'''
	for style in range(8):
		#print(f'Start Loop {style}\n')
		#print(f'style = {style}\n')
		for fg in range(30, 38):
			#print(f'foreground in loop {fg-30} = {fg}\n')
			s1 = ''
			for bg in range(40, 48):
				#print(f'background in loop {bg-0} = {bg}\n')
				format = ';'.join([str(style), str(fg), str(bg)])
				s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
				#print('s1 = ', s1)
			print(s1)
		print('\n')


print_format_table()

