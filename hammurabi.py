#Homework No.1
#Name: Ziyi Han
#This is a program about Hammurabi game.


import random

def print_intro():
    #print the introduction words
    print('''\t  Congrats, you are the newest ruler of ancient Samaria, elected
          for a ten-year term of office. Your duties are to distribute food,
          direct farming, and buy and sell land as needed to support your
          people. Watch out for rat infestations and the resultant plague!
          Grain is the general currency, measured in bushels. The following
          will help you in your decisions:\n
          \t* Each person needs at least 20 bushels of grain per year to survive.\n
          \t* Each person can farm at most 10 acres of land.\n
          \t* It takes 2 bushels of grain to farm an acre of land.\n
          \t* The market price for land flustuates yearly.\n
          Rule wisely and you will be showered with appreciation at the end
          of your term. Rule poorly and you will be kicked out of office!\n\n''');
    
def ask_to_buy_land(bushels,cost):
    #'''Ask user how many bushels to spend buying land.'''
    try:
        acres_toBuy = int(input("\tYour Majesty, how many acres will you buy? "));
        while (acres_toBuy * cost > bushels) or (acres_toBuy < 0):
            print "\tO great Hammurabi, we have but ",bushels," bushels of grain!"
            acres_toBuy = int(input("\tYour Majesty, how many acres will you buy?"));
    except:
        print "Program Crashed!!!"
        quit();
        
    return acres_toBuy

def ask_to_sell_land(acres):
    #'''Ask user how much land they want to sell.'''
    try:
        acres_toSell = int(input("\tYour Majesty, how many acres will you sell? "));
        while acres_toSell > acres or acres_toSell<0:
            print "/tO great Hammurabi, we have but ",acres," acres of land!";
            acres_toSell = int(input("\tYour Majesty, how many acres will you sell? "));
    except:
        print "Program Crashed!!!"
        quit();
        
    return acres_toSell

def ask_to_feed(bushels):
    #Ask user how many bushels they want to use for feeding.
    try:
        feed = int(input("\tYour Majesty, how much grain will feed the people? "));
        while feed > bushels or feed<0:
            print "\tO great Hammurabi, we have but ",bushels," bushels of grain!";
            feed = int(input("\tYour Majesty, how much grain will you feed the people? "));
    except:
        print "Program Crashed!!!"
        quit();
        
    return feed

def ask_to_cultivate(acres,population,bushels):
    #'''Ask user how much land they want to plant seed in.'''
    try:
        plant = int(input('''\tYour Majesty, how many acres of land will you plant with
                           seed in? '''));
        while plant > acres or plant > population*10 or plant > bushels or plant<0:
            print "\tO great Hammurabi, we have but ",bushels, " bushels of grain and ",acres,"acres of land and ",population,"people!\n"
            plant = int(input('''\tYour Majesty, how many acres of land will you plant
                               with seed in? '''));
    except:
        print "Program Crashed!!!"
        quit();
        
    return plant

def isPlague():
    #determine if there is plague
    rand = random.randint(1,100);
    if rand <86:
        return False
    else:
        return True

def numStarving(population,bushels):
    #calculate how many people starved
    if bushels < population*20:
        return int(population-bushels/20)
    else:
        return 0

def numImmigrant(land,bushels,population,starved):
    #calculate number of immigrants
    if starved > 0:
        return 0
    else:
        return int((20*land+bushels)/(100*population+1))

def getHarvest():
    #harvest per acre
    return random.randint(1,8)

def effectOfRats():
    #rats ate
    return random.randint(10,30)/100.0

def priceOfLand():
    #determine the price of land 
    return random.randint(16,22)

def print_sum(starved, acres, population):
    plantable = acres;
    if plantable > 10 * population:
        plantable = 10 * population;
        
    if starved >= population *45/100:
        print ('''\t\tO Great Hammurabi!\n
               %d of your people starved during the last year of your incompetent reign!\n
               The few who remain have stormed your palace and bodily evicted you!\n
               \nYour Final Rating: Terrible.'''%(starved))
    else:
        if plantable <600:
            print ('''Congratulations, O Great Hammurabi!\n
                    You have ruled wisely but not well;\n
                    You have led your people through ten difficult year, \n
                    but your kingdom has shrunk to a mere %d acres.\n
                    \nYour Final Rating: Adequate.'''%(acres))
        elif plantable < 800 and plantable >= 600:
            print ('''Congratulations, O Great Hammurabi!\n
                    You have ruled wisely, and show the ancient world that\n
                    a stable economy is possible.\n
                    \nYour Final Rating: Good.''')
        else:
            print ('''Congratulations, O Great Hammurabi!\n
                    You have ruled wisely and well, \n
                    and expanded your holdings while keeping your people happy.\n
                    Altogether, a most impressive job!\n
                    \n Your Final Rating: Superb.''')
    

#Hammurabi 
def Hammurabi():
    starved = 0;
    immigrants = 5;
    population = 100;
    harvest = 3000;       # total bushels harvested
    bushels_per_acre = 3; # amount harvested for each acre planted
    rats_ate = 200;       # bushels destroyed by rats
    bushels_in_storage = 2800;
    acres_owned = 1000;
    cost_per_acre = 19;   # each acre costs this many bushels
    plague_deaths = 0;
    

    print_intro(); # Call intro printing function

    for year in range(0,11):
        #loop 11 turns 
        print('''\t\tO great Hammurabi!\n
                 I beg to report to you.\n
                 You are in year %d of your ten year rule.\n
                 In the previous year %d people starved to death.\n
                 In the previous year %d people entered the kingdom.\n
                 The population is now %d.\n
                 We harvested %d bushels at %d bushels per acre.\n
                 Rats destroyed %d bushels, leaving %d bushels in storage.\n
                 The city owns %d acres of land.\n
                 Land is currently worth %d bushels per acre.\n
                 There were %d deaths from the plague.\n'''
            %(year,starved,immigrants,population,harvest,bushels_per_acre,
              rats_ate,bushels_in_storage,acres_owned,cost_per_acre,
              plague_deaths));
        
        land_buy = ask_to_buy_land(bushels_in_storage,cost_per_acre)

        acres_owned += land_buy;
        bushels_in_storage -= cost_per_acre * land_buy

        if land_buy==0:
            land_sell = ask_to_sell_land(acres_owned);
            acres_owned -= land_sell;
            bushels_in_storage += land_sell * cost_per_acre;

        feed = ask_to_feed(bushels_in_storage);
        bushels_in_storage -= feed;

        cul = ask_to_cultivate(acres_owned,population,bushels_in_storage);
        bushels_in_storage -= cul;
        
        #if there is plague
        if isPlague():
            plague_deaths = population/2
            population = population/2
        else:
            plague_deaths = 0
            
        #count starved 
        starved = numStarving(population,feed);

        if starved >= population*0.45:
            print('''HAMMURABI! YOU've been KICKED OUT OF OFFICE!\n
                  You starved %d people in one year!\n
                  Due to this extreme mismanagement, you have not only
                  been impeached and thrown out of office, but you have
                  also been declared \'National Fink\''''%(starved));
            print("GAME OVER")
            break;

        population -= starved;

        #immigrants 
        immigrants = numImmigrant(acres_owned,bushels_in_storage,population,starved);

        population+=immigrants;

        #bushels harvest
        bushels_per_acre = getHarvest();
        harvest = cul * bushels_per_acre;
        bushels_in_storage += harvest;
        
        #set land price for the next year
        cost_per_acre = priceOfLand();

        #determine the amount rat destroyed
        rat_probability = random.random();
        if rat_probability < 0.4:
            rats_ate = bushels_in_storage*effectOfRats();
        else:
            rats_ate = 0;
        bushels_in_storage -=rats_ate;

    #print the final summary
    print_sum(starved,acres_owned,population);

    #quit the game
    while raw_input("------Press any key to exit the game-------"):
        quit();

Hammurabi()
        
        

        

        


        
    



    

    
    
    
    
