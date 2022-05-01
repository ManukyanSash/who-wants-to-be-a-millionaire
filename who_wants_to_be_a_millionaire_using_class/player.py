class Player:
    def __init__(self, fname):
        self.pname = None
        self.fname = fname
     
        
    def check_player_exist(self, pname):
        ml = []
        with open(self.fname, 'r') as f:
            c = f.readlines()
        for line in c:
            ml.append(line.split(" :")[0])
        if pname not in ml:
            self.pname = pname
            return True
        return False           
    
    def get_players_list(self):
        res = {}
        with open(self.fname, 'r') as f:
            l = f.readlines()
        if len(l) > 0:    
            for i in range(len(l)):
                pl, c = l[i].split(" : ")
                res[pl] = c.strip()  
        return res   
    
    def add_and_sort_res(self, res, c): 
        res[self.pname] = str(c)
        sorted_res = sorted(list(res.items()), key=lambda x:x[1], reverse=True)
        return sorted_res
    
    def add_to_list(self, result):
        with open(self.fname, 'w') as f:
            for i in range(len(result)):
                f.write("{a} : {b} \n".format(a = result[i][0], b = result[i][1])) 