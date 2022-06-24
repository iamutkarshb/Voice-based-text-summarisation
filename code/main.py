import requests as req
import mail1
import scrapper
import handleFile
import text2voice as t2v
import scrapper
import x
from bs4 import BeautifulSoup 
import speech_recognition as sr
def final():
    print("Thank You. The program is starting now.")
    print("Choose from the following options")
    t2v.speechTrans("Thank You. The program is starting now.")
    t2v.speechTrans("Choose from the following options")
    print("Options -")
    print("1. Press 1 to search for data using voice search")
    print("2. Press 2 to summarized the existing text data")
    optionad=int(input())
    
    def stot():
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Speak......")
                audio = r.listen(source)
                try:
                    return r.recognize_google(audio)
                except Exception as e:
                    return "Voice not recognised Speak again"
                    exit(0)
        except:
            t2v.speechTrans("An error occured your microphone is not working")
            t2v.speechTrans("Write the topic")
            print("An error occured your microphone is not working")
            print("Write the topic")
            return str(input())
    t2v.speechTrans("Tell the topic")
    topic=stot()

    while topic=="Voice not recognised Speak again":
        t2v.speechTrans(topic)
        topic=stot()

    t2v.speechTrans("You spoke "+str(topic))
    print("You spoke "+str(topic))
    t2v.speechTrans("Press 1 to confirm the topic or press 0 to restart")
    print("1. Press 1 to confirm the topic \n2. Press 0 to restart \nChoice: ")
    inp=int(input())
    while (inp!=1):
        t2v.speechTrans("Tell the topic")
        topic=stot()
        t2v.speechTrans("You spoke "+str(topic))
        print("You spoke "+str(topic))
        t2v.speechTrans("Press 1 to confirm the topic or press 0 to restart")
        print("1. Press 1 to confirm the topic \n2. Press 0 to restart \nChoice: ")
        inp=int(input())
    
    if(optionad==1):
        data=scrapper.get(topic)
    if(optionad==2):
        t2v.speechTrans("Please confirm that the data to summarized the existing text data available in the file \"text-for-summarization\"")
        print("1. Press 1 to confirm that the data to summarized the existing text data available in the file \"text-for-summarization\"")
        ink=int(input())
        while (ink!=1):
            print("Press 1 to confirm that the data to summarized the existing text data available in the file \"text-for-summarization.txt\"")
            t2v.speechTrans("Please confirm that the data to summarized the existing text data available in the file \"text-for-summarization.txt\"")
            ink=int(input())
        with open('text-for-summarization.txt') as f:
            data = f.read()
    

    if len(data)==0:
        print("No infomation related to this topic can be found. Please try with a different topic")
        t2v.speechTrans("No infomation related to this topic can be found. Please try with a different topic")
        exit(0)

    print("Data Scrapped Successfully")
    t2v.speechTrans("Data Scrapped Successfully")

    print("Scarapped Data - \n",data)

    t2v.speechTrans("Choose from the following options")
    print("Options -")
    print("1. Press 1 for storing the summarized data in text file")
    print("2. Press 2 for getting it mailed to your mail id")
    print("3. Press 3 for printing the summarized text")
    print("4. Press 4 for speech output of summarized text")
    option=int(input())

    t2v.speechTrans("You Choose "+str(option))

    s=x.summarize(data)

    if(option=="1" or option=="one" or option==1):
        t2v.speechTrans("Storing the summarized data in text file, Check Results folder.")
        print("Storing the summarized data in text file, Check Results folder.")
        t2v.speechTrans(handleFile.CreateFile(s,topic))

    if(option==2 or option=="two" or  option=="2"):
        status=handleFile.CreateFile(s,topic)
        if status=="File Successfully Written":
            print("Attachment successfully created")
            t2v.speechTrans("Attachment successfully created")
        else:
            print("Some Problem Occured")
            t2v.speechTrans("Some Problem Occured")
        t2v.speechTrans(mail1.sendMail(topic))

    if (option==3 or option=="two" or  option=="3"):
        print(s)

    if (option==4 or option=="two" or  option=="4"):
        t2v.speechTrans(s)