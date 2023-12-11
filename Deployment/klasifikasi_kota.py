import pickle
import pandas as pd

def klasifikasi_kota(kota):
    if pd.isna(kota):
        pass
    elif kota in ["Armadale" , "Ashendon", "Bedfordale" ,'Brookdale', 'Camillo', 'Champion Lakes', 'Forrestdale', 'Harrisdale', 'Haynes', 'Hilbert', 
                  'Karragullen', 'Kelmscott', 'Mount Nasura', 'Mount Richon', 'Piara Waters', 'Roleystone', 'Seville Grove', 'Wungong']:
        return 1
    elif kota in ['Eden Hill', 'Bassendean', 'Ashfield']:
        return 2
    elif kota in ['Bayswater', 'Bedford', 'Dianella', 'Embleton', 'Maylands', 'Morley', 'Noranda']:
        return 3
    elif kota in ['Ascot', 'Belmont', 'Cloverdale','Kewdale', 'Perth Airport', 'Redcliffe', 'Rivervale']:
        return 4
    elif kota in ['Bunbury']:
        return 5
    elif kota in ['Busselton']:
        return 6
    elif kota in ['City Beach', 'Daglish', 'Floreat', 'Wembley', 'West Leederville']:
        return 7
    elif kota in ['Bentley', 'Cannington', 'Canning Vale', 'East Cannington', 'Ferndale', 'Lynwood', 'Parkwood', 'Queens Park', 'Riverton', 
                  'Rossmoyne', 'Shelley', 'Welshpool', 'Willetton', 'Wilson', 'Mount Claremont']:
        return 8
    elif kota in ['Claremont', 'Swanbourne']:
        return 9
    elif kota in ['Atwell', 'Aubin Grove', 'Banjup', 'Beeliar', 'Bibra Lake', 'Coogee', 'Coolbellup', 'Hamilton Hill', 'Hammond Hill', 'Henderson','Treeby', 
                  'Jandakot', 'Munster', 'North Lake','South Lake', 'Spearwood', 'Success','Wattleup', 'Yangebup', 'Hammond Park','North Coogee','Cockburn Central']:
        return 10
    elif kota in ['Cottesloe']:
        return 11
    elif kota in ['East Fremantle']:
        return 12
    elif kota in ['Beaconsfield', 'Fremantle', 'Hilton', 'North Fremantle', "O'Connor", 'Samson', 'South Fremantle', 'White Gum Valley']:
        return 13
    elif kota in ['Beckenham', 'Gosnells', 'Huntingdale', 'Kenwick', 'Langford', 'Maddington', 'Martin', 'Orange Grove', 'Southern River', 'Thornlie']:
        return 14
    elif kota in ['Beldon', 'Burns Beach', 'Connolly', 'Craigie', 'Currambine', 'Duncraig', 'Edgewater', 'Greenwood', 'Heathridge', 'Hillarys', 'Iluka', 'Joondalup', 'Kallaroo', 
                  'Kingsley', 'Kinross', 'Marmion', 'Mullaloo', 'Ocean Reef', 'Padbury', 'Sorrento', 'Warwick', 'Woodvale']:
        return 15
    elif kota in ['Bickley', 'Canning Mills', 'Carmel', 'Forrestfield', 'Gooseberry Hill', 'Hacketts Gully', 'High Wycombe', 'Kalamunda', 'Lesmurdie', 'Maida Vale', 'Paulls Valley', 
                  'Pickering Brook', 'Piesse Brook', 'Walliston', 'Wattle Grove']:
        return 16
    elif kota in ['Anketell', 'Bertram', 'Calista', 'Casuarina', 'Hope Valley', 'Kwinana', 'Leda', 'Mandogalup', 'Medina', 'Orelia', 'Parmelia', 'Postans', 'The Spectacles', 'Naval Base', 
                  'Wandi', 'Wellard','Kwinana Town Centre','Kwinana Beach']:
        return 17
    elif kota in ['Mandurah']:
        return 18
    elif kota in ['Alfred Cove', 'Applecross','Ardross', 'Attadale', 'Bateman', 'Bicton', 'Booragoon', 'Brentwood', 'Bull Creek', 'Kardinya', 'Leeming', 'Melville', 'Mt Pleasant', 'Murdoch', 'Myaree', 
                  'Palmyra','Willagee',' Winthrop','Mount Pleasant','Winthrop']:
        return 19
    elif kota in ['Mosman Park']:
        return 20
    elif kota in ['Bailup', 'Beechina', 'Boya', 'Chidlow', 'Darlington', 'Glen Forrest', 'Gorrie', 'Greenmount', 'Helena Valley', 'Hovea', 'Mahogany Creek', 'Mt Helena', 'Mundaring', 
                  'Parkerville', 'Sawyers Valley','Stoneville','Swan View', 'The Lakes', 'Wooroloo','Mount Helena']:
        return 21
    elif kota in ['Banksiadale', 'Barragup', 'Birchmont', 'Blythewood', 'Coolup', 'Dwellingup', 'Etmilyn', 'Fairbridge', 'Furnissdale', 'Holyoake', 'Inglehope', 'Keralup', 'Keysbrook', 'Marrinup', 
                  'Meelon', 'Myara', 'Nambeelup', 'Nirimba', 'North Dandalup', 'North Yunderup', 'Oakley', 'Pinjarra', 'Point Grey', 'Ravenswood', 'Solus', 'South Yunderup', 
                  'Stake Hill', 'Teesdale', 'West Coolup', 'West Pinjarra', 'Whittaker']:
        return 22
    elif kota in ['Dalkeith', 'Karrakatta', 'Mt Claremont', 'Nedlands', 'Swanbourne']:
        return 23
    elif kota in ['Bakers Hill', 'Clackline', 'Northam', 'Spencers Brook', 'Wundowie']:
        return 24
    elif kota in ['Peppermint Grove']:
        return 25
    elif kota in ['East Perth', 'Kings Park', 'Northbridge', 'Perth City', 'West Perth']:
        return 26
    elif kota in ['Mount Barker', 'Kendenup', 'Narrikup', 'Rocky Gully', 'Porongurup']:
        return 27
    elif kota in ['Baldivis', 'Cooloongup', 'East Rockingham', 'Golden Bay', 'Hillman', 'Karnup', 'Peron', 'Port Kennedy', 'Rockingham', 'Safety Bay', 'Secret Harbour', 
                  'Shoalwater', 'Singleton', 'Waikiki', 'Warnbro']:
        return 28
    elif kota in ['Byford', 'Cardup', 'Darling Downs', 'Hopeland', 'Jarrahdale', 'Karrakup', 'Mardella', 'Mundijong', 'Oakbury', 'Oldbury', 'Serpentine', 'Whitby','Oakford']:
        return 29
    elif kota in ['Como', 'Karawara', 'Kensington', 'Manning', 'Salter Point', 'South Perth', 'Waterford']:
        return 30
    elif kota in ['Balcatta', 'Balga', 'Carine', 'Churchlands', 'Coolbinia', 'Dianella', 'Doubleview', 'Glendalough', 'Gwelup', 'Hamersley', 'Herdsman', 'Inglewood', 'Innaloo', 
                  'Joondanna', 'Karrinyup', 'Menora', 'Mirrabooka', 'Mt Lawley', 'Nollamara', 'North Beach', 'Osborne Park', 'Scarborough', 'Stirling', 'Trigg', 'Tuart Hill', 
                  'Watermans Bay', 'Wembley Downs',  'Westminster', 'Woodlands', 'Yokine','Mount Lawley']:
        return 31
    elif kota in ['Crawley', 'Daglish', 'Jolimont', 'Shenton Park', 'Subiaco']:
        return 32
    elif kota in ['Aveley', 'Ballajura', 'Baskerville', 'Beechboro', 'Belhus', 'Bellevue', 'Bennett Springs', 'Brabham', 'Brigadoon', 'Bullsbrook' , 'Caversham', 'Cullacabardee', 'Dayton', 'Ellenbrook', 
                  'Gidgegannup', 'Guildford', 'Hazelmere', 'Henley Brook', 'Herne Hill', 'Jane Brook', 'Kiara', 'Koongamia', 'Lexia', 'Lockridge', 'Malaga', 'Melaleuca', 'Middle Swan', 'Midland', 
                  'Midvale', 'Millendon', 'Noranda', 'Perth Airport', 'Red Hill','South Guildford', 'Stratton', 'The Vines', 'Upper Swan', 'Valley Ridge', 'Viveash' ,'West Swan', 'Whiteman', 'Woodbridge']:
        return 33
    elif kota in ['Burswood', 'Carlisle', 'East Victoria Park', 'Lathlain', 'St James', 'Victoria Park']:
        return 34
    elif kota in ['Highgate', 'Leederville', 'Mt Hawthorn', 'North Perth']:
        return 35
    elif kota in ['Alexander Heights', 'Alkimos', 'Ashby', 'Banksia Grove', 'Butler', 'Carabooda', 'Carramar', 'Clarkson', 'Darch', 'Eglinton', 'Girrawheen', 'Gnangara', 'Hocking', 'Jandabup', 'Jindalee', 
                  'Koondoola', 'Landsdale', 'Madeley', 'Marangaroo', 'Mariginiup', 'Merriwa', 'Mindarie', 'Neerabup','Nowergup', 'Pearsall', 'Pinjar', 'Quinns Rocks', 'Ridgewood', 'Sinagra', 'Tamala Park', 
                  'Tapping', 'Two Rocks', 'Wangara', 'Wanneroo', 'Yanchep','Mount Hawthorn']:
        return 36

with open('klasifikasi_kota.pkl', 'wb') as file_2:
    pickle.dump(klasifikasi_kota, file_2)