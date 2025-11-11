def find_words(search_term: str):

    dot="."
    star="*"
    indexlist=[]
    templist=[]
    searchstring=""
    

    for items in range(len(search_term)):
                    
        if search_term[items]==dot:
             continue
        
        searchstring+=search_term[items]

        indexlist.append(items)
 
    
    with open("Part 6/words.txt") as file:
        
        for line in file:
            tempstring=""
            line=line.strip()

            if dot in search_term:
                if len(line)==len(search_term):
                    for items in indexlist:
                        tempstring+=line[items]
                    if tempstring==searchstring:
                        templist.append(line)
            
            elif star in search_term:

                if star in search_term[0]:

                    newsearch_term=search_term[1:]

                    if line.endswith(newsearch_term):
                        templist.append(line)
                
                elif star in search_term[-1]:

                    newsearch_term=search_term[:-1]

                    if line.startswith(newsearch_term):
                        templist.append(line)
                       
            else:

                if search_term==line:
                    templist.append(line)
                
 
    return templist


print(find_words(".a.e"))
print(find_words("ca."))
print(find_words("sane"))
print(find_words("ca*"))
print(find_words("*vokes"))
print(find_words("randomword"))

