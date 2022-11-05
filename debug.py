data1 = ['React', 'Office', 'Public', 'Private', 'Classified', 'General', 'Downloads', 'Word File.doc', 'Excel File.doc']
data2 = ['react', 'office', 'public', 'private', 'classified', 'general', 'downloads', 'wordFile', 'excelFile']

data1 = str(data1).replace(' ', '').replace('.', '').replace('doc', '').lower()
data2 = str(data2).replace(' ', '').lower()

print(data1)
print(data2)

assert data1 == data2

