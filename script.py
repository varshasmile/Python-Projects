# my_file = open("text.txt")

# # print(my_file)
# # print(my_file.read())
# # my_file.seek(0)
# # print(my_file.read())
# # my_file.seek(0)
# # print(my_file.read())
# print(my_file.readlines())

# my_file.close()


with open("text.txt", mode = 'r+') as my_file:
	text = my_file.write("heyyyyy")
	print(text)


with open("happy.txt", mode = 'w') as my_file:
	text = my_file.write(":)")
	print(text)