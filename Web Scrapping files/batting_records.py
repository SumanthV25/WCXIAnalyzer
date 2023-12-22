import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2022-23-14450"
# url ="https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2021-22-14024"
response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")


table = soup.find("table", class_="ds-w-full ds-table ds-table-xs ds-table-auto  ds-w-full ds-overflow-scroll ds-scrollbar-hide")

body = soup.find("tbody")


rows = body.find_all("tr")
table_data = []

for row in rows:  
    columns = row.find_all("td")
    player = columns[0].text.strip()
    span = columns[1].text.strip()
    mat = columns[2].text.strip()
    innis = columns[3].text.strip()
    notout = columns[4].text.strip()
    runs = columns[5].text.strip()
    highscore = columns[6].text.strip()
    avg = columns[7].text.strip()
    ballsfaced = columns[8].text.strip()
    strikerate = columns[9].text.strip()
    hundreds = columns[10].text.strip()
    fifties = columns[11].text.strip()
    ducks = columns[12].text.strip()
    fours = columns[13].text.strip()
    sixes = columns[14].text.strip()
    
    print("player: ", player)
    print("span: ", span)
    print("matches:", mat)
    print("innings:", innis)
    print("NO:", notout)
    print("runs:",runs)
    print("high score:", highscore)
    print("average:", avg )
    print("ballsfaced:", ballsfaced)
    print("strikerate:", strikerate)
    print("hundreds:", hundreds)
    print("fifties:",fifties )
    print("ducks:", ducks)
    print("fours:", fours)
    print("sixes:", sixes)

    print("--------------------")

    
#     table_data.append([player,span, mat, innis, notout, runs, highscore,avg, ballsfaced, strikerate, hundreds, fifties,ducks,fours, sixes])


# with open("batting_records2.csv", "w", newline="") as csvfile:

#     csvwriter = csv.writer(csvfile, delimiter=",")

    
#     csvwriter.writerow(["Player","span","matches","innings","not outs","runs","highscore","average","balls faced","strikerate","hundreds","fifties","ducks","fours","sixes"])


    
#     for row in table_data:
#         csvwriter.writerow(row)
