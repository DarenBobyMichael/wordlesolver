ans = {0:None,1:None,2:None,3:None,4:None}
print ("""
____    __    ____  ______   .______       _______   __       _______         _______.  ______    __      ____    ____  _______ .______      
\   \  /  \  /   / /  __  \  |   _  \     |       \ |  |     |   ____|       /       | /  __  \  |  |     \   \  /   / |   ____||   _  \     
 \   \/    \/   / |  |  |  | |  |_)  |    |  .--.  ||  |     |  |__         |   (----`|  |  |  | |  |      \   \/   /  |  |__   |  |_)  |    
  \            /  |  |  |  | |      /     |  |  |  ||  |     |   __|         \   \    |  |  |  | |  |       \      /   |   __|  |      /     
   \    /\    /   |  `--'  | |  |\  \----.|  '--'  ||  `----.|  |____    .----)   |   |  `--'  | |  `----.   \    /    |  |____ |  |\  \----.
    \__/  \__/     \______/  | _| `._____||_______/ |_______||_______|   |_______/     \______/  |_______|    \__/     |_______|| _| `._____|                                                                                                                                                                   
""")
blacklisted = set()
yellowlisted = {0:[],1:[],2:[],3:[],4:[]}
suspects = []
file = open("dictionary.txt","r")
for word in file.readlines():
    suspects.append(word[:len(word)-1])
print("Hint💡: Try starting with something like 'ADIEU' or 'SLATE'\nEnter 'SOLVED' once the word is solved")
while True:
    word_set = []
    result = input("Enter output: ").split()
    if result[0] == "solved" or result[0] == "SOLVED":
        break

    for i in range(len(result)):
        option = -1
        if len(result[i]) ==  2:
            option = result[i][0]
        if option == '0': #yellow
            yellowlisted[i].append(result[i][1])
            word_set.append(result[i][1])
            continue
        if option == '1': #green
            # word_set.remove(result[i][1])
            ans[i] = result[i][1]
            continue
        blacklisted.add(result[i]) #black

    #black filter
    print(ans)
    filtered_suspects = []

    for suspect in suspects:
            flag=True
            for letter in suspect:
                if letter in blacklisted:
                    flag=False
                    break
            if flag:
                filtered_suspects.append(suspect)

    suspects = filtered_suspects
    
    #yellow filter positive
    for letter in word_set:
        filtered_suspects = []
        for word in suspects:
            if letter in word:
                filtered_suspects.append(word)
        suspects = filtered_suspects

    suspects = filtered_suspects

    #yellow filter positive
    filtered_suspects = []
    for word in suspects:
        flag = True
        for key,value in yellowlisted.items():
            if value is None:
                continue
            if word[key]==value:
                flag = False
        if flag:
            filtered_suspects.append(word)
    suspects = filtered_suspects

    #green filter
    filtered_suspects = []
    for word in suspects:
        flag = True
        for key,value in ans.items():
            if value is None:
                continue
            if word[key]!=value:
                flag = False
        if flag:
            filtered_suspects.append(word)
    
    suspects = filtered_suspects
    
    print(suspects)
print('See you at the next puzzle ;)')


    



    


        







