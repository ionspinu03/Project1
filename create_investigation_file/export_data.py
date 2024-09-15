from create_investigation_file.verivy_if_file_exist import check_if_file_exists
from create_investigation_file.ct_tranzaction_parser import obtain_data_from_ct_tranz
from open_write import write_to_xlsx_file


def process_element(element):
    if not element["Seria aparatului"].startswith(("Depunere", "Plata")):
        date = element["Data"]
        timp1 = " " + element["Time Stamp"]
        locatia = element["Locatia"]
        adj = element["Seria aparatului"]

        if check_if_file_exists(date, locatia, adj):
            file_csv = f"rezultat/{date} {locatia} {adj}.csv"
            games_played, game_name, bet, wins_game, t2, delta = obtain_data_from_ct_tranz(file_csv, timp1)
            element["Ora plata"] = t2[12:]
            element["Jocuri jucate"] = games_played
            element["Jocul de Start"] = ", ".join(game_name)
            element["Jucul castigator"] = ", ".join(wins_game)
            element["Mizele jucate"] = ", ".join(bet)
            element["Timp pentrecut in joaca"] = delta
            element["Real POP by Game %"] = ""
            element["Real POP by GMT"] = ""
        else:
            print(f"File {date} {locatia} {adj} not exists")


def export(data, valid):

    for element in valid:
        process_element(element)


    if data:
        player_name = data[0].get("Player Name", "Unknown")
        player_id = data[0].get("Player Id", "Unknown")
    else:
        player_name = "Unknown"
        player_id = "Unknown"

    # Creăm și salvăm fișierul Excel
    file_write_xlsx = f"rezultat/Investigatii/Investigare {player_id} {player_name}.xlsx"
    print(f"[+] A fost Exportat in directoriul: {file_write_xlsx}")
    directory = "rezultat/Investigatii"
    write_to_xlsx_file(file_write_xlsx, valid, directory)
    return file_write_xlsx


if __name__ == "__main__":
    pass
