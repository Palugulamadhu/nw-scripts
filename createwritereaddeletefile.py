import os #module needed for deletion of file


#will create new madhu.txt file
f = open("madhu.txt" , "x")

#open the madhu.txt file in write mode
f = open("madhu.txt","w")
print ("Erasing content in file!!")
f.truncate() #will erase if any data exists inside filename

print("please enter the new lines:")

#script asks for data to be written to file
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Going to write new 3 lines to new.txt file:")

f.write(line1)
f.write("\n")
f.write(line2)
f.write("\n")
f.write(line3)
f.write("\n")
f.write("**** End of the file ****")

print("Now we'll readout new written lines")

#prints the output from madhu.txt file
f = open("madhu.txt" , "r")
print(f.read())
f.close()

#deletes the file madhu.txt once data is written
if os.path.exists("madhu.txt"):
    os.remove("madhu.txt")
else:
    print("The file doesn't exists!!!")



