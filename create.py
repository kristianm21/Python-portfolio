#The purpose of our code is for the user to participate in a beauty pageant in which they are given a theme they have to follow. The more on theme the outfit, the more points the user receives.

#Initialize
import random
import time
import webbrowser
global themes
global xp
global urls
themes=["Old Money", "Beach Day", "Red Carpet", "Gothic", "Slumber Party", "Office Wear"] #Outfit Themes the user can either choose from or randomize
xp=0
urls=["https://photos.fife.usercontent.google.com/pw/AP1GczPmSuzWb7yYhCm7z5ffQb9h6T2BE_rKy5Oczjuvasmd6cqZ8_mjZps6=w512-h911-s-no-gm?authuser=0",
      "https://photos.fife.usercontent.google.com/pw/AP1GczPBZqMG499UcoGcL4nJJquNDERLX1XBZvjJcpi2qy9WAoZvvudTGwyY=w512-h911-s-no-gm?authuser=0",
      "https://photos.fife.usercontent.google.com/pw/AP1GczNUhTMvPl1kcEfriktFtTV0eI-qON9AK728yfkOBZ3RtSKJZefXU-32=w512-h911-s-no-gm?authuser=0"
      ] #The images that give clothing options for the user to choose from
shirts=["1", "2", "3", "4", "5", "6"] #Numbered shirt options
bottoms=["1", "2", "3", "4", "5", "6"] #Numbered bottoms options
shoes=["1", "2", "3", "4", "5", "6"] #Numbered shoes options
filter=[] #Blank array for filtering data

#Functions
def lobby(options):#Where the user chooses where to begin (rules or begin game automatically)
    global theme_input
    global theme
    if options=="New Game":#Brings user to the game automatically if parameter is "New Game"
        theme_input=input("""Would you like to pick your theme or randomize it?:
                  1. Choose
                  2. Randomize
                          -> """)
        if theme_input=="1":#The user chooses a theme
                theme_input=input("""What would like your theme to be? Pick a number:
                      1. Old Money
                      2. Beach Day
                      3. Red Carpet
                      4. Gothic
                      5. Slumber Party
                      6. Office Wear
                                  -> """)
                print("Theme chosen! Have fun.")
                theme=theme_input#Where the theme is stored
                game()
        elif theme_input=="2":
                random_game()
    elif options=="Rules":
        rules()

def random_game(): #Randomizes a theme for the user
    global themes
    global theme
    print("The theme is")
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    theme=random.choice(themes) #Where the theme is stored
    print(theme)
    game()

def game(): #The actual game: Where the user picks the clothes and builds an outfit according to the theme
    global themes
    global theme
    global urls
    time.sleep(1)
    webbrowser.open(urls[0]) #Opens image with shirt options
    shirt_choice=input("Please a number 1-6 corresponding to the shirt you'd like to pick that matches your theme: ") #User chooses a shirt option
    for i in range(len(shirts)): #Loop: Goes into the shirts index
        if shirt_choice in shirts[i]:
            filter.append(shirts[i]) #Adds shirt option to the filtered array
    time.sleep(1)
    webbrowser.open(urls[1]) #Opens image with bottom options
    bottoms_choice=input("Please a number 1-6 corresponding to the bottoms you'd like to pick that matches your theme: ") #User chooses a bottom option
    for i in range(len(bottoms)): #Loop: Goes into the bottoms index
        if bottoms_choice in bottoms[i]:
            filter.append(bottoms[i]) #Adds bottom option to the filtered array
    time.sleep(1)
    webbrowser.open(urls[2]) #Opens image with shoe options
    shoes_choice=input("Please a number 1-6 corresponding to the shoes you'd like to pick that matches your theme: ") #User chooses a shoe option
    for i in range(len(shoes)): #Loop: Goes into the shoes index
        if shoes_choice in shoes[i]:
            filter.append(shoes[i]) #Add shoe option to the filtered array
    print(filter) #Prints the final three options

    if theme=="1" or theme==themes[0]:
        scoring(themes[0])
    elif theme_input=="2" or theme==themes[1]:
        scoring(themes[1])
    elif theme_input=="3" or theme==themes[2]:
        scoring(themes[2])
    elif theme_input=="4" or theme==themes[3]:
        scoring(themes[3])
    elif theme_input=="5" or theme==themes[4]:
        scoring(themes[4])
    elif theme_input=="6" or theme==themes[5]:
        scoring(themes[5]) #Opens scoring function based on theme

def scoring(theme):
    global themes
    global xp
    for i in range(len(themes)):
        if theme in themes[i]:
            if filter[0]==filter[1]:
                if filter[1]==filter[2]:
                    xp=xp+150
                else:
                    xp=xp+100
            elif filter[0]==filter[2]:
                if filter[2]==filter[1]:
                    xp=xp=150 #Adds 150 points to total score if 3/3 options are equal
                else:
                    xp=xp+100 #Adds 100 points to total score if 2/3 options are equal
            elif filter[1]==filter[2]:
                if filter[2]==filter[0]:
                    xp=xp+150 #Adds 150 points to total score if 3/3 options are equal
                else:
                    xp=xp+100 #Adds 100 points to total score if 2/3 options are equal
            else:
                xp=xp+0 #Adds 0 points if 0/3 options are equal

#Ultimate scoring based on options in relation to the theme
#Loop: Goes into the themes index
#Adds 150 points to total score if 3/3 options are equal
#Adds 100 points to total score if 2/3 options are equal

    print(f"Your final score is {xp}! Thank you for participating!") #Provides final score

def rules(): #The rule guide: One of the options for the parameter
    print("""Welcome to the Beauty Pageant! Here, your fashion skills will be put to the test.

          In order to participate in our pageant, here are some things to know:
          You will be provided with a random theme and you must build an outfit from the options shown to best match the theme.
          You must choose the article of clothing by inputting the number corresponding with the item.
          The more on theme your outfit is, the more points you will receive.
          The more points you have, the higher your level will be.""")
    time.sleep(2)
    lobby("New Game") #Opens the game after rules are given

#Main
lobby("Rules")

#Source Info/credits:
#Shirt 1:
#Website name: Old Money
#URL: https://old-money.com/products/classic-chich-shirt
#Name of item: Classic Chic Shirt

#Shirt 2:
#Website name: Lily Boutique
#URL: https://www.lilyboutique.com/fluttering-eyelet-scallop-hemline-top-in-cream
#Name of item: Ivory Flutter Top

#Shirt 3:
#Website name: Shopakira
#URL: https://shopakira.com/products/lover-girl-rhinestone-chain-top?variant=50376328282427&country=US
#Name of item: LOVER GIRL RHINESTONE CHAIN TOP

#Shirt 4:
#Website name: EMP-online
#URL: https://www.emp-online.com/p/gothic-top/463885.html?srsltid=AfmBOoqT_VNYbwmULq2lglCe9QSjibLGC0YsfweWgIHhW5r-2RNbv5Yp
#Name of item: "Gothic Top" Blouse black by Ocultica

#Shirt 5:
#Website name: Michael Andrews
#URL: https://www.michaelandrews.com/product/navy-short-sleeve-pajama-shirt/?srsltid=AfmBOop3ekI_t8ZeO1lIJi14OhtPWijiyE9lUSApoDdxL_drylf-_MXQ
#Name of item: Navy Short Sleeve Pajama Shirt

#Shirt 6:
#Website name: Kohls
#URL: https://www.kohls.com/product/prd-7527026/business-work-suit-set-for-womens-2-pc-notched-lapel-blazer-and-long-pants.jsp?skuid=72070878&CID=seo_offers&utm_campaign=SAG&utm_medium=organic&utm_source=google&utm_product=72070878
#Name of item: Business Work Suit Set for Women's 2 Piece Notched Lapel Blazer and Long Pants

#Pant 1:
#Website name: Boogzel Clothing
#URL: https://boogzelclothing.com/products/old-money-wide-pants?srsltid=AfmBOore3CXizNwbi8ftPUpYgQ2lmksDGr1Du6d0lFL3HTDn-9kVV6pF%5C
#Name of item: Old Money Wide Pants

#Pant 2:
#Website name: Sunday Supply co
#URL: https://us.sundaysupply.co/products/dunes-towelling-womens-beach-short?variant=31699682426926
#Name of item: Dunes Towelling Women's Beach Short

#Pant 3:
#Website name: PRISCAVera
#URL: https://priscavera.com/products/navy-asymmetrical-waist-maxi-skirt?variant=41137128865863
#Name of item: Navy Asymmetrical Waist Maxi Skirt

#Pant 4:
#Website name: Arcane Trail
#URL: https://arcanetrail.com/products/goth-maiden-bell-bottoms
#Name of item: Goth Maiden Bell Bottoms

#Pant 5:
#Website name: Vera Bradley
#URL: https://verabradley.com/products/pajama-pants-5502321511
#Name of item: Pajama Pants Tiny tomatoes coral in Cotton

#Pant 6:
#Website name: Kohls
#URL: https://www.kohls.com/product/prd-6998903/womens-elegant-pencil-skirt-high-waist-split-hem-work-bodycon-business-skirts.jsp?skuid=77641076&CID=seo_offers&utm_campaign=SAG&utm_medium=organic&utm_source=google&utm_product=77641076
#Name of item: Women's Elegant Pencil Skirt High Waist Split Hem Work Bodycon Business Skirts

#Shoe 1:
#Website name: Wear Old Money
#URL: https://wearoldmoney.com/products/old-money-leather-loafers?variant=47500539560278
#Name of item: OLD MONEY Leather Loafers

#Shoe 2:
#Website name: 2BigFeet
#URL: https://www.2bigfeet.com/products/birkenstock-arizona-birkibuc-mocha?srsltid=AfmBOoo3PNmzwkR4E8oUYyH2AC-euens67yJRnGRm9EoM-3NsXH8gc9A
#Name of item: Birkenstock Arizona Birkibuc Mocha

#Shoe 3:
#Website name: Lola Dre
#URL: https://loladre.com/products/black-satin-slingback-c12625-080-r001y063-black-silver?srsltid=AfmBOooUOzCzJteSneicPKpB2ecM-T1rUhKibdBNwEhq7-oSjZJAqud_
#Name of item: Lily Black Satin Crystal Trim Slingback

#Shoe 4:
#Website name: GothicPlus
#URL: https://www.gothicplus.com/gothic-shoes-ashes33-black-chunky-platform-mary-jane?srsltid=AfmBOopql9q4XlFJtqyMDZwBFuo3Td0HJQt_nv2xK-O-rGkkN4aiy5Kt
#Name of item: Ashes Chunky Heel Platform Mary Jane Shoes

#Shoe 5:
#Website name: Shoecity
#URL: https://shoecity.com/products/skechers-bobs-womens-too-cozy-meow-pajamas-memory-foam-slippers?srsltid=AfmBOoqPCcEpsyCfOcL2UHYLFl13zrdTmC8ZvmS_hobdeGwcawp708C2
#Name of item: Skechers Bobs Women's Too Cozy- Meow Pajamas Memory Foam Slippers

#Shoe 6:
#Website name: Amazon
#URL: https://www.amazon.com/YooPrettyz-Classic-Pointed-Stiletto-Romantic/dp/B0BTS9V8NC?th=1&psc=1
#Name of item: YooPrettyz Women Classic Pointed Toe Sexy High Heels Office Suite Stiletto Romantic Formal Wear Heel Shoes
