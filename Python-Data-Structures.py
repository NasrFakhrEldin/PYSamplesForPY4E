# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ")
counter = 0
num = 0

try:
    fhandl = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

for line in fhandl:
    line = line.rstrip()

    if not "X-DSPAM-Confidence:" in line:
        continue

    atpost = line.find(':')
    numbers = float(line[atpost+1:])

    num += numbers
    counter += 1
print('Average spam confidence:', num/counter)


# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter File Name:")

try:
    fhandl = open(fname)

except:
    print("File cannot be opened:", fname)
    exit()

count = 0
for line in fhandl:
    line = line.rstrip()

    if not "From:" in line:
        continue
    li = line.split()

    count += 1
    print(li[1])
print("There were", count, "lines in the file with From as the first word")



# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


fname = input("Enter file:")

try:
    fhandl = open(fname)

except:
    print("File cannot be opened:", fname)
    exit()
    
counts = {}

for line in fhandl:
    line = line.rstrip()

    if not "From:" in line:
        continue

    line = line.split()
    lines = line[1]
    counts[lines] = counts.get(lines, 0) + 1

Maxvalue = None
Maxkey = None

for key, value in counts.items():
    if Maxvalue is None or Maxvalue < value:
        Maxvalue = value
        Maxkey = key

print(Maxkey, Maxvalue)





# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


fname = input("Enter File Name:")

try:
    fhandl = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = {}

for line in fhandl:
    line = line.rstrip()
    if not "From " in line:
        continue

    words  = line.split()
    t = words[5]
    time = t[:+2]
    counts[time] = counts.get(time,0) +1

li = []

for key, val in counts.items():
    li.append((key, val))
    li = sorted(li)
    
for key, val in li:
    print(key, val)
