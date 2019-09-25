def to_camel_case(text):
    text=text.replace('-', '_')
    list1=text.split("_")
    for x in range(len(list1)):
        if x>0:
            list1[x]=list1[x].capitalize()
    new_text=''.join(list1)
    return new_text    
    
    
        
    
    
        
    
print (to_camel_case("The-Stealth-Warrior"))

    

