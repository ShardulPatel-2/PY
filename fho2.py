file_read = open ('goon.txt', 'r')
print("File in read mode -")
print(file_read.read())
file_read.close()

file_write = open ('goon.txt', 'w')
file_write.write("I love gooning, GIMMIE GOOBY GOOO!!!!!!!!!!!!!!!!")
file_write.write("Jimmy Bablo is my favorite cricketer")
file_write.close()

file_append = open ('goon.txt', 'a')
file_append.write("\nFile in append mode:")
file_append.write("\nR.I.P Jimmy Bablo 2014 - 2024 june 7 (he was killed by the PAIN IN THE WAR HE FOUGHT FOR HIS LIFE AND IN THE END HE WON but at what cost?.......)")
file_append.close()