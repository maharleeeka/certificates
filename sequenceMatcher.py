import difflib

def calculate(original, result):
    seq=difflib.SequenceMatcher(None, original, result)
    return seq.ratio()*100

i = 1

while (i <= 30):
    filename = "TEST_" + str(i)
    filename_r = filename+"_RESULTS"
    filename = filename+".txt"
    filename_r = filename_r+".txt"

    f = open(filename, "r")
    fr = open(filename_r, "w+")

    contents = f.read()
    contents = contents.split("\n")

    for content in contents:
        items = content.split("|")
        original = items[1]
        actual = items[2]
        accuracy = calculate(original, actual)
        fr.write(str(items[0]) + " " + str(accuracy) + "\n")
    
    print(filename + " ...done")
    
    f.close()
    fr.close()

    i = i + 1