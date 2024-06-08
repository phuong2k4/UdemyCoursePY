

# write file use mode 'w' mean: write
# file = open("ExDay24/text.txt", mode='w')
# file.write("The only one who person who can!")

# add line use mode 'a' mean: add
# file = open("ExDay24/text.txt", mode='a')
# file.write("\nIm the best. ")

# Ways first
# file = open(".../text.txt")
# readF = file.read()
# print(readF)
# file.close()

# Ways second
# with open("ExDay24/text.txt") as f:
#     read = f.read()
#     f.close()
#     print(read)


replaces = "[name]"

with open("ExDay24/Input/Name/Starting_Name.txt") as FileName:
    names = FileName.readlines()


with open("ExDay24/Input/Letter/Starting_Letter.txt") as FileLetter:
    letter = FileLetter.read()
    for name in names:
        strip = name.strip()
        replace_letter = letter.replace(replaces, strip)
        with open(f"ExDay24/Output/ReadyToSend/readyToSend_to_{strip}.txt", mode='w') as FileSend:
            complete = FileSend.write(replace_letter)