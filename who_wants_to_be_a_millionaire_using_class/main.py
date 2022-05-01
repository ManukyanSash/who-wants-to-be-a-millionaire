from quest import Quest
from player import Player
from game import Game

        
def main():
    q = Quest('quest.txt')   
    p = Player('top_list.txt') 
    g = Game() 
    while True:        
        pl_name = input("Who are you warrior? ")
        if p.check_player_exist(pl_name): 
            break
        else:
            print("We have such warrior!!!")
            
       
    quests = q.get_quests()
    rand_ind = q.get_random_three_numbers()
    g.set_quest(q.create_questions(quests, rand_ind))
    ccount = g.game()
    list = p.get_players_list()
    res = p.add_and_sort_res(list, ccount)
    p.add_to_list(res)                 
              
if __name__ == "__main__":
    main()

