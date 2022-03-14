guests = {}

def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    val = yield line_data
    if val is not None:
      line_data = val

lst = read_guestlist('guest_list.txt')
for i in range(0, 10):
  print(next(lst))
lst.send('Jane,35')

# Outputs:
['Tim', '22']
['Tonya', '45']
['Mary', '12']
['Ann', '32']
['Beth', '20']
['Sam', '5']
['Manny', '76']
['Kenton', '15']
['Kenny', '27']
['Dixie', '46']