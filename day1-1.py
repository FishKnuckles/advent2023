f = open('day1.txt', 'r')
data = f.read().split()
f.close()
numlist = []
for line in data:
  # print(line)
  for char in line:
    if ord(char) >= ord('0') and ord(char) <= ord('9'):
      first = char
      break
  for i in range(len(line)-1, -1, -1):
    if ord(line[i]) >= ord('0') and ord(line[i]) <= ord('9'):
      last = line[i]
      break
  numlist.append(int(first + last))
  
print(sum(numlist))
