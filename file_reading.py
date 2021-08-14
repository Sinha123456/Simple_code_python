# with open('test.txt', 'r') as f:
#     file_data = f.read()
# print(file_data)
# with open('test.txt') as song:
#     print(song.read(2))
#     print(song.read(8))
#     print(song.read())
#reading lines in the file
# file_lines = []
# with open('test.txt') as f:
#     for line in f:
#         file_lines.append(line.strip()) #using strip to remove the new line
# print(file_lines)

'''Using function to open the file and print it'''

def create_list(filename):
    file_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            file_list.append(name)
    return file_list
file_list = create_list('test.txt')
for actor in file_list:
    print(actor)