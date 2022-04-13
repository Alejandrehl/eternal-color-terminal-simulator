import requests
from bs4 import BeautifulSoup
import pandas as pd

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("Starting Scrapper")
for i in range (0, 10000000000):
    print(bcolors.HEADER + "Alejandro Exequiel Hernández Lara" + bcolors.HEADER)
    print(bcolors.OKBLUE + "ROMPEPARADIGMAS" + bcolors.OKBLUE)
    print(bcolors.OKCYAN + "ROMPEPARADIGMAS" + bcolors.OKCYAN)
    print(bcolors.OKGREEN + "ROMPEPARADIGMAS" + bcolors.OKGREEN)
    print(bcolors.WARNING + "Alejandro Exequiel Hernández Lara" + bcolors.WARNING)
    print(bcolors.FAIL + "ROMPEPARADIGMAS" + bcolors.FAIL)
    print(bcolors.ENDC + "Alejandro Exequiel Hernández Lara" + bcolors.ENDC)
    print(bcolors.BOLD + "ROMPEPARADIGMAS" + bcolors.BOLD)
    print(bcolors.UNDERLINE + "ROMPEPARADIGMAS" + bcolors.UNDERLINE)

gob_url = "https://www.enquefase.cl/region/metropolitana-de-santiago"

percentage_url = "https://www.enquefase.cl/"

r = requests.get(gob_url)
percentage_request = requests.get(percentage_url)

data = r.text
data_percentage_url = percentage_request.text

soup = BeautifulSoup(data, "html.parser")
soup_percentage_url = BeautifulSoup(data_percentage_url, "html.parser")

names = []
phases = []
states = []
communes = []

percentages = []
percentage_phases = []
percentage_values = []

infoTable = soup.find("tbody")
info_percentages = soup_percentage_url.find("div", attrs={"class": "col-xl-12 col-xxl-12 col-md-12"})

print("Scrapping https://www.enquefase.cl/region/metropolitana-de-santiago")
for listing in infoTable.find_all("tr"):
    name = listing.find("a").text
    print(name)
    phase = listing.find_all("td")[1].text
    print(name)
    state = listing.find("span").text
    print(name)

    names.append(name)
    phases.append(phase)
    states.append(state)

    newCommune = {"name": name, "phase": phase, "state": state}
    print(newCommune)
    communes.append(newCommune)

df = pd.DataFrame({
    "Comuna": names,
    "Fase": phases,
    "Estado": states
})

print("Scrapping https://www.enquefase.cl/")
for listing_percentage in info_percentages.find_all("div", attrs={"class": "col-sm-3 mb-4 col-6"}):
    phase_name = listing_percentage.find("span", attrs={"class": "fs-14 d-block"}).text
    print(phase_name)
    percentage = listing_percentage.find("small").text
    print(phase_name)

    percentage_phases.append(phase_name)
    percentage_values.append(percentage)

    newPercentage = {"name": phase_name, "percentage": percentage}
    print(newPercentage)
    percentages.append(newPercentage)

percentage_df = pd.DataFrame({
    "Fase": percentage_phases,
    "Porcentaje": percentage_values
})

print(df)
print(percentage_df)

# botUrl = 'https://adam-whatsapp-bot.herokuapp.com/messages/send-communes-status'
# requestBody = {'communes': communes, "phases": percentages}
# print(requestBody)

# sendCommunesStatusRequest = requests.post(botUrl, json=requestBody)

print("Script finished")