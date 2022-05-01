import random

class Quest:
    def __init__(self, fname):
        self.fname = fname
        #top_list.txt
        
    def get_quests(self):
        with open(self.fname, 'r') as f:
            c = f.readlines()
        quest = {}
        for line in c:
            q, a = line.split("?")     
            quest[q] = a.split(",")                                         
        return quest 
    
    @staticmethod
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
    
    @staticmethod
    def create_questions(q, ind):
        nq = {}
        ind_list = list(q.keys())
        for i in ind:
            nq[ind_list[i]] = q[ind_list[i]]
        return nq