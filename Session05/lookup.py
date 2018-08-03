teencode = {
    "hc": "Học",
    "ng": "người",
    "pt": "phát triển", 
    "eny": "em người yêu",
    "any": "anh người yêu",
    "ns": "nói",
    "ngta": "người ta",
    "lm": "làm",
    "r": "rồi",
    "stt": "status"
}

loop = True
while loop:
    for key in teencode.keys():
        print(key, end=" ")

    your_code=input("Your code? ")
    print("*"*20)
    if your_code in teencode:
        print("Translation: ", teencode[your_code])
    else:
        print("Not found, do you want to contribute this word? ")
        answer=input("Y/N? ").upper()
        if answer=="Y":
            newtranslation=input("Enter your translation: ")
            teencode[your_code] = newtranslation
            print(teencode)
            print("Updated")
        else: 
            loop = False 
    print("*"*20)


    
        
