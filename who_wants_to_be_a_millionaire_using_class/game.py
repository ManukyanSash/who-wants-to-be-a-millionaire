import random

class Game:
    def __init__(self):
        self.quest = None
        
    def set_quest(self, quest):
        self.quest = quest        
    
    def game(self):
        quests = list(self.quest.keys())
        ans = list(self.quest.values())
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