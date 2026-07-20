#new try from the start

intakelist = [] #list of protein intake in the from of dictionary
print("Lets complete daily protein intake!")

while True:
    print("====MENU====")
    print("1. ADD protein intake")
    print("2. View protein intake")
    print("3. view total protein intake")
    print("4. Exit")

    choice= int(input("Choice your preference "))

    if(choice == 1):
        date= input("kis date ko?")
        time= input("kis time per?")
        grams= int(input("kitna gram protein intake kiya?"))
        
        intake= {
            "date": date,
            "time": time,
            "grams": grams
        }
        intakelist.append(intake)
        print("==saved successfull==")
    elif(choice== 2):
         if(len(intakelist)== 0) :
          print("no intakes done yet!")
         else:
            print("your protein intakes")
            count= 1
            for eachintake in intakelist:
                 print(f"Intake number {count} -> {eachintake["date"]}, {eachintake["time"], {eachintake["grams"]}}")
                 count= count + 1

    elif(choice== 3):
        total = 0
        for eachintake in intakelist:
            total = total + eachintake["grams"]
        
        print("AAPKA TOTALPROTEIN INTAKE HAI: ", total)

    elif(choice== 4):
        print("thanks for useing PROTEIN-INTAKE-TRACKER")

        break
    else:
        print("choose a valid option sir/ma'am!")
    

        
        