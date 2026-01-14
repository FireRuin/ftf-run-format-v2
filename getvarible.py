from speedruncomapi import Game
import time

start = time.perf_counter() #only use this whenever the game update, please

def GET_CATEGORY_VARIBLES(id, type):
    return Game.get_category_variables(f"{id}")[type]["values"]["choices"]

game_id = Game.get_game_id("roblox_ftf")
game_cat = Game.get_categories(f"{game_id}")
id_list = []
name_list = []
id_to_name_dict = {'id':"id_name"}
id_to_name_dict.update(GET_CATEGORY_VARIBLES("7dg6l4gk", 0))
id_to_name_dict.update(GET_CATEGORY_VARIBLES("7dg6l4gk", 1))
id_survivor_list = list(id_to_name_dict.keys())
name_survivor_list = list(id_to_name_dict.values())

id_to_name_dict = {'id':"id_name"}
id_to_name_dict.update(GET_CATEGORY_VARIBLES("n2yg8772", 0))
id_to_name_dict.update(GET_CATEGORY_VARIBLES("n2yg8772", 1))
id_beast_list = list(id_to_name_dict.keys())
name_beast_list = list(id_to_name_dict.values())

id_to_name_dict = {'id':"id_name"}
id_to_name_dict.update(GET_CATEGORY_VARIBLES("wk65l5e2", 0))
id_to_name_dict.update(GET_CATEGORY_VARIBLES("wk65l5e2", 1))
id_to_name_dict.update(GET_CATEGORY_VARIBLES("wk65l5e2", 2))
seasonal_id_list = list(id_to_name_dict.keys())
seasonal_name_list = list(id_to_name_dict.values())
#ts time is based on the internet :wilted:, cant use aiohttp

def GET_DIFFERENT(lista, listb):
    difference_list = [item for item in lista if item not in listb]
    return difference_list
category_name_list = [['7dg6l4gk', 'n2yg8772', 'qj70zmeq', 'q6504o3l'], ['gq7ddxyq', '21gddpm1', 'jqzee3mq', '21dgzjj1'],['lmokx3j1', '1w4pm2oq', 'qoxpyepq', '1398vkd1']]

id_count_survivor_list = id_survivor_list[-4:] #1
name_count_survivor_list = name_survivor_list[-4:] #2
id_count_beast_list = id_beast_list[-4:] #3
name_count_beast_list = name_beast_list[-4:] #4
seasonal_id_survivor_list = ['lmokx3j1', '1w4pm2oq', 'qoxpyepq', '1398vkd1'] #5
seasonal_name_count_survivor_list = ['One Player', 'Two Players', 'Three Players', 'Four Players'] #6
seasonal_id_beast_list = ['lmokx3j1', '1w4pm2oq', 'qoxpyepq', '1398vkd1'] #7
seasonal_name_count_beast_list = ['One Capture', 'Two Captures', 'Three Captures', 'Four Captures'] #81
id_map_survivor_list = GET_DIFFERENT(id_survivor_list, id_count_survivor_list + ["id"]) #9
name_map_survivor_list = GET_DIFFERENT(name_survivor_list, name_count_survivor_list + ["id_name"]) #10
id_map_beast_list = GET_DIFFERENT(id_beast_list, id_count_beast_list + ["id"]) #11
name_map_beast_list = GET_DIFFERENT(name_beast_list, name_count_beast_list + ["id_name"]) #12
seasonal_id_list = GET_DIFFERENT(seasonal_id_list, seasonal_id_survivor_list + ["id"]) #13
seasonal_name_list = GET_DIFFERENT(seasonal_name_list, ['1', '2', '3', '4', "id_name"]) #14
seasonal_map_id_list = GET_DIFFERENT(seasonal_id_list, ['qj70zmeq', 'q6504o3l']) #15
seasonal_map_name_list = GET_DIFFERENT(seasonal_name_list, ['Survivor', 'Beast']) #16
# list 13, list 14 for viewing purpose only, do not touch or use any code on them

def ORDERING(lista, listb, listc, listd, name, type):
    global id_list, name_list
    for i in range(0, len(lista)):
        for j in range(0, 4):
            id_list.append(type + lista[i] + listb[j])
            name_list.append(name + " " + listc[i] + " " + listd[j])

ORDERING(id_map_survivor_list, id_count_survivor_list, name_map_survivor_list, name_count_survivor_list, "Survivor", "7dg6l4gk")
ORDERING(id_map_beast_list, id_count_beast_list, name_map_beast_list, name_count_beast_list, "Beast", "n2yg8772")
print(seasonal_name_list, seasonal_id_list)
for i in range(0, len(seasonal_map_id_list)):
    for j in range(0, 4):
        id_list.append('qj70zmeq' + seasonal_map_id_list[i] + seasonal_id_survivor_list[j])
        id_list.append('q6504o3l' + seasonal_map_id_list[i] + seasonal_id_beast_list[j])
        name_list.append("Survivor" + " " + seasonal_map_name_list[i] + " " + seasonal_name_count_survivor_list[j])
        name_list.append("Beast" + " " + seasonal_map_name_list[i] + " " + seasonal_name_count_beast_list[j])

print("done getting variables", time.perf_counter() - start)
print(id_list, name_list, category_name_list)
print(id_count_beast_list)