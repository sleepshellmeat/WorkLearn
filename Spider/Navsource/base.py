from parse import Parse_Battleships
from save import SaveSql

url_dict = {
    'battleships': 'http://www.navsource.org/archives/01idx.htm',
    'aircraft_carriers': 'http://www.navsource.org/archives/02idx.htm',
    'escort_carriers': 'http://www.navsource.org/archives/03idx.htm',
    'cruisers': 'http://www.navsource.org/archives/04idx.htm',
    'destroyers': 'http://www.navsource.org/archives/05idx.htm',
    'DE_FFG_LCS': 'http://www.navsource.org/archives/06idx.htm',
    'submarines': 'http://www.navsource.org/archives/subidx.htm',
    'service_sessels': 'http://www.navsource.org/archives/auxidx.htm',
    'sealift': 'http://www.navsource.org/archives/09/80idx.htm',
    'amphibiors': 'http://www.navsource.org/archives/phibidx.htm',
    'mine_warfare': 'http://www.navsource.org/archives/mineidx.htm',
    'patrol_vessels': 'http://www.navsource.org/archives/patidx.htm',
    'yard_district': 'http://www.navsource.org/archives/ydidx.htm',
    'civilian_vessels': 'http://www.navsource.org/archives/12/17idx.htm',
    'steam_sailIndex': 'http://www.navsource.org/archives/09/86/86idx.htm',
    'rigid_airships': 'http://www.navsource.org/archives/02/99/0299idx.htm',
    'army_ships': 'http://www.navsource.org/archives/armyidx.htm'
}

def main():
    parse = Parse_Battleships(url=url_dict['battleships'])
    reponse = parse.get_first_href()
    print(reponse)
    print(len(reponse))
    print(type(reponse))


if __name__ == '__main__':
    main()

