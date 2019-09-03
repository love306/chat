def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
def convert(lines):
	new = []
	person = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0.
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if '貼圖' in s[2:]:
				allen_sticker_count += 1
			elif '圖片' in s[2:]:
				allen_image_count += 1
			else:  
				for word in s[2:]:
					allen_word_count += len(word)

		elif name == 'Viki':
			if '貼圖' in s[2:]:
				viki_sticker_count += 1
			elif '圖片' in s[2:]:
				viki_image_count += 1
			else:
				for word in s[2:]:
					viki_word_count += len(word)
	print('allen說了', allen_word_count, '字')
	print('傳了', allen_sticker_count, '張貼圖')
	print('傳了', allen_image_count, '張圖片')
	print('viki說了', viki_word_count, '字')
	print('傳了', viki_sticker_count, '張貼圖')
	print('傳了', viki_image_count, '張圖片')

		#print(s)	
		
	return new
def write_file(filename,lines):
	with open(filename, 'w', encoding='utf-8') as d:
		for line in lines:
			d.write(line + '\n')
def main():
	filename = '-LINE-Viki.txt'
	lines = read_file('-LINE-Viki.txt')
	lines = convert(lines)
	#write_file(filename,lines)
main()