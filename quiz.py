# -*- coding: utf-8 -*-
glosvektor  = []
quizLength = 0
def fetchSettings(file):
    i = 0
    for line in open(file):
        if line[0]!="#" and line[0]!=" ":
            print line
            key,value=line.split("=")
            key = key.strip()
            
            if key=="Procent rätt":
                passScore=value.strip
        
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
            word,translation = line.split("=")
            glosa = nyGlosa(word, translation)
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
    for r in range (quizLength):    
        glosa = glosvektor.pop()
        print glosa.word
        translation = (glosa.translation).strip();
        answer = raw_input("Vad är översättningen? ")
        print "'"+str(translation) + "'" + str(answer) + "'"
        glosvektor.insert(0,glosa)

        if answer == translation:
            print "Rätt svar"

        else:
            almostCorrect(translation, answer)
            
    
    

quizLength = fetchSettings("quiz.conf")
quiz(quizLength)
