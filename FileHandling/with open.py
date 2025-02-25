with open ('C:/Users/avnee/OneDrive/Desktop/Python Practice/FileHandling/monday.text','a') as avi:
    print(avi.tell())
    print(avi.writelines(['\n hello\n','world']))
