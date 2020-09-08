
# pip install pyfiglet
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Travel-Diary!!")
print(ascii_banner)


balance = 5000
comp_thng = ("tents , rope , tourch, pair-of-clothes")
credential = {"John" : "123a", "Jack" : "456b" , "abc" : "789a"}
success = False
for i in range(3):
    username = input("please enter your username: ")
    password = input("please enter your password: ")
    if (credential.get(username) == password):
        print("----------login Succeeded------------")
        success = True
        if success == True:
            print("!!!!-TRAVELLING WOULD BE THE BEST IN-!!! ")
            print('Jammu&Kashmir -press 1:\n')
            print('Kerala -press 2:\n')
            print('Maharashtra -press 3:\n')
            print('Meghalaya -press 4:\n')
            option=int(input('select your state: '))
            if option==1:
                print("Great Choice")
                print("Jammu and Kashmir was a region formerly administered by India as \na state from 1954 to 2019, constituting the southern and southeastern portion of\nthe larger Kashmir region, which has been the subject of a dispute between India, \nPakistan and China since the mid-20th century")
                print()
                print('Complusary things before packing bag :',comp_thng,'\n')
                ascii_banner = pyfiglet.figlet_format("Jammu&Kashmir")
                print(ascii_banner)

                break
            elif option==2:
                print('Great choice')
                print('Natural beauty: Kerala the land of beauty is describes as the favourite \nchild of nature, and famous for its breath-taking natural beauty. Major attraction \nare includes long coconuts tree, the blue mountain and rivers makes Kerala one of the greenest places ever seen.')
                print()
                print('Complusary things before packing bag :', comp_thng, '\n')
                ascii_banner = pyfiglet.figlet_format("kerala")
                print(ascii_banner)

                break
            elif option==3:
                print('Great choice!!')
                print('Maharashtra can also be called the land of scholars, saints and actors as many of the \npeople from Maharashtra have succeeded in the fields mentioned above. \nMaharashtra is known for its purogami culture (forward culture).\nMaha means big and Rashtra means nation.')
                print()
                print('Complusary things before packing bag :', comp_thng, '\n')
                ascii_banner = pyfiglet.figlet_format("Maharashtra")
                print(ascii_banner)
                break
            elif option==4:
                print('Great choice!!')
                print('Meghalaya (Abode of Clouds in Sanskrit) is one of the seven Northeastern states of India.\nFamous for its high rainfall, subtropical forests and biodiversity, \nit is abutted by Assam in the north and east and by Bangladesh in the south.')
                print()
                print('Complusary things before packing bag :', comp_thng, '\n')
                ascii_banner = pyfiglet.figlet_format("--Megalaya--")
                print()
                print(ascii_banner)
                ascii_banner = pyfiglet.figlet_format("Food")
                print(ascii_banner)
                print("-----------------------")
                user_req = (input('veg or non-veg : '))
                if user_req==('nonveg'):
                    print("--[complusary food in bag]--")
                    print("[Beef Jerky and Dried Meat, Powdered Eggs]\n")
                else:
                    print("--[complusary food in bag]--")
                    print('[cup maggi ,Powdered Milk, Nuts and Seeds]\n')

                ascii_banner = pyfiglet.figlet_format('Guide')
                print(ascii_banner)
                chck_tb=(input("To check TimeTable for trek (y/n):  "))
                if chck_tb == ('y'):
                    print("-----TRAVEL DIARY------")
                for i in range(1):
                    print(i, end=" \t")
                    print("----Eat-------Sleep------Travel\n"
                          "1) Bus -- Travel \n"
                          "2) Treak-- to --Hill\n"
                          "3) Camp -- side --river\n ")
                    print('----------------------------------------')
                    print()
                    ascii_banner = pyfiglet.figlet_format("Save Money")
                    print(ascii_banner)
                    x=(input("Did you take any private car to reach here? (y/n):  "))
                    if x==("y"):
                        print('ok')
                    elif x==("n"):
                        print("Good you save atleast 100-200")

                    y=(input("food you carried was from outside (y/n):  "))
                    if y==("y"):
                        print('ok')
                    elif y==("n"):
                        print("Good you save atleast 100-200")

                    z=(input("Did you shop any items? (y/n):  "))
                    if z==("y"):
                        print(" ok")
                    elif z==("n"):
                        print("Good you save atleast 100-200!!!! ")
                    widhdrawl = float(input('How much total cost [100, 200, 500 , 2000]:  '))
                    if widhdrawl in [100, 200, 500, 2000]:
                        balance = balance - widhdrawl
                        print('You Saved:  ', balance,'\n')


            ascii_banner = pyfiglet.figlet_format('Helpline No.')
            print(ascii_banner)
            print("HelpLine No = 911")
            break
        else:
            print("Thank you")


    else:
        print("Login Failed")
    if not success:
        print("\n please try again in 10 minutes!")


