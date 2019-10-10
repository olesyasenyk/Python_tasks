def shorten_to_date(long_date):
    for i in range(len(long_date)):
        if long_date[i]==',':
            short_date=long_date[0:i]
            
            
    return short_date

print(shorten_to_date("Tuesday January 29, 10pm"))