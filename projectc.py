import re # for removing spl char
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from PIL import Image
import speech_recognition as sr
from textblob import TextBlob

def want_sentiment():
    ws = input("Do you want get sentiment analysis? (Y/N)")
    return ws

def get_sentiment(q):
    text = q
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity >= -1 and polarity <=1:
        print("This content not available INDIA.. ")
    elif polarity == 0:
        return text
    elif polarity >= 1:
        return polarity
    
def voice_process(): 
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source,duration=2)
        print("Listening... Speak something!")
        audio = recognizer.listen(source)
    voice_text = recognizer.recognize_google(audio)   
    return voice_text


def show_image(file_name):
    imag = Image.open(f"D:/construction_bot/{file_name}.jpg")
    imag.show()    

def back_track(spl_char):
    with open(r"D:\construction_bot\unasnwered_question.txt",'a') as write_file:
        write_file.write(f"\n{spl_char}")
        print("your question much valued.. in future will develope answer for your all quires")
    return 'question noted'

def display_answer(question_id):
   
   result = get_answers(question_id)
   if result:
       print('your question:',result["title"])
       print('result:',result["answer"])
   else:
       print("Question not found")
   return ""


def get_answers(question_id):
  with open(r"D:\construction_bot\Construction_150_Answers_Converted.txt","r") as file:
        text = file.read()
  pattern = r"\[QUESTION_ID=(\d+)\]\s*TITLE=(.*?)\s*ANSWER=(.*?)(?=\n\[QUESTION_ID=|\Z)"
  matches = re.findall(pattern, text, re.DOTALL)
  answers = {}
  for qid, title, answer in matches:
       answers[qid] = {
       "title": title.strip(),
       "answer": answer.strip()
         }
  return answers.get(str(question_id), None)

def check_out (splited_words):
    
    check_out = ["construction","project","projects","building","buildings","work","works","activity","activities",
    "scope","process","procedure","method","methods","stage","stages","tender","pre_tender","post_tender",
    "bid","bidding","quotation","estimate","estimation","planning","schedule","scheduling","timeline",
    "milestone","cost","budget","pricing","rate","rates","quantity","quantitys","survey","surveying",
    "boq","contract","contracts","subcontract","subcontractor","vendor","vendors","site","sites",
    "execution","supervision","inspection","monitoring","procurement","purchase","purchasing",
    "material","materials","safety","quality","risk","compliance","drawing","drawings","plan","plans",
    "document","documents","report","reports","labour","wastage","qs",'recovery','planning','funding','management']

    filter_checkout = [word for word in splited_words if word.lower() in check_out]
    return filter_checkout

def check_in(splited_words):
    check = ["what","which","who","whose","where","when","why","how","is","are","am","was","were","do","does","did","has","have","had",
             "can","could","shall","should","will","would","may","might","must","show","give","tell","find","get","display","list",
             "explain","describe","define","provide","a","an","the","of","for","with","by","in","on","at","to","from",
             "into","onto","over","under","between","through","during","before","after","above","below","and","or","but","because","while","although",
             "i","you","he","she","it","we","they","me","him","her","us","them","my","your","his","their","our","this","that","these","those",
             "about","regarding","related","regards","information","details","data","record","records",
             "result","results","answer","answers","greater","less","more","higher","lower","maximum","minimum","highest","lowest",
             "best","top","least","equal","equals","exact","exactly","than","not","without","exclude","excluding"]
    filter_word = [word for word in splited_words if word.lower() not in check]
    return filter_word

c1 =  'project estimation'
c2 =  'labour requirement'
c3 =  'machinery requirement'
c4 =  'material types'
c5 =  'land types'
c6 =  'subcontract risk'
c7 =  'resource classification'
c8 =  'resource optimization'
c9 =  'material market price'
c10 = 'material wastage reduction'
c11 = 'qs site coordination'
c12 = 'daily progress tracking'
c13 = 'recovery planning'
c14 = 'funding management'
c15 = 'funding delay handling'
c16 = 'material quality'
c17 = 'vendor selection'
c18 = 'stock shortage'
c19 = 'inventory management'
c20 = 'damaged stock'
c21 = 'wage management'
c22 = 'monthly billing'
c23 = 'billing delay management'
c24 = 'boq preparation'
c25 = 'rate analysis'
c26 = 'quantity take off'
c27 = 'tender preparation'
c28 = 'tender evaluation'
c29 = 'contract review'
c30 = 'contract risk analysis'
c31 = 'project scheduling'
c32 = 'milestone planning'
c33 = 'critical path analysis'
c34 = 'cash flow planning'
c35 = 'budget monitoring'
c36 = 'cost variance analysis'
c37 = 'project profitability'
c38 = 'material procurement'
c39 = 'supplier management'
c40 = 'purchase order management'


resp = int(input(f"Hi How are you..!\n press 2 for typing..\n press 1 for voice process..! "))

if resp == 2:
   user_inp = input(f"Please type your query..") #user_input from keyboard
   lower_case = user_inp.lower() # converting into lower case
   spl_char = re.sub(r'[^a-zA-Z0-9 ]',"",lower_case) # removing extract symbols
   splited_words = spl_char.split()
   key = " ".join(check_in(splited_words))
   key1 = " ".join(check_out(splited_words))
   print('-'* 50)
   print('KEY IS===>',key)
   print('KEY1 IS===>',key1)
elif   resp ==1:
     user_inp=voice_process()   
     lower_case = user_inp.lower() # converting into lower case
     spl_char = re.sub(r'[^a-zA-Z0-9 ]',"",lower_case) # removing extract symbols
     splited_words = spl_char.split()
     key = " ".join(check_in(splited_words))
     key1 = " ".join(check_out(splited_words))
     print('-'* 50)
     print('KEY IS===>',key)
     print('KEY1 IS===>',key1)

if key =='project estimation':
    print('-'* 50)
    print('-' * 25,'GA NOT-IN condition:',key)
    question_id = 1
    ws1 = want_sentiment() # Y or N
    wslc = ws1.lower()
    if wslc =='y':
        q = display_answer(question_id)
        get_sentiment(q)
       # print('test:',q)
    else:  #Y
         #display_answer(question_id)
         None
elif key =='labour requirement':
    question_id = 2
    display_answer(question_id)
elif key =='machinery requirement' or key =='machine requirements':
     question_id = 3
     file_name = 3
     #display_answer(question_id)   
     show_image(file_name)
elif key =='material types':
     question_id = 4
     display_answer(question_id)   
elif key =='land types':
     question_id = 5
     display_answer(question_id)  
elif key =='subcontract':
     question_id = 6
     display_answer(question_id) 
elif key =='resource classification':
     question_id = 7
     display_answer(question_id)      
elif key =='resource optimization':
     question_id = 8
     display_answer(question_id)   
elif key =='material market price'or key =='market price':
     question_id = 9
     display_answer(question_id)   
elif key =='material wastage reduction'or key =='wastage reduction':
     question_id = 10
     display_answer(question_id)             
elif key =='qs site coordination'or key =='qs site':
     question_id = 11
     display_answer(question_id)  
elif key =='daily progress tracking'or key =='daily progress':
     question_id = 12
     display_answer(question_id)       
elif key =='recovery planning'or key =='planning':
     question_id = 13
     display_answer(question_id)       
elif key =='fund planning' or key =='funding':
     question_id = 14
     display_answer(question_id)       
elif key =='funding delay' or key =='delay':
     question_id = 15
     display_answer(question_id)     
elif key =='material quality' or key =='quality material':
     question_id = 16
     display_answer(question_id)
elif key =='vendor selection' or key =='selection vendor':
     question_id = 17
     display_answer(question_id)
elif key =='stock shortage handling' or key =='stock':
     question_id = 18
     display_answer(question_id)  
elif key =='inventory management' or key =='inventory':
     question_id = 19
     display_answer(question_id)   
elif key =='damaged stock' or key =='stock damage':
     question_id = 20
     display_answer(question_id)      
elif key =='wage management' or key =='manage wage':
     question_id = 21
     display_answer(question_id)     
elif key =='monthly billing' or key =='billing monthly':
     question_id = 22
     display_answer(question_id)
elif key =='billing delay' or key =='delay billing':
     question_id = 23
     display_answer(question_id)  
elif key =='boq preparation' or key =='boq':
     question_id = 24
     display_answer(question_id)           
elif key =='rate analysis' or key =='analysis rate':
     question_id = 25
     display_answer(question_id)  
elif key =='quantity take off':
     question_id = 26
     display_answer(question_id)   
elif key =='tender preparation':
     question_id = 27
     display_answer(question_id)   
elif key =='tender evaluation':
     question_id = 28
     display_answer(question_id)   
elif key =='contract review':
     question_id = 29
     display_answer(question_id) 
elif key =='contract risk analysis':
     question_id = 30
     display_answer(question_id) 
elif key =='project scheduling':
     question_id = 31
     display_answer(question_id) 
elif key =='milestone planning':
     question_id = 32
     display_answer(question_id)    
elif key =='critical path analysis':
     question_id = 33
     display_answer(question_id)    
elif key =='cash flow planning':
     question_id = 34
     display_answer(question_id)      
elif key =='budget monitoring':
     question_id = 35
     display_answer(question_id)   
elif key =='cost variance analysis':
     question_id = 36
     display_answer(question_id)    
elif key =='project profitability':
     question_id = 37
     display_answer(question_id)      
elif key =='material procurement':
     question_id = 38
     display_answer(question_id)           
elif key =='supplier management':
     question_id = 39
     display_answer(question_id)           
elif key =='purchase order management':
     question_id = 40
     display_answer(question_id) 
else:
    if key1 == 'estimation' or key == 'estimation project' or key1 =='project' or key =='construction estimation':
       question_id = 1
       display_answer(question_id)
    elif key1 == 'labour' or key1=='requirement' or key1 =='labour requirement overview'or key =='manpower'or key =='workforce'or key =='force':
         question_id =2
         display_answer(question_id)  
    elif key1 == 'machinery' or key1=='requirement' or key1 =='machinery requirement overview':
         question_id =3
         display_answer(question_id)       
    elif key1 == 'material' or key1=='type':
         question_id =4
         display_answer(question_id)  
    elif key1 == 'land' or key1=='type':
         question_id =5
         display_answer(question_id)      
    elif key1 == 'subcontract' or key1=='contract':
         question_id =6
         display_answer(question_id)     
    elif key1 == 'resource' or key1=='classification':
         question_id =7
         display_answer(question_id)    
    elif key1 == 'resource' or key1=='optimization':
         question_id =8
         display_answer(question_id)   
    elif key1 == 'market price' or key1=='material price':
         question_id =9
         display_answer(question_id)  
    elif key1 == 'material wastage' or key1=='Wastage Reduction':
         question_id =10
         display_answer(question_id) 
    elif key1 == 'qs site coordination' or key1=='qa coordination':
         question_id =11
         display_answer(question_id)    
    elif key1 == 'day process' or key1=='day tracking' or key1=='today process' or key1 =='day tracking' or key =='daily progress tracking overview':
         question_id =12
         display_answer(question_id)    
    elif key1 == 'recovery planning' or key1=='day tracking' or key1=='today process' or key1 =='day tracking' or key =='daily progress tracking overview':
         question_id =13
         display_answer(question_id) 
    elif key1 == 'funding overview' or key1=='funding management' or key1=='funding process':
         question_id =14
         display_answer(question_id)   
    elif key1 == 'funding delay' or key1=='fund delay':
         question_id =15
         display_answer(question_id) 
    elif key1 == 'material quality' or key1=='quality check':
         question_id =16
         display_answer(question_id)
    elif key1 == 'vendors' or key1=='outsource':
         question_id =17
         display_answer(question_id)  
    elif key1 == 'stock less' or key1=='shortage stock':
         question_id =18
         display_answer(question_id)   
    elif key1 == 'inventory overview' or key1=='storage':
         question_id =19
         display_answer(question_id)   
    elif key1 == 'damage stocks' or key1=='stocks damages':
         question_id =20
         display_answer(question_id)    
    elif key1 == 'wages' or key1=='manage wages':
         question_id =21
         display_answer(question_id)       
    elif key1 == 'month bill' or key1=='monthly bill' or key1=='bills monthly':
         question_id =22
         display_answer(question_id)
    elif key1 == 'billing delay' or key1=='delay bill':
         question_id =23
         display_answer(question_id)     
    elif key1 == 'boq' or key1=='preparation boq':
         question_id =24
         display_answer(question_id)      
    elif key1 == 'rate analysis' or key1=='analysis rate':
         question_id =25
         display_answer(question_id)   
    elif key1 == 'take off quantity' or key1=='off quantity':
         question_id =26
         display_answer(question_id) 
    elif key1 == 'tender preparation' or key1=='preparation tendor':
         question_id =27
         display_answer(question_id)  
    elif key1 == 'tender evaluation' or key1=='evaluation tendor':
         question_id =28
         display_answer(question_id)       
    elif key1 == 'review contract':
         question_id =29
         display_answer(question_id)
    elif key1 == 'contract risk analysis':
         question_id =30
         display_answer(question_id) 
    elif key1 == 'scheduling' or key1 =='schedule project':
         question_id =31
         display_answer(question_id)      
    elif key1 == 'milestone' or key1 =='planning milestone':
         question_id =32
         display_answer(question_id)
    elif key1 == 'critical path' or key1 =='path critical':
         question_id =33
         display_answer(question_id) 
    elif key1 == 'cash flow' or key1 =='flow cash':
         question_id =34
         display_answer(question_id)  
    elif key1 == 'budget monitor' or key1 =='monitor budget':
         question_id =35
         display_answer(question_id)  
    elif key1 == 'cost variance' or key1 =='variance cost':
         question_id =36
         display_answer(question_id)  
    elif key1 == 'project profitability' or key1 =='profitability project':
         question_id =37
         display_answer(question_id)
    elif key1 == 'procurement material' :
         question_id =38
         display_answer(question_id)  
    elif key1 == 'management supplier' :
         question_id =39
         display_answer(question_id) 
    elif key1 == 'management purchase order' or key1=='order purchase':
         question_id =40
         display_answer(question_id)                                                         
    else:
     print('-'* 50)
     print('-' * 25,'starting fuzzy..!')
     D1 = fuzz.WRatio(c1,key)
     D2 = fuzz.WRatio(c2,key)
     D3 = fuzz.WRatio(c3,key)
     D4 = fuzz.WRatio(c4,key)
     D5 = fuzz.WRatio(c5,key)
     D6 = fuzz.WRatio(c6,key)
     D7 = fuzz.WRatio(c7,key)
     D8 = fuzz.WRatio(c8,key)
     D9 = fuzz.WRatio(c9,key)
     D10 = fuzz.WRatio(c10,key)
     D11 = fuzz.WRatio(c11,key)
     D12 = fuzz.WRatio(c12,key)
     D13 = fuzz.WRatio(c13,key)
     D14 = fuzz.WRatio(c14,key)
     D15 = fuzz.WRatio(c15,key)
     D16 = fuzz.WRatio(c16,key)
     D17 = fuzz.WRatio(c17,key)
     D18 = fuzz.WRatio(c18,key)
     D19 = fuzz.WRatio(c19,key)
     D20 = fuzz.WRatio(c20,key)
     D21 = fuzz.WRatio(c21,key)
     D22 = fuzz.WRatio(c22,key)
     D23 = fuzz.WRatio(c23,key)
     D24 = fuzz.WRatio(c24,key)
     D25 = fuzz.WRatio(c25,key)
     D26 = fuzz.WRatio(c26,key)
     D27 = fuzz.WRatio(c27,key)
     D28 = fuzz.WRatio(c28,key)
     D29 = fuzz.WRatio(c29,key)
     D30 = fuzz.WRatio(c30,key)
     D31 = fuzz.WRatio(c31,key)
     D32 = fuzz.WRatio(c32,key)
     D33 = fuzz.WRatio(c33,key)
     D34 = fuzz.WRatio(c34,key)
     D35 = fuzz.WRatio(c35,key)
     D36 = fuzz.WRatio(c36,key)
     D37 = fuzz.WRatio(c37,key)
     D38 = fuzz.WRatio(c38,key)
     D39 = fuzz.WRatio(c39,key)
     D40 = fuzz.WRatio(c40,key)
     

     print("Fuzzy key is =",key)
     if D1 >= 90:
        print("Score",D1)
        print('fuzzy works')
        question_id = 1
        display_answer(question_id)
     elif D2 >= 90:
        print("Score",D2)
        question_id = 2
        display_answer(question_id)
     elif D3 >= 90:
        print("Score",D3)
        question_id = 3
        display_answer(question_id)  
     elif D4 >= 90:
        print("Score",D4)
        question_id = 4
        display_answer(question_id)   
     elif D5 >= 90:
        print("Score",D5)
        question_id = 5
        display_answer(question_id)      
     elif D6 >= 90:
        print("Score",D6)
        question_id = 6
        display_answer(question_id)      
     elif D7 >= 90:
        print("Score",D7)
        question_id = 7
        display_answer(question_id)   
     elif D8 >= 90:
        print("Score",D8)
        question_id = 8
        display_answer(question_id)    
     elif D9 >= 90:
        print("Score",D9)
        question_id = 9
        display_answer(question_id)       
     elif D10 >= 90:
        print("Score",D10)
        question_id = 10
        display_answer(question_id)      
     elif D11 >= 90:
        print("Score",D11)
        question_id = 11
        display_answer(question_id)    
     elif D12 >= 90:
        print("Score",D12)
        question_id = 12
        display_answer(question_id)  
     elif D13 >= 90:
        print("Score",D13)
        question_id = 13
        display_answer(question_id) 
     elif D14 >= 90:
        print("Score",D14)
        question_id = 14
        display_answer(question_id)  
     elif D15 >= 90:
        print("Score",D15)
        question_id = 15
        display_answer(question_id) 
     elif D16 >= 90:
        print("Score",D16)
        question_id = 16
        display_answer(question_id)    
     elif D17 >= 90:
        print("Score",D17)
        question_id = 17
        display_answer(question_id)  
     elif D18 >= 90:
        print("Score",D18)
        question_id = 18
        display_answer(question_id)       
     elif D19 >= 90:
        print("Score",D19)
        question_id = 19
        display_answer(question_id)   
     elif D20 >= 90:
        print("Score",D20)
        question_id = 20
        display_answer(question_id)
     elif D21 >= 90:
        print("Score",D21)
        question_id = 21
        display_answer(question_id)  
     elif D22 >= 90:
        print("Score",D22)
        question_id = 22
        display_answer(question_id)   
     elif D23 >= 90:
        print("Score",D23)
        question_id = 23
        display_answer(question_id) 
     elif D24 >= 90:
        print("Score",D24)
        question_id = 24
        display_answer(question_id)   
     elif D25 >= 90:
        print("Score",D25)
        question_id = 25
        display_answer(question_id)   
     elif D26 >= 90:
        print("Score",D26)
        question_id = 26
        display_answer(question_id)  
     elif D27 >= 90:
         print("Score",D27)
         question_id = 27
         display_answer(question_id)
     elif D28 >= 90:
         print("Score",D28)
         question_id = 28
         display_answer(question_id)
     elif D29 >= 90:
         print("Score",D29)
         question_id = 29
         display_answer(question_id)    
     elif D30 >= 90:
         print("Score",D30)
         question_id = 30
         display_answer(question_id)
     elif D31 >= 90:
         print("Score",D31)
         question_id = 31
         display_answer(question_id) 
     elif D32 >= 90:
         print("Score",D32)
         question_id = 32
         display_answer(question_id)  
     elif D33 >= 90:
         print("Score",D33)
         question_id = 33
         display_answer(question_id)  
     elif D34 >= 90:
         print("Score",D34)
         question_id = 34
         display_answer(question_id)
     elif D35 >= 90:
         print("Score",D35)
         question_id = 35
         display_answer(question_id) 
     elif D36 >= 90:
         print("Score",D36)
         question_id = 36
         display_answer(question_id)     
     elif D37 >= 90:
          print("Score",D37)
          question_id = 37
          display_answer(question_id)      
     elif D38 >= 90:
           print("Score",D38)
           question_id = 38
           display_answer(question_id)
     elif D39 >= 90:
           print("Score",D39)
           question_id = 39
           display_answer(question_id)  
     elif D40 >= 90:
           print("Score",D40)
           question_id = 40
           display_answer(question_id)          
     else:
        back_track(spl_char) 