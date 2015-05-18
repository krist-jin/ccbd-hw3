import os

path = "D:/CS/Course/cloud/homework/a3/sentiment-output"
fout = open("sentiment-output.txt", "w")

def main():
    files = os.listdir(path)
    for fname in files:
        print fname
        fin = open(path+"/"+fname, "r")
        for line in fin:
            fout.write(line)
        fin.close()
    fout.close()

if __name__ == '__main__':
    main()