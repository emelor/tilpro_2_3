# -*- coding: utf-8 -*-

import io


          

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
        glosa = io.glosvektor.pop()
        print glosa.word
        translations = glosa.translation;
        answer = raw_input("Vad är översättningen? ")
        print "'"+str(translations) + "'" + str(answer) + "'"
        io.glosvektor.insert(0,glosa)

        if answer in translations:
            print "Rätt svar"
            numberCorrect = numberCorrect + 1

        else:
            for translation in translations:
                almostCorrect(translation, answer)
    if (float(numberCorrect)/quizLength) >= io.passScore:
        print str(numberCorrect) + ", " + str(quizLength) + ", " + str(io.passScore)
        print "Grattis, quiz godkänt"
    else:
        print str(numberCorrect) + ", " + str(quizLength) + ", " + str(io.passScore), ", " + str(float(numberCorrect)/quizLength), ", " + str((float(numberCorrect)/quizLength) >= io.passScore)
        print "Underkänt, försök igen"
    
            
    
    

quizLength = io.fetchSettings("quiz.conf")
quiz(quizLength)
