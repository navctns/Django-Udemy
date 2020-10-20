import textract
# text = textract.process("sample.doc")
# print(text)

a = 'asddddd'

s = 'asdddfactooopactfactdddfact'
l = len(s)

for i in range(l+1):
    if s[i:i+4] == 'fact':
        print('yes')