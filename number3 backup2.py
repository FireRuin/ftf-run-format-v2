from speedruncomapi import Game, Leaderboard
import time
import asyncio
import aiohttp

start = time.perf_counter()

print("getting runs information ...")
def GET_RUNS(type):
    return Leaderboard.get_full_game_leaderboard(f"{Game.get_game_id("roblox_ftf")}",f"{Game.get_categories(f"{Game.get_game_id("roblox_ftf")}")[type]["id"]}")["runs"]

special_case = ["SkittlesCat", "Jenna_0134"]
all_runs = GET_RUNS(0) + GET_RUNS(1) + GET_RUNS(3)
#print(len(all_runs))
print("done getting all runs", time.perf_counter() - start)

print("getting variables ...")
id_list = []
name_list = []
category_id_list = []
def LISTMAKER_1():
    global id_list, name_list, category_id_list
    id_list = ['7dg6l4gkgq7dd6yq4qyoow7l', '7dg6l4gkgq7dd6yqmlnmmod1', '7dg6l4gkgq7dd6yq810jjd5l', '7dg6l4gkgq7dd6yq9qjnn8g1', '7dg6l4gk21gdd3m14qyoow7l', '7dg6l4gk21gdd3m1mlnmmod1', '7dg6l4gk21gdd3m1810jjd5l', '7dg6l4gk21gdd3m19qjnn8g1', '7dg6l4gkjqzeemmq4qyoow7l', '7dg6l4gkjqzeemmqmlnmmod1', '7dg6l4gkjqzeemmq810jjd5l', '7dg6l4gkjqzeemmq9qjnn8g1', '7dg6l4gk21dggej14qyoow7l', '7dg6l4gk21dggej1mlnmmod1', '7dg6l4gk21dggej1810jjd5l', '7dg6l4gk21dggej19qjnn8g1', '7dg6l4gk5q8889kq4qyoow7l', '7dg6l4gk5q8889kqmlnmmod1', '7dg6l4gk5q8889kq810jjd5l', '7dg6l4gk5q8889kq9qjnn8g1', '7dg6l4gk4qykjm314qyoow7l', '7dg6l4gk4qykjm31mlnmmod1', '7dg6l4gk4qykjm31810jjd5l', '7dg6l4gk4qykjm319qjnn8g1', '7dg6l4gkmlngz7614qyoow7l', '7dg6l4gkmlngz761mlnmmod1', '7dg6l4gkmlngz761810jjd5l', '7dg6l4gkmlngz7619qjnn8g1', '7dg6l4gkmln2grjl4qyoow7l', '7dg6l4gkmln2grjlmlnmmod1', '7dg6l4gkmln2grjl810jjd5l', '7dg6l4gkmln2grjl9qjnn8g1', '7dg6l4gk810r23214qyoow7l', '7dg6l4gk810r2321mlnmmod1', '7dg6l4gk810r2321810jjd5l', '7dg6l4gk810r23219qjnn8g1', '7dg6l4gklmo8vvj14qyoow7l', '7dg6l4gklmo8vvj1mlnmmod1', '7dg6l4gklmo8vvj1810jjd5l', '7dg6l4gklmo8vvj19qjnn8g1', '7dg6l4gk1w4ezzoq4qyoow7l', '7dg6l4gk1w4ezzoqmlnmmod1', '7dg6l4gk1w4ezzoq810jjd5l', '7dg6l4gk1w4ezzoq9qjnn8g1', '7dg6l4gkq8kezwyq4qyoow7l', '7dg6l4gkq8kezwyqmlnmmod1', '7dg6l4gkq8kezwyq810jjd5l', '7dg6l4gkq8kezwyq9qjnn8g1', '7dg6l4gkqyzx4g614qyoow7l', '7dg6l4gkqyzx4g61mlnmmod1', '7dg6l4gkqyzx4g61810jjd5l', '7dg6l4gkqyzx4g619qjnn8g1', '7dg6l4gkln8y3jol4qyoow7l', '7dg6l4gkln8y3jolmlnmmod1', '7dg6l4gkln8y3jol810jjd5l', '7dg6l4gkln8y3jol9qjnn8g1', '7dg6l4gkqox3k64q4qyoow7l', '7dg6l4gkqox3k64qmlnmmod1', '7dg6l4gkqox3k64q810jjd5l', '7dg6l4gkqox3k64q9qjnn8g1', '7dg6l4gk1395zjk14qyoow7l', '7dg6l4gk1395zjk1mlnmmod1', '7dg6l4gk1395zjk1810jjd5l', '7dg6l4gk1395zjk19qjnn8g1', '7dg6l4gkq75kpor14qyoow7l', '7dg6l4gkq75kpor1mlnmmod1', '7dg6l4gkq75kpor1810jjd5l', '7dg6l4gkq75kpor19qjnn8g1', '7dg6l4gkqkekv59q4qyoow7l', '7dg6l4gkqkekv59qmlnmmod1', '7dg6l4gkqkekv59q810jjd5l', '7dg6l4gkqkekv59q9qjnn8g1', '7dg6l4gkqkejr3nq4qyoow7l', '7dg6l4gkqkejr3nqmlnmmod1', '7dg6l4gkqkejr3nq810jjd5l', '7dg6l4gkqkejr3nq9qjnn8g1', 'n2yg87724lxoo6rlgq7ddxyq', 'n2yg87724lxoo6rl21gddpm1', 'n2yg87724lxoo6rljqzee3mq', 'n2yg87724lxoo6rl21dgzjj1', 'n2yg8772814ggwj1gq7ddxyq', 'n2yg8772814ggwj121gddpm1', 'n2yg8772814ggwj1jqzee3mq', 'n2yg8772814ggwj121dgzjj1', 'n2yg8772z19yypklgq7ddxyq', 'n2yg8772z19yypkl21gddpm1', 'n2yg8772z19yypkljqzee3mq', 'n2yg8772z19yypkl21dgzjj1', 'n2yg877281poo5kqgq7ddxyq', 'n2yg877281poo5kq21gddpm1', 'n2yg877281poo5kqjqzee3mq', 'n2yg877281poo5kq21dgzjj1', 'n2yg8772xqk00ny1gq7ddxyq', 'n2yg8772xqk00ny121gddpm1', 'n2yg8772xqk00ny1jqzee3mq', 'n2yg8772xqk00ny121dgzjj1', 'n2yg87728102wyjqgq7ddxyq', 'n2yg87728102wyjq21gddpm1', 'n2yg87728102wyjqjqzee3mq', 'n2yg87728102wyjq21dgzjj1', 'n2yg87729qjpxo0qgq7ddxyq', 'n2yg87729qjpxo0q21gddpm1', 'n2yg87729qjpxo0qjqzee3mq', 'n2yg87729qjpxo0q21dgzjj1', 'n2yg87729qj5pj31gq7ddxyq', 'n2yg87729qj5pj3121gddpm1', 'n2yg87729qj5pj31jqzee3mq', 'n2yg87729qj5pj3121dgzjj1', 'n2yg8772jq6j83j1gq7ddxyq', 'n2yg8772jq6j83j121gddpm1', 'n2yg8772jq6j83j1jqzee3mq', 'n2yg8772jq6j83j121dgzjj1', 'n2yg8772qoxmkkpqgq7ddxyq', 'n2yg8772qoxmkkpq21gddpm1', 'n2yg8772qoxmkkpqjqzee3mq', 'n2yg8772qoxmkkpq21dgzjj1', 'n2yg8772139wddd1gq7ddxyq', 'n2yg8772139wddd121gddpm1', 'n2yg8772139wddd1jqzee3mq', 'n2yg8772139wddd121dgzjj1', 'n2yg8772q65478vlgq7ddxyq', 'n2yg8772q65478vl21gddpm1', 'n2yg8772q65478vljqzee3mq', 'n2yg8772q65478vl21dgzjj1', 'n2yg8772lmoxn781gq7ddxyq', 'n2yg8772lmoxn78121gddpm1', 'n2yg8772lmoxn781jqzee3mq', 'n2yg8772lmoxn78121dgzjj1', 'n2yg87721w4m86mqgq7ddxyq', 'n2yg87721w4m86mq21gddpm1', 'n2yg87721w4m86mqjqzee3mq', 'n2yg87721w4m86mq21dgzjj1', 'n2yg8772139mdny1gq7ddxyq', 'n2yg8772139mdny121gddpm1', 'n2yg8772139mdny1jqzee3mq', 'n2yg8772139mdny121dgzjj1', 'n2yg8772qvvej05qgq7ddxyq', 'n2yg8772qvvej05q21gddpm1', 'n2yg8772qvvej05qjqzee3mq', 'n2yg8772qvvej05q21dgzjj1', 'n2yg87721gny56olgq7ddxyq', 'n2yg87721gny56ol21gddpm1', 'n2yg87721gny56oljqzee3mq', 'n2yg87721gny56ol21dgzjj1', 'n2yg87721pyw92e1gq7ddxyq', 'n2yg87721pyw92e121gddpm1', 'n2yg87721pyw92e1jqzee3mq', 'n2yg87721pyw92e121dgzjj1', 'n2yg8772q75jn3v1gq7ddxyq', 'n2yg8772q75jn3v121gddpm1', 'n2yg8772q75jn3v1jqzee3mq', 'n2yg8772q75jn3v121dgzjj1', 'qj70zmeq10vz5nwllmokx3j1', 'q6504o3l10vz5nwllmokx3j1', 'qj70zmeq10vz5nwl1w4pm2oq', 'q6504o3l10vz5nwl1w4pm2oq', 'qj70zmeq10vz5nwlqoxpyepq', 'q6504o3l10vz5nwlqoxpyepq', 'qj70zmeq10vz5nwl1398vkd1', 'q6504o3l10vz5nwl1398vkd1'] 
    name_list = ['Survivor Facility_0 One Player', 'Survivor Facility_0 Two Players', 'Survivor Facility_0 Three Players', 'Survivor Facility_0 Four Players', 'Survivor Airport One Player', 'Survivor Airport Two Players', 'Survivor Airport Three Players', 'Survivor Airport Four Players', 'Survivor Homestead One Player', 'Survivor Homestead Two Players', 'Survivor Homestead Three Players', 'Survivor Homestead Four Players', 'Survivor Abandoned Prison Maximus One Player', 'Survivor Abandoned Prison Maximus Two Players', 'Survivor Abandoned Prison Maximus Three Players', 'Survivor Abandoned Prison Maximus Four Players', 'Survivor Library One Player', 'Survivor Library Two Players', 'Survivor Library Three Players', 'Survivor Library Four Players', 'Survivor Abandoned Facility Remake One Player', 'Survivor Abandoned Facility Remake Two Players', 'Survivor Abandoned Facility Remake Three Players', 'Survivor Abandoned Facility Remake Four Players', 'Survivor Forgotten Facility One Player', 'Survivor Forgotten Facility Two Players', 'Survivor Forgotten Facility Three Players', 'Survivor Forgotten Facility Four Players', 'Survivor Haunted Mansion One Player', 'Survivor Haunted Mansion Two Players', 'Survivor Haunted Mansion Three Players', 'Survivor Haunted Mansion Four Players', 'Survivor The Backrooms One Player', 'Survivor The Backrooms Two Players', 'Survivor The Backrooms Three Players', 'Survivor The Backrooms Four Players', 'Survivor School One Player', 'Survivor School Two Players', 'Survivor School Three Players', 'Survivor School Four Players', 'Survivor Nuclear Power Plant One Player', 'Survivor Nuclear Power Plant Two Players', 'Survivor Nuclear Power Plant Three Players', 'Survivor Nuclear Power Plant Four Players', 'Survivor Sewer Treatment Plant One Player', 'Survivor Sewer Treatment Plant Two Players', 'Survivor Sewer Treatment Plant Three Players', 'Survivor Sewer Treatment Plant Four Players', 'Survivor Laboratory Complex One Player', 'Survivor Laboratory Complex Two Players', 'Survivor Laboratory Complex Three Players', 'Survivor Laboratory Complex Four Players', 'Survivor Abandoned Facility Optimus One Player', 'Survivor Abandoned Facility Optimus Two Players', 'Survivor Abandoned Facility Optimus Three Players', 'Survivor Abandoned Facility Optimus Four Players', 'Survivor Arcade One Player', 'Survivor Arcade Two Players', 'Survivor Arcade Three Players', 'Survivor Arcade Four Players', 'Survivor Arctic Station One Player', 'Survivor Arctic Station Two Players', 'Survivor Arctic Station Three Players', 'Survivor Arctic Station Four Players', 'Survivor Sanctuary Zoo One Player', 'Survivor Sanctuary Zoo Two Players', 'Survivor Sanctuary Zoo Three Players', 'Survivor Sanctuary Zoo Four Players', 'Survivor Spaceship One Player', 'Survivor Spaceship Two Players', 'Survivor Spaceship Three Players', 'Survivor Spaceship Four Players', 'Survivor Ghost Town One Player', 'Survivor Ghost Town Two Players', 'Survivor Ghost Town Three Players', 'Survivor Ghost Town Four Players', 'Beast Facility_0 One Capture', 'Beast Facility_0 Two Captures', 'Beast Facility_0 Three Captures', 'Beast Facility_0 Four Captures', 'Beast Airport One Capture', 'Beast Airport Two Captures', 'Beast Airport Three Captures', 'Beast Airport Four Captures', 'Beast Homestead One Capture', 'Beast Homestead Two Captures', 'Beast Homestead Three Captures', 'Beast Homestead Four Captures', 'Beast Abandoned Prison Maximus One Capture', 'Beast Abandoned Prison Maximus Two Captures', 'Beast Abandoned Prison Maximus Three Captures', 'Beast Abandoned Prison Maximus Four Captures', 'Beast Library One Capture', 'Beast Library Two Captures', 'Beast Library Three Captures', 'Beast Library Four Captures', 'Beast Abandoned Facility Remake One Capture', 'Beast Abandoned Facility Remake Two Captures', 'Beast Abandoned Facility Remake Three Captures', 'Beast Abandoned Facility Remake Four Captures', 'Beast Forgotten Facility One Capture', 'Beast Forgotten Facility Two Captures', 'Beast Forgotten Facility Three Captures', 'Beast Forgotten Facility Four Captures', 'Beast Haunted Mansion One Capture', 'Beast Haunted Mansion Two Captures', 'Beast Haunted Mansion Three Captures', 'Beast Haunted Mansion Four Captures', 'Beast The Backrooms One Capture', 'Beast The Backrooms Two Captures', 'Beast The Backrooms Three Captures', 'Beast The Backrooms Four Captures', 'Beast School One Capture', 'Beast School Two Captures', 'Beast School Three Captures', 'Beast School Four Captures', 'Beast Nuclear Power Plant One Capture', 'Beast Nuclear Power Plant Two Captures', 'Beast Nuclear Power Plant Three Captures', 'Beast Nuclear Power Plant Four Captures', 'Beast Sewer Treatment Plant One Capture', 'Beast Sewer Treatment Plant Two Captures', 'Beast Sewer Treatment Plant Three Captures', 'Beast Sewer Treatment Plant Four Captures', 'Beast Laboratory Complex One Capture', 'Beast Laboratory Complex Two Captures', 'Beast Laboratory Complex Three Captures', 'Beast Laboratory Complex Four Captures', 'Beast Abandoned Facility Optimus One Capture', 'Beast Abandoned Facility Optimus Two Captures', 'Beast Abandoned Facility Optimus Three Captures', 'Beast Abandoned Facility Optimus Four Captures', 'Beast Arcade One Capture', 'Beast Arcade Two Captures', 'Beast Arcade Three Captures', 'Beast Arcade Four Captures', 'Beast Arctic Station One Capture', 'Beast Arctic Station Two Captures', 'Beast Arctic Station Three Captures', 'Beast Arctic Station Four Captures', 'Beast Sanctuary Zoo One Capture', 'Beast Sanctuary Zoo Two Captures', 'Beast Sanctuary Zoo Three Captures', 'Beast Sanctuary Zoo Four Captures', 'Beast Spaceship One Capture', 'Beast Spaceship Two Captures', 'Beast Spaceship Three Captures', 'Beast Spaceship Four Captures', 'Beast Ghost Town One Capture', 'Beast Ghost Town Two Captures', 'Beast Ghost Town Three Captures', 'Beast Ghost Town Four Captures', 'Survivor Backrooms (Halloween) One Player', 'Beast Backrooms (Halloween) One Capture', 'Survivor Backrooms (Halloween) Two Players', 'Beast Backrooms (Halloween) Two Captures', 'Survivor Backrooms (Halloween) Three Players', 'Beast Backrooms (Halloween) Three Captures', 'Survivor Backrooms (Halloween) Four Players', 'Beast Backrooms (Halloween) Four Captures']
    category_id_list = [ '7dg6l4gk', 'n2yg8772', 'wk65l5e2', 'qj70zmeq', 'q6504o3l', 'gq7ddxyq', 1, '21gddpm1', 2, 'jqzee3mq', 3, '21dgzjj1', 4]
    #print(len(id_list), len(name_list))
    print("done getting variables", time.perf_counter() - start)
LISTMAKER_1()

print("getting users data ...")
player_id_list = []
player_name_list = []
player_nation_list = []
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

async def fetch_api(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            data = await response.json()

            return {
                "url": url,
                "status": response.status,
                "data": data
            }

    except Exception as e:
        return {
            "url": url,
            "status": "error",
            "error": str(e)
        }

async def fetch_all_apis(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_api(session, url) for url in urls]
        return await asyncio.gather(*tasks)

def get_rest_api_data(urls):
    return asyncio.run(fetch_all_apis(urls))

if __name__ == "__main__":
    api_endpoints = [f"https://www.speedrun.com/api/v1/users/{i}" for i in player_id_list]

    data_list = get_rest_api_data(api_endpoints)

    for item in data_list:
        player_name_list.append(item["data"]["data"]["names"]["international"])
        if item["data"]["data"]["location"] == None :
            player_nation_list.append("None")
        else :
            player_nation_list.append(item["data"]["data"]["location"]["country"]["names"]["international"])
#print(len(player_id_list), len(player_name_list))
print("done getting players' name", time.perf_counter() - start)

print("ordering runs data ...")
categories_placement_count = []
category_data = {"id":0}
for i in all_runs :
    category_id = ""
    if category_id_list.index(i["run"]["category"]) == 0:
        for j in list(i["run"]["values"].values()):
            category_id += j
        category_id = i["run"]["category"] + category_id
        i["run"]["category"] = 0
    elif category_id_list.index(i["run"]["category"]) == 1:
        for j in list(i["run"]["values"].values()):
            if list(i["run"]["values"].values()).index(j) == 2:
                break
            else: category_id += j
        category_id = i["run"]["category"] + category_id
        i["run"]["category"] = 1
    else:
        for j in list(i["run"]["values"].values()):
            category_id += j
        if category_id_list.index(category_id[:8]) == 4:
            i["run"]["category"] = 0
        else:
            i["run"]["category"] = 1
    i["run"]["values"] = category_id
    for k in range(0, len(categories_placement_count)):
        if category_id in categories_placement_count[k]:
            categories_placement_count[k][category_id] += 1
            i["place"] = categories_placement_count[k][category_id]
            break
    else:
        category_data[category_id] = category_data.pop('id')
        category_data[category_id] = 1
        categories_placement_count.append(category_data)
        i["place"] = 1
        category_data = {"id":0}
#print(categories_placement_count, len(categories_placement_count))
print("done ordering runs", time.perf_counter() - start)

print("getting runs data ...")
run_stats_datas = []
ftf_run = {
    "name" : "name",
    "link" : "link",
    "gametype": 0,
    "category_type" : 0,
    "time" : 900,
    "placement" : 0,
    "total_run_in_category" : 0,
    "the_runners" : [],
    "random_count" : 0,
    "wr_val" : 0,
    "wr_value_per_person" : 3,
    "score" : 0
}

for i in all_runs:
    run_info = i["run"]
    count = 0
    placeholder_list = []
    R1 = R2 = 0
    ftf_run["name"] = name_list[id_list.index(run_info["values"])]
    ftf_run['link'] = run_info["weblink"]
    if run_info["category"] == 1 : ftf_run['gametype'] = 1
    ftf_run["time"] = run_info["times"]["primary_t"]
    ftf_run["placement"] = i["place"]
    for k in categories_placement_count:
        if run_info["values"] in k:
            ftf_run['total_run_in_category'] = k[run_info["values"]]
            break
    if run_info["category"] == 0:
        for p in run_info["players"]:
            if p["rel"] == "user":
                placeholder_list.append(player_name_list[player_id_list.index(p["id"])])
                count += 1
            else:
                ftf_run['random_count'] += 1
        ftf_run['the_runners'] = placeholder_list
    else:
        ftf_run['random_count'] = category_id_list[category_id_list.index(run_info["values"][-8:]) + 1]
    R1 = len(ftf_run['the_runners'])
    R2 = ftf_run['random_count']
    if i["place"] == 1: 
        ftf_run['wr_val'] = 1
        ftf_run['wr_value_per_person'] = 3/R1
    if run_info["values"][:8] in category_id_list :
        ftf_run['score'] = (ftf_run['total_run_in_category']/ftf_run['placement']) + ((150 - 10*R1)/ftf_run['time']) + (((R1 - R2) + 1)/5)
    else:
        ftf_run['score'] = (ftf_run['total_run_in_category']/ftf_run['placement'] + ((20*R2)/ftf_run['time']))
    run_stats_datas.append(ftf_run)

print(run_stats_datas)


player_stats = {
    "name" : "name",
    "country" : "country",
    "wr_count" : 0,
    "wr_value" : 0,
    "score" : 0,
    "most_value_run" : "run_name" 
}    
