def count_words_in_file(filename:str)->int:
    count=0
    sample_file=open(filename,"r")
    document=sample_file.readlines()

    for i in range (0,len(document)):
        line=document[i].split()
        count+=len(line)

    return count

print("Number of words in sample file: ",count_words_in_file("sample.txt"))