import random

def check_player_exist(player):
    ml = []
    with open('top_list.txt', 'r') as f:
        c = f.readlines()
    for line in c:
        ml.append(line.split(" :")[0])
    if player not in ml:
        return player
    return False        

def get_quests():
    with open('quest.txt', 'r') as f:
        c = f.readlines()
    quest = {}
    for line in c:
        q, a = line.split("?")     
        quest[q] = a.split(",")                                         
    return quest 

def get_random_three_numbers():
    ml = []
    i = 0
    n = 0
    while i < 3:
        n = random.randint(0,9)
        if n not in ml:
            ml.append(n)  
            i += 1
    return ml    
   
def create_questions(q, ind):
    nq = {}
    ind_list = list(q.keys())
    for i in ind:
        nq[ind_list[i]] = q[ind_list[i]]
    return nq

def game(q):
    quests = list(q.keys())
    ans = list(q.values())
    ccount = 0 
    i = 0
    call = True
    fifty = True
    help = True
    while i < len(quests):
        print(quests[i])
        ls_a = []
        while len(ls_a) < 4:
            item = random.choice(ans[i])
            if item not in ls_a:
                ls_a.append(item)
        print("---------")        
        for el in ls_a:        
            print(str(el).strip())    
        print("---------")        
        a = input("your answer is: ")
        if a in "123456789":
            if ls_a[int(a)-1] == ans[i][0]:
                ccount += 1
                print("correct")
                print("---------")
                i += 1
            else:
                print("correct answer was: {a}".format(a=ans[i][0]))
                print("---------")
                i += 1
        elif a == "call" and call:
            print("correct answer was: {a}".format(a=ans[i][0]))
            print("---------")
            ccount += 1
            call = False
            i += 1    
        elif a == "fifty" and fifty:
            fifty_ans = [ans[i][0], ans[i][random.randint(1,3)]]
            print("---------")
            for el in fifty_ans:
                print(el)  
            print("---------") 
            fifty_a = input("your answer is: ")
            if fifty_a in "123456789":
                if fifty_ans[int(fifty_a)-1] == ans[i][0]:  
                    ccount += 1
                    print("correct")
                    print("---------")
                    i += 1
                else:
                    print("correct answer was: {a}".format(a=ans[i][0]))
                    print("---------")
                    i += 1     
            fifty = False 
        elif a == "help" and help:
            help_ans = {}
            sum = 0
            for el in ls_a:
                help_ans[el] = random.randint(0,24)
                if el == ans[i][0]:
                    help_ans[el] = 0
                sum += help_ans[el]
            help_ans[ans[i][0]] = 100 - sum         
            for j in range(len(help_ans)):
                print(str(ls_a[j]) + ":" + str(help_ans[ls_a[j]]) + "%")      
            help_a = input("your answeris: ")  
            if help_a in "123456789":
                if ls_a[int(help_a)-1] == ans[i][0]:
                    ccount += 1
                    print("correct")
                    print("---------")
                    i += 1
                else:
                    print("correct answer was: {a}".format(a=ans[i][0]))
                    print("---------")
                    i += 1    
            help = False              
    return ccount  
def get_from_list():
    res = {}
    with open('top_list.txt', 'r') as f:
        l = f.readlines()
    if len(l) > 0:    
        for i in range(len(l)):
            pl, c = l[i].split(" : ")
            res[pl] = c.strip()  
    return res   

def add_and_sort_res(res,pl, c): 
    res[pl] = str(c)
    sorted_res = sorted(list(res.items()), key=lambda x:x[1], reverse=True)
    return sorted_res

def add_to_list(result):
    with open('top_list.txt', 'w') as f:
        for i in range(len(result)):
            f.write("{a} : {b} \n".format(a = result[i][0], b = result[i][1])) 
    print(result)       
        
def main():
    
    while True:
        pl_name = input("Who are you warrior? ")
        if check_player_exist(pl_name): 
            break
        else:
            print("We have such warrior!!!")
    quests = get_quests()
    rand_ind = get_random_three_numbers()
    game_quests = create_questions(quests, rand_ind)
    ccount = game(game_quests)
    list = get_from_list()
    res = add_and_sort_res(list, pl_name, ccount)
    add_to_list(res)                 
              
if __name__ == "__main__":
    main()

