# to create a file object you can named it anyting

fw = open('sample.txt', 'w')
fw.write('writing some stuff in my text file\n')
fw.write('I like Fish\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
