filename = 'Level J _2 a side.pdf'
filename1 = 'abhifile.pdf'
directory = 'c:/abhi/kumonanswersheets/'

with open(directory + filename, 'rb') as myfile:
    with open(directory + filename1, 'wb') as someotherpersonsfile:
        mycontents = myfile.read()
        someotherpersonsfile.write(mycontents)
   

