
import requests
from bs4 import BeautifulSoup

def parse_stat_by_id(soup, stat_id):
    el = soup.find("span", id=stat_id)
    return el.text.strip().replace(",", "") if el else "N/A"

def get_world_data():
    url = "https://www.worldometers.info/world-population/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    return {
        "Population Actuelle": soup.find("div", class_="maincounter-number").text.strip(),
        "Naissances Aujourd'hui": parse_stat_by_id(soup, "births_today"),
        "Naissances cette année": parse_stat_by_id(soup, "births_this_year"),
        "Décès Aujourd'hui": parse_stat_by_id(soup, "dth1s_today"),
        "Décès cette année": parse_stat_by_id(soup, "dth1s_this_year"),
        "Croissance nette aujourd'hui": parse_stat_by_id(soup, "population_growth_today"),
        "Croissance nette cette année": parse_stat_by_id(soup, "population_growth_this_year")
    }

def get_country_data(country):
    url = f"https://www.worldometers.info/world-population/{country.replace(' ', '-').lower()}/"
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        pop_block = soup.find("div", class_="col-md-8 country-pop-description")
        if pop_block:
            return {
                "Population": pop_block.find("strong").text.strip()
            }
    except:
        pass
    return {"Population": "Donnée indisponible"}
