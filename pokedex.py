from termcolor import colored

pokemon_database = [
    {'id': 1, 'name': 'Bulbasaur', 'type': 'Grass/Poison', 'evolves_from': None, 'evolves_into': 'Ivysaur', 'region': 'Kanto'},
    {'id': 2, 'name': 'Ivysaur', 'type': 'Grass/Poison', 'evolves_from': 'Bulbasaur', 'evolves_into': 'Venusaur', 'region': 'Kanto'},
    {'id': 3, 'name': 'Venusaur', 'type': 'Grass/Poison', 'evolves_from': 'Ivysaur', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 4, 'name': 'Charmander', 'type': 'Fire', 'evolves_from': None, 'evolves_into': 'Charmeleon', 'region': 'Kanto'},
    {'id': 5, 'name': 'Charmeleon', 'type': 'Fire', 'evolves_from': 'Charmander', 'evolves_into': 'Charizard', 'region': 'Kanto'},
    {'id': 6, 'name': 'Charizard', 'type': 'Fire/Flying', 'evolves_from': 'Charmeleon', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 7, 'name': 'Squirtle', 'type': 'Water', 'evolves_from': None, 'evolves_into': 'Wartortle', 'region': 'Kanto'},
    {'id': 8, 'name': 'Wartortle', 'type': 'Water', 'evolves_from': 'Squirtle', 'evolves_into': 'Blastoise', 'region': 'Kanto'},
    {'id': 9, 'name': 'Blastoise', 'type': 'Water', 'evolves_from': 'Wartortle', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 10, 'name': 'Caterpie', 'type': 'Bug', 'evolves_from': None, 'evolves_into': 'Metapod', 'region': 'Kanto'},
    {'id': 11, 'name': 'Metapod', 'type': 'Bug', 'evolves_from': 'Caterpie', 'evolves_into': 'Butterfree', 'region': 'Kanto'},
    {'id': 12, 'name': 'Butterfree', 'type': 'Bug/Flying', 'evolves_from': 'Metapod', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 13, 'name': 'Weedle', 'type': 'Bug/Poison', 'evolves_from': None, 'evolves_into': 'Kakuna', 'region': 'Kanto'},
    {'id': 14, 'name': 'Kakuna', 'type': 'Bug/Poison', 'evolves_from': 'Weedle', 'evolves_into': 'Beedrill', 'region': 'Kanto'},
    {'id': 15, 'name': 'Beedrill', 'type': 'Bug/Poison', 'evolves_from': 'Kakuna', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 16, 'name': 'Pidgey', 'type': 'Normal/Flying', 'evolves_from': None, 'evolves_into': 'Pidgeotto', 'region': 'Kanto'},
    {'id': 17, 'name': 'Pidgeotto', 'type': 'Normal/Flying', 'evolves_from': 'Pidgey', 'evolves_into': 'Pidgeot', 'region': 'Kanto'},
    {'id': 18, 'name': 'Pidgeot', 'type': 'Normal/Flying', 'evolves_from': 'Pidgeotto', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 19, 'name': 'Rattata', 'type': 'Normal', 'evolves_from': None, 'evolves_into': 'Raticate', 'region': 'Kanto'},
    {'id': 20, 'name': 'Raticate', 'type': 'Normal', 'evolves_from': 'Rattata', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 21, 'name': 'Spearow', 'type': 'Normal/Flying', 'evolves_from': None, 'evolves_into': 'Fearow', 'region': 'Kanto'},
    {'id': 22, 'name': 'Fearow', 'type': 'Normal/Flying', 'evolves_from': 'Spearow', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 23, 'name': 'Ekans', 'type': 'Poison', 'evolves_from': None, 'evolves_into': 'Arbok', 'region': 'Kanto'},
    {'id': 24, 'name': 'Arbok', 'type': 'Poison', 'evolves_from': 'Ekans', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 25, 'name': 'Pikachu', 'type': 'Electric', 'evolves_from': None, 'evolves_into': 'Raichu', 'region': 'Kanto'},
    {'id': 26, 'name': 'Raichu', 'type': 'Electric', 'evolves_from': 'Pikachu', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 27, 'name': 'Sandshrew', 'type': 'Ground', 'evolves_from': None, 'evolves_into': 'Sandslash', 'region': 'Kanto'},
    {'id': 28, 'name': 'Sandslash', 'type': 'Ground', 'evolves_from': 'Sandshrew', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 29, 'name': 'Nidoran♀', 'type': 'Poison', 'evolves_from': None, 'evolves_into': 'Nidorina', 'region': 'Kanto'},
    {'id': 30, 'name': 'Nidorina', 'type': 'Poison', 'evolves_from': 'Nidoran♀', 'evolves_into': 'Nidoqueen', 'region': 'Kanto'},
    {'id': 31, 'name': 'Nidoqueen', 'type': 'Poison/Ground', 'evolves_from': 'Nidorina', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 32, 'name': 'Nidoran♂', 'type': 'Poison', 'evolves_from': None, 'evolves_into': 'Nidorino', 'region': 'Kanto'},
    {'id': 33, 'name': 'Nidorino', 'type': 'Poison', 'evolves_from': 'Nidoran♂', 'evolves_into': 'Nidoking', 'region': 'Kanto'},
    {'id': 34, 'name': 'Nidoking', 'type': 'Poison/Ground', 'evolves_from': 'Nidorino', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 35, 'name': 'Clefairy', 'type': 'Fairy', 'evolves_from': None, 'evolves_into': 'Clefable', 'region': 'Kanto'},
    {'id': 36, 'name': 'Clefable', 'type': 'Fairy', 'evolves_from': 'Clefairy', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 37, 'name': 'Vulpix', 'type': 'Fire', 'evolves_from': None, 'evolves_into': 'Ninetales', 'region': 'Kanto'},
    {'id': 38, 'name': 'Ninetales', 'type': 'Fire', 'evolves_from': 'Vulpix', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 39, 'name': 'Jigglypuff', 'type': 'Normal/Fairy', 'evolves_from': None, 'evolves_into': 'Wigglytuff', 'region': 'Kanto'},
    {'id': 40, 'name': 'Wigglytuff', 'type': 'Normal/Fairy', 'evolves_from': 'Jigglypuff', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 41, 'name': 'Zubat', 'type': 'Poison/Flying', 'evolves_from': None, 'evolves_into': 'Golbat', 'region': 'Kanto'},
    {'id': 42, 'name': 'Golbat', 'type': 'Poison/Flying', 'evolves_from': 'Zubat', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 43, 'name': 'Oddish', 'type': 'Grass/Poison', 'evolves_from': None, 'evolves_into': 'Gloom', 'region': 'Kanto'},
    {'id': 44, 'name': 'Gloom', 'type': 'Grass/Poison', 'evolves_from': 'Oddish', 'evolves_into': 'Vileplume', 'region': 'Kanto'},
    {'id': 45, 'name': 'Vileplume', 'type': 'Grass/Poison', 'evolves_from': 'Gloom', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 46, 'name': 'Paras', 'type': 'Bug/Grass', 'evolves_from': None, 'evolves_into': 'Parasect', 'region': 'Kanto'},
    {'id': 47, 'name': 'Parasect', 'type': 'Bug/Grass', 'evolves_from': 'Paras', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 48, 'name': 'Venonat', 'type': 'Bug/Poison', 'evolves_from': None, 'evolves_into': 'Venomoth', 'region': 'Kanto'},
    {'id': 49, 'name': 'Venomoth', 'type': 'Bug/Poison', 'evolves_from': 'Venonat', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 50, 'name': 'Diglett', 'type': 'Ground', 'evolves_from': None, 'evolves_into': 'Dugtrio', 'region': 'Kanto'},
    {'id': 51, 'name': 'Dugtrio', 'type': 'Ground', 'evolves_from': 'Diglett', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 52, 'name': 'Meowth', 'type': 'Normal', 'evolves_from': None, 'evolves_into': 'Persian', 'region': 'Kanto'},
    {'id': 53, 'name': 'Persian', 'type': 'Normal', 'evolves_from': 'Meowth', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 54, 'name': 'Psyduck', 'type': 'Water', 'evolves_from': None, 'evolves_into': 'Golduck', 'region': 'Kanto'},
    {'id': 55, 'name': 'Golduck', 'type': 'Water', 'evolves_from': 'Psyduck', 'evolves_into': None, 'region': 'Kanto'},
    {'id': 56, 'name': 'Mankey', 'type': 'Fighting', 'evolves_from': None, 'evolves_into': 'Primeape', 'region': 'Kanto'},
    {'id': 57, 'name': 'Primeape', 'type': 'Fighting', 'evolves_from': 'Mankey', 'evolves_into': None, 'region': 'Kanto'},
]

input_index = 0
def get_input(prompt):
    print(colored(prompt, 'cyan'))
    return input().strip()

def display_pokemon(pokemon):
    print(colored(f"ID: {pokemon['id']}", 'green'))
    print(colored(f"Name: {pokemon['name']}", 'yellow'))
    print(colored(f"Type: {pokemon['type']}", 'blue'))
    print(colored(f"Evolves From: {pokemon['evolves_from']}", 'magenta'))
    print(colored(f"Evolves Into: {pokemon['evolves_into']}", 'magenta'))
    print(colored(f"Region: {pokemon['region']}", 'red'))
    print(colored('---', 'white'))

while True:
    print(colored("""Welcome to the Pokedex!fff
                  
  
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.           
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
                                
                                """, 'green', attrs=['bold']))
    
    
    print(colored("1. View all Pokémon", 'cyan'))
    print(colored("2. Search for a Pokémon", 'cyan'))
    print(colored("3. Add a new Pokémon", 'cyan'))
    print(colored("4. Exit", 'cyan'))
    choice = get_input("Enter your choice: ")

    if choice == "1":
        for pokemon in pokemon_database:
            display_pokemon(pokemon)

    elif choice == "2":
        name = get_input("Enter the Pokémon name: ").strip().lower()
        found = False
        for pokemon in pokemon_database:
            if pokemon['name'].lower() == name:
                display_pokemon(pokemon)
                found = True
                break
        if not found:
            print(colored("Pokémon not found.", 'red'))

    elif choice == "3":
        id = int(get_input("Enter ID: "))
        name = get_input("Enter Name: ").capitalize()
        type = get_input("Enter Type: ")
        evolves_from = get_input("Enter Evolves From (or None): ")
        evolves_into = get_input("Enter Evolves Into (or None): ")
        region = get_input("Enter Region: ").capitalize()
        pokemon_database.append({
            'id': id,
            'name': name,
            'type': type,
            'evolves_from': evolves_from if evolves_from.lower() != "none" else None,
            'evolves_into': evolves_into if evolves_into.lower() != "none" else None,
            'region': region
        })
        print(colored("Pokémon added successfully!", 'green'))

    elif choice == "4":
        print(colored("Exiting Pokedex. Goodbye!", 'yellow'))
        break

    else:
        print(colored("Invalid choice. Please try again.", 'red'))
