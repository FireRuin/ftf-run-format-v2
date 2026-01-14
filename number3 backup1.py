from speedruncomapi import Game, Leaderboard, User
import time

start = time.perf_counter()

class ftf_run :
    def __init__(self, map_name, map_name_id ,runtime, runners, score, wr_val, wr_val_per_person):
        self.map_name = map_name
        self.map_name_id = map_name_id
        self.runtime = runtime
        self.runners = runners
        self.score = score
        self.wr_val = wr_val
        self.wr_val_per_person = wr_val_per_person

def GET_ALL_RUNS(id):
    return Leaderboard.get_full_game_leaderboard(f"{game_id}",f"{id}")["runs"]

def COMBINE_RUNS(type):
    return GET_ALL_RUNS(game_cat[type]["id"])

game_id = Game.get_game_id("roblox_ftf")
game_cat = Game.get_categories(f"{game_id}")
special_case = ["SkittlesCat", "Jenna_0134"]
all_runs = []
all_runs = COMBINE_RUNS(0) + COMBINE_RUNS(1) + COMBINE_RUNS(3)
print(len(all_runs))
print("done getting all runs", time.perf_counter() - start)

id_list = ['id', ' 7dg6l4gk', 'n2yg8772' 'gq7dd6yq', '21gdd3m1', 'jqzeemmq', '21dggej1', '5q8889kq', '4qykjm31', 'mlngz761', 'mln2grjl', '810r2321', 'lmo8vvj1', '1w4ezzoq', 'q8kezwyq', 'qyzx4g61', 'ln8y3jol', 'qox3k64q', '1395zjk1', 'q75kpor1', 'qkekv59q', 'qkejr3nq', '4qyoow7l', 'mlnmmod1', '810jjd5l', '9qjnn8g1', '4lxoo6rl', '814ggwj1', 'z19yypkl', '81poo5kq', 'xqk00ny1', '8102wyjq', '9qjpxo0q', '9qj5pj31', 'jq6j83j1', 'qoxmkkpq', '139wddd1', 'q65478vl', 'lmoxn781', '1w4m86mq', '139mdny1', 'qvvej05q', '1gny56ol', '1pyw92e1', 'q75jn3v1', 'gq7ddxyq', '21gddpm1', 'jqzee3mq', '21dgzjj1', 'qj70zmeq', 'q6504o3l', '10vz5nwl', 'lmokx3j1', '1w4pm2oq', 'qoxpyepq', '1398vkd1'] 
name_list = ['id_name', 'Survivor', 'Beast' 'Facility_0', 'Airport', 'Homestead', 'Abandoned Prison Maximus', 'Library', 'Abandoned Facility Remake', 'Forgotten Facility', 'Haunted Mansion', 'The Backrooms', 'School', 'Nuclear Power Plant', 'Sewer Treatment Plant', 'Laboratory Complex', 'Abandoned Facility Optimus', 'Arcade', 'Arctic Station', 'Sanctuary Zoo', 'Spaceship', 'Ghost Town', 'One Player', 'Two Players', 'Three Players', 'Four Players', 'Facility_0', 'Airport', 'Homestead', 'Abandoned Prison Maximus', 'Library', 'Abandoned Facility Remake', 'Forgotten Facility', 'Haunted Mansion', 'The Backrooms', 'School', 'Nuclear Power Plant', 'Sewer Treatment Plant', 'Laboratory Complex', 'Abandoned Facility Optimus', 'Arcade', 'Arctic Station', 'Sanctuary Zoo', 'Spaceship', 'Ghost Town', 'One Capture', 'Two Captures', 'Three Captures', 'Four Captures', 'Survivor', 'Beast', 'Backrooms (Halloween)', '1', '2', '3', '4']
print("done getting variables", time.perf_counter() - start)

player_id_list = []
player_name_list = []
guest_list = []
for i in all_runs :
    players = i["run"]["players"]
    for p in range(0, len(players)) :
        if players[p]["rel"] == 'user' :
            player_id_list.append(players[p]["id"])
        else :
            guest_list.append(players[p]["name"])
player_id_list = list(set(player_id_list))
guest_list = list(set(guest_list))
for i in player_id_list:
    player_name_list.append(User.Info(f"{i}")["data"]["names"]["international"])
print("done getting players' name", time.perf_counter() - start)

run_stats_datas = []
player_stats_datas = []
ftf_run = {
    "name" : "name",
    "runid" : "runid",
    "time" : 900,
    "placement" : 0,
    "runners" : "",
    "random_count" : 0,
    "wr_val" : 0,
    "wr_value_per_person" : 3,
    "total_run_in_category" : 0,
    "score" : 0
}

player_stats = {
    "name" : "name",
    "country" : "country",
    "wr_count" : 0,
    "wr_value" : 0,
    "score" : 0,
    "most_value_run" : "run_name" 
}
