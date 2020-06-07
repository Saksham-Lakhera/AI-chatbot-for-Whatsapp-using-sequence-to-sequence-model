import re
import emoji
def give_emoji_free_text(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])
    return clean_text

filenames = ["chat file name"]
for names in filenames:
    file_handle = open(names + ".txt")
    print(names + ".txt has been opened")
    f = open(names + "out.txt", 'w')
    for line in file_handle:
        line=line.replace("<Media omitted>", "")
        line=give_emoji_free_text(line)+"\n"
        
        temp = re.sub(r'.*-', '-', line)
        line = temp[2:]
        f.write(line)
        #print(line)
file_handle.close()

filenames = ["chat file name"]
cwboolean = True
othersboolean = True

for names in filenames:
	file_handle = open(names + "out.txt")
	print(names + "out.txt has been opened")
	fcw = open(names + "CW.txt", 'w')
	fothers = open(names + "sep.txt", 'w')
	for line in file_handle:
		if(line.startswith("user name as on chat file")):
			if(cwboolean):
				fcw.write("|\n")
				othersboolean = True
				cwboolean = False
			fcw.write(line)
		else:
			if(othersboolean):
				fothers.write("|\n")
				cwboolean = True
				othersboolean = False
			fothers.write(line)
		#print(line)
file_handle.close()

import re
filenames = ["chat file name"]

for names in filenames:
	file_handle = open(names + "sep.txt")
	print(names + ".txt has been opened")
	f = open(names + "OK.txt", 'w')
	for line in file_handle:
		if(line.startswith("|")):
			f.write(line)
		else:
			temp = re.sub(r'.*:', ':', line)
			line = temp[2:]
			f.write(line)

file_handle.close()

import re
filenames = ["chat file name"]

for names in filenames:
	file_handle = open(names + "CW.txt")
	print(names + ".txt has been opened")
	f = open(names + "CWOK.txt", 'w')
	for line in file_handle:
		if(line.startswith("|")):
			f.write(line)
		else:
			temp = re.sub(r'.*:', ':', line)
			line = temp[2:]
			f.write(line)

file_handle.close()

filenames = ["chat file name"]
cwcounter = 0
othercounter = 0
stringstore = ""

f = open("myside.txt", 'w')
fother = open("otherside.txt", 'w')
#column 0 and column 1, 0 Chunside 1 Ohter Side, row 0++
for names in filenames:
	cwfile = open(names + "CWOK.txt")
	otherfile = open(names + "OK.txt")

	print(names + ".txt QnA pair has been opened")
	for line in cwfile:
		if(line.startswith("|")):
			#s1.write(cwcounter, 0, stringstore)
			f.write(stringstore)
			cwcounter += 1
			stringstore = "\n"
		else:
			stringstore += " " + line.rstrip()
			#print(stringstore)
			
	for oline in otherfile:
		if(oline.startswith("|")):
			#s1.write(othercounter, 1, stringstore)
			fother.write(stringstore)
			othercounter += 1
			stringstore = "\n"
		else:
			stringstore += " " + oline.rstrip()
			#print(stringstore)
			#print(stringstore)
#print("Me:" + str(cwcounter) + " Other" + str(othercounter))

f = open("myside.txt", 'r')
fother = open("otherside.txt", 'r')
one=[]
two=[]
for line in fother:
    one.append(line)
for line in f:
    two.append(line)
print(len(one))
print(len(two))
f = open("data.txt", 'w')
for i in range(len(two)):
    f.write(two[i])
    f.write(one[i])
