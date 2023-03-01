water=5000
milk=5000
sugar=3000
coffee=300
cup=50
totalBill=0
buych=1
fillch=1
mainch=1
lattetotalBill=0
espressototalBill=0
capachinototalBill=0

print("*----------------------------------------------------------------------------------------------------------------------*")
print("																											       ")
print("																											       ")
print("*___________________-------------------------WELCOME TO FRIENDS-COFFEE-SHOP-------------------------___________________*")
print("																											       ")
print("																											       ")
print("*----------------------------------------------------------------------------------------------------------------------*")
while(mainch==1):
    print("**************MENU************")
    print("*1. BUY  COFFEE              *")
    print("*2. FILL COFFEE              *")
    print("******************************")
    ch=int(input("Enter your choice:"))
    buych=1
    fillch=1
    if(ch==1):
        while(buych==1):
            print("*--------------------------------*")
            print("*1.Espresso    | 150Rs           *")
            print("*--------------------------------*")
            print("*2.Cappuccino  | 100Rs           *")
            print("*--------------------------------*")
            print("*3.Latte       | 120Rs           *")
            print("*--------------------------------*")
            chbuy=int(input("Enter your choice:"))
            if(chbuy==1):
                excup=int(input("Enter how many cups you want:"))
                water-=excup*50
                milk-=excup*100
                sugar-=excup*15
                coffee-=excup*5
                cup-=excup*1
                espressototalBill+=excup*150
                totalBill+=espressototalBill
                print("Your Espresso Coffee Bill=",espressototalBill)
                print("Your Total Coffee Bill=",totalBill)
            if(chbuy==2):
                capcup=int(input("Enter how many cups you want:"))
                water-=capcup*50
                milk-=capcup*100
                sugar-=capcup*10
                coffee-=capcup*4
                cup-=capcup*1
                capachinototalBill+=capcup*100
                totalBill+=capachinototalBill
                print("Your Cappuccino Coffee Bill=",capachinototalBill)
                print("Your Total Coffee Bill=",totalBill)
            if(chbuy==3):
                lacup=int(input("Enter how many cups you want:"))
                water-=lacup*60
                milk-=lacup*160
                sugar-=lacup*20
                coffee-=lacup*3
                cup-=lacup*1
                lattetotalBill+=lacup*120
                totalBill+=lattetotalBill
                print("Your Latte Coffee Bill=",lattetotalBill)
                print("Your Total Coffee Bill=",totalBill)
            buych=int(input("Do you Want To Continue Buy Coffee \n press 1 \n for exit 2"))
    if(ch==2):
        while(fillch==1):
            print("|-------------------------------|")
            print("| Iteam-Name   | Remaining Iteam|")
            print("|-------------------------------|")
            print("|1.Water       |          ",water,"|")
            print("|-------------------------------|")
            print("|2.Milk        |          ",milk,"|")
            print("|-------------------------------|")
            print("|3.Coffee      |           ",coffee,"|")
            print("|-------------------------------|")
            print("|4.Sugar       |          ",sugar,"|")
            print("|-------------------------------|")
            print("|5.Cup         |            ",cup,"|")
            print("|-------------------------------|")
            chfill=int(input("Enter your choice:"))
            if(chfill==1):
                print("Total Water is=5000 ml")
                print("Remaining Water is=",water)
                print("You Filling Water only=",(5000-water))
                fwater = int(input("Enter Filling Water:"))
                if(fwater<=(5000-water)):
                    water +=fwater
                    print("Your Total water =" , water)
                else:
                    print("You are filling water out of range")
            
                
            if(chfill==2):
                print("Total milk is=5000 ml")
                print("Remaining milk is=",milk)
                print("You Filling milk only=",(5000-milk))
                fmilk = int(input("Enter Filling milk:"))
                if(fmilk<=(5000-milk)):
                    milk +=fmilk
                    print("Your Total milk =" , milk)
                else:
                    print("You are filling milk out of range")

            if(chfill==3):
                print("Total coffee is=300 gm")
                print("Remaining coffee is=",coffee)
                print("You Filling coffee only=",(300-coffee))
                fcoffee = int(input("Enter Filling coffee:"))
                if(fcoffee<=(300-coffee)):
                    coffee+=fcoffee
                    print("Your Total coffee =" , coffee)
                else:
                    print("You are filling coffee out of range")

            if(chfill==4):
                print("Total sugar is=3000 gm")
                print("Remaining sugar is=",sugar)
                print("You Filling sugar only=",(3000-sugar))
                fsugar = int(input("Enter Filling sugar:"))
                if(fsugar<=(3000-sugar)):
                    sugar+=fsugar
                    print("Your Total sugar =" , sugar)
                else:
                    print("You are filling sugar out of range")
          
            if(chfill==5):
                print("Total cup is=50 ")
                print("Remaining cup is=",cup)
                print("You Filling cup only=",(50-cup))
                fcup = int(input("Enter Filling cup:"))
                if(fcup<=(50-cup)):
                    cup +=fcup
                    print("Your Total cup =" , cup)
                else:
                    print("You are filling cup out of range")
            fillch=int(input("Do you Want To Continue Filling Section:\n press 1 \n for exit press2"))
    mainch=int(input("Do you Want To Continue Main Section:\n press 1 \n for exit press2"))
    if(mainch==2):
        print("*-------------------------------------------------------------------------------------*")
        print("|___________----------**********THANK YOU FOR VISITING**********----------____________|")
        print("*-------------------------------------------------------------------------------------*")



