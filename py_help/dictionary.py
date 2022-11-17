alien_0={'color':'green','points':5}
alien_1={'color':'red','points':10}
print(alien_0['color']+" alien is "+str(alien_0['points']))
print(alien_1['color']+" alien is "+str(alien_1['points']))
#adding the items
alien_0['weapon']='sword'

alien_1['weapon']='gun'

if(alien_1['weapon']=='sword'):
    print("melee")
else:
    print("ranged")

del alien_0['weapon']
print(alien_0)