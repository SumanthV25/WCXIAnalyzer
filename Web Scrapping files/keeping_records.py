import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.espncricinfo.com/records/tournament/keeping-most-dismissals-career/icc-men-s-t20-world-cup-2022-23-14450"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", class_="engineTable")

body = soup.find("tbody")

rows = body.find_all("tr")
table_data = []

for row in rows: 
    
    columns = row.find_all("td")
    player = columns[0].text.strip()
    span = columns[1].text.strip()
    mat = columns[2].text.strip()
    innis = columns[3].text.strip()
    dissmisals = columns[4].text.strip()
    catches = columns[5].text.strip()
    stumping = columns[6].text.strip()
    maxdisperinn = columns[7].text.strip()
    disperinn =  columns[8].text.strip()
    # print("player: ", player)
    # print("span: ", span)
    # print("matches:", mat)
    # print("innings:", innis)
    # print("dismissals:", dissmisals)
    # print("catches:", catches)
    # print("stumpings: ", stumping)
    # print("max dismissals in innings:", maxdisperinn)
    # print("dismissals/innings",disperinn )
    # print("--------------------")
    table_data.append([player,span, mat, innis, dissmisals, catches, stumping,maxdisperinn,disperinn])

with open("keeping_records2.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Player", "span", "matches", "innings", "dismissals", "catches","stumpings", "max dismissals in innings", "dismissals/innings"])
    for row in table_data:
        csvwriter.writerow(row)
