# python file_handling/fileHandling.py

def writeTextToFile():
    # Open a file in write mode
    with open('file_handling/filedata/example.txt', 'w') as file:
        file.write('Hello, World!\n')
        file.write('This is a file handling example.\n')

def  writingMultipleLinesToFile():
    # Open a file in write mode
    with open('file_handling/filedata/example.txt', 'w') as file:
        lines = ['Hello, World!\n', 'This is a file handling example.\n']
        file.writelines(lines)
        
def readingFromFile():
    # Open a file in read mode
    with open('file_handling/filedata/example.txt', 'r') as file:
        # Read the entire file
        content = file.read()
        print(content)
        
        # Read the file line by line
        file.seek(0)
        for line in file:
            print(line)
            
        # Read the file line by line
        file.seek(0)
        lines = file.readlines()
        for line in lines:
            print(line)

def main():
    writeTextToFile()
    writingMultipleLinesToFile()
    readingFromFile()
    
    
if __name__ == '__main__':
    main()