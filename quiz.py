# -*- coding: utf-8 -*-
glosvektor  = []
quizLength = 0
passScore = 0
def fetchSettings(file):
    global glosvektor
    global quizlength
    global passScore
    i = 0
    for line in open(file):
        if line[0]!="#" and line[0]!=" ":
            print line
            key,value=line.split("=")
            key = key.strip()

            if key == "Procent rätt":
                passScore = value.strip()
            
            
            if key=="Fil(er)":
                for i in value.split(","):
                    readWords(i.strip())
    
            if key=="Antal frågor":
                quizLength = value.strip()
                return int(quizLength)

class nyGlosa:
    
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation

          
def readWords(glosor):
    for line in open(glosor):
        if line[0]!="#":
            word,translations = line.split("=")
            ary = []
            for trans in translations.split(","):
                ary.append(trans.strip())
            glosa = nyGlosa(word, ary)
            glosvektor.append(glosa)

def almostCorrect(translation, answer):
    if len(translation) == len(answer):
            i = 0
            while i < len(translation) - 1:
                if translation[i] == answer[i + 1] and answer[i] == translation[i + 1]:
                    print "Nästan rätt, rätt svar är " + str(translation)
                i += 1
                
            


def quiz(quizLength):
    print "QUIZ" + str(quizLength)
    numberCorrect = 0
    for r in range (quizLength):
        glosa = glosvektor.pop()
        print glosa.word
        translations = glosa.translation;
        answer = raw_input("Vad är översättningen? ")
        print "'"+str(translations) + "'" + str(answer) + "'"
        glosvektor.insert(0,glosa)

        if answer in translations:
            print "Rätt svar"
            numberCorrect = numberCorrect + 1

        else:
            almostCorrect(translations, answer)
    if (float(numberCorrect)/quizLength >= passScore):
        print str(numberCorrect) + ", " + str(quizLength) + ", " + str(passScore)
        print "Grattis, quiz godkänt"
    else:
        print "Underkänt, försök igen"
    
            
    
    

quizLength = fetchSettings("quiz.conf")
quiz(quizLength)
