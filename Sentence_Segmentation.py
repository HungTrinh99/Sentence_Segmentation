import re

def Sentence_Segmentation():
    with open("TextInput.txt",encoding="utf8") as file_in:
        text=file_in.read()
    text=text.replace('\n',' ')
    regex=re.compile('(?<=(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!Jr)[.!?])\s{1,2}(?=[A-ZẮẰẲẴẶĂẤẦẨẪẬÂÁÀÃẢẠĐẾỀỂỄỆÊÉÈẺẼẸÍÌỈĨỊỐỒỔỖỘÔỚỜỞỠỢƠÓÒÕỎỌỨỪỬỮỰƯÚÙỦŨỤÝỲỶỸỴ])')
    sentenceList=regex.split(text)
    i=1
    for sentence in sentenceList:
        print("Sentence ",i,":",sentence)
        i+=1

def main():
   print("Result")
   Sentence_Segmentation()

if __name__=="__main__":
    main()