import random
first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
            "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
            'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
            'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
            'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
            'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
            'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
            'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
            'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
            'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
            'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
            "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
            'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
            'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
            "Winston 'Jazz Hands'", 'Worms')
last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
            'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
            'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Jonson',
            'Kilbassom', 'Kneebob', 'Lemongrass', 'Lil Debil', 'Longbranch',
            'Mcgee', 'Muttley', 'Nettles', 'Noseworthy', 'Olivetti', 'Outerbridge',
            'Overpeck', 'Overturf', 'Pennywhistle', 'Peterson', 'Pieplow',
            'Pottin Soil', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal',
            'Snuggles', 'Splern', 'Swackhamer', 'Tippins', 'Turnipseed',
            'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

while True:
    firstname = random.choice(first)
    lastname = random.choice(last)
    print('\n \n')
    print('hello : ',firstname, lastname)
    
    tryagain = input('\n\nTry again? (Press Enter else N to quit) ')
    if tryagain.lower() == 'n':
        break

print('Bye',firstname, lastname)