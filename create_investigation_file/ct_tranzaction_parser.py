from open_write import open_csv
from create_investigation_file.time_operation import find_diference_time, check_time



def obtain_data_from_ct_tranz(file_csv, timp1):
    timp1.format("%d.%m.%Y %H:%M:%S")
    data = open_csv(file_csv)
    t1,t2, delta, id_start, id_end = obtain_start_game(data, timp1)
    games_played = obtain_number_played_games(id_start, id_end, data)
    game_name = obtain_name_played_games(id_start, id_end, data)
    bet = obtain_bets(id_start, id_end, data)
    wins_game = obtian_game_wins(id_start, id_end, data)
    return games_played, game_name, bet, wins_game, t2, delta



def obtain_start_game(data, timp1):
    id_start, t1 = shearch_remote_in(data, timp1)
    id_end, t2 = shearch_end_sesion(data, id_start)
    delta = find_diference_time(t1,t2)
    return t1,t2, delta, id_start, id_end


def shearch_remote_in(data, timp1):

    for i in range(1,6):
        timp1, timp_plus, timp_minus = check_time(timp1, i)

        for element in data:
            if timp1 == element["time"] and "Remote-In" in element["action"]:
                t1 = element["time"]
                id_start = element["id"]
                break
            elif timp_plus == element["time"] and "Remote-In" in element["action"]:
                t1 = element["time"]
                id_start = element["id"]
                break
            elif timp_minus == element["time"] and "Remote-In" in element["action"]:
                t1 = element["time"]
                id_start = element["id"]
                break
            else: pass

    return id_start, t1

def shearch_end_sesion(data, id_start):
    for element in data:
        if int(element["id"]) > int(id_start):
            if "Handpay" in element["action"]:
                id = int(element["id"])
                break
            elif "Remote-In" in element["action"]:
                id = int(element["id"])-1
                break
            elif "End of Business Day" in element["action"]:
                id = int(element["id"])-1
                break
    id_end, t2 = find_end_session(id, data)
    return id_end, t2
            
def find_end_session(id, data):
    for el in data:
        if id == int(el["id"]):
            id_end = int(el["id"])
            t2 = el["time"]

    return id_end, t2


def obtain_number_played_games(id_start, id_end, data):
    games_played = 0

    for element in data:
        if int(id_start) < int(element["id"]) < int(id_end):
            if "Game-Start" in element["action"]:
                games_played = games_played + 1
    return games_played

def obtain_name_played_games(id_start, id_end, data):
    game_name = []

    for element in data:
        if int(id_start) < int(element["id"]) < int(id_end):
            if "Game" in element["description"]:
                nume = element["description"][6:]
                if nume not in game_name:
                    game_name.append(nume)
    return game_name

def obtain_bets(id_start, id_end, data):
    bet = []

    for element in data:
        if int(id_start) < int(element["id"]) < int(id_end):
            if "Game-Start" in element["action"]:
                if element["amount"] not in bet:
                    bet.append(element["amount"])
    return bet

def obtian_game_wins(id_start, id_end, data):
    wins_game = []
    for element in data:
        if int(id_start) < int(element["id"]) < int(id_end):
            if element["action"] == "Game-End":
                try:
                    amount = float(element["amount"].replace(".",""))
                    if amount >= 500000:
                        if element["description"][6:] not in wins_game:
                            wins_game.append(element["description"][6:])
                except ValueError:
                    # Handle the case where conversion to float fails
                    pass
    return wins_game