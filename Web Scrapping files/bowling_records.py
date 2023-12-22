import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2022-23-14450"
# url="https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2021-22-14024"
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
    balls = columns[4].text.strip()
    overs = columns[5].text.strip()
    maidens = columns[6].text.strip()
    runs = columns[7].text.strip()
    wkts = columns[8].text.strip()
    bbi = columns[9].text.strip()
    bbm = columns[10].text.strip()
    avg = columns[11].text.strip()
    econ = columns[12].text.strip()
    SR = columns[13].text.strip()
    four = columns[14].text.strip()
    fifer = columns[15].text.strip()
    # Do whatever you want with the extracted data
    # print("player: ", player)
    # print("span: ", span)
    # print("matches:", mat)
    # print("innings:", innis)
    # print("balls:", balls)
    # print("Overs:",overs)
    # print("maidens:", maidens)
    # print("runs:", runs )
    # print("wkts:", wkts)
    # print("BBI:", bbi)
    # print("BBM:", bbm)
    # print("Avg:",avg )
    # print("Econ:", econ)
    # print("SR:", SR)
    # print("FOUR WIC:", four)
    # print("fifer:", fifer)

    # print("--------------------")
    table_data.append([player,span, mat, innis, balls, overs, maidens, runs, wkts,bbi, bbm, avg,  econ, SR, four, fifer])

with open("bowling_records2.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Player", "span", "matches", "innings", "balls", "overs", "maidens", "runs", "wickets", "BBI", "BBM", "average", "economy", "strike rate", "four wicket haul","fifer"])
    for row in table_data:
        csvwriter.writerow(row)