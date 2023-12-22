import requests
from bs4 import BeautifulSoup

# url = "https://www.espncricinfo.com/records/season/team-match-results/2022to23-2022to23?trophy=89"
url = "https://www.espncricinfo.com/records/season/team-match-results/2021to22-2021to22?trophy=89"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", class_="engineTable")
body = soup.find("tbody")
rows = body.find_all("tr")

for row in rows:  
    columns = row.find_all("td")
    team1 = columns[0].text.strip()
    team2 = columns[1].text.strip()
    winner = columns[2].text.strip()
    margin = columns[3].text.strip()
    ground = columns[4].text.strip()
    match_date = columns[5].text.strip()
    scorecard = columns[6].find("a")["href"]

    print("Team 1:", team1)
    print("Team 2:", team2)
    print("Winner:", winner)
    print("Margin:", margin)
    print("Ground:", ground)
    print("Match Date:", match_date)
    print("Scorecard:", scorecard)
    print("--------------------")
