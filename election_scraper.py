"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Karolína Dvořáková Machová
email: karolin.machova@gmail.com
"""
import csv
import sys
from bs4 import BeautifulSoup as bs
from requests import get
from urllib.request import urlretrieve, HTTPError

# Functions
## Functions for extraction data from url in general
def send_request_get (url: str) -> str:
    """
    Returns the server's response to a "get" request.
    """
    response = get(url)
    return response.text

def get_parsed_request(response: str) -> bs:
    """
    Gets a splitted response to a GET request.
    """
    parsed = bs(response, features="html.parser")
    return parsed

## Functions for municipality specific urls extraction
def choose_a_tags(parsed: bs) -> bs:
    """
    Selects all "a" tags from the source code of the page.
    """
    all_a = parsed.find_all("a")
    return all_a

def get_urls(all_a: bs) -> list:
    """
    Selects all municicpality-specific parts of urls.
    """
    urls = []
    for element in all_a[5:244:2]:
        urls.append(element.get("href").splitlines())
    return urls

def get_full_urls(core_url: str, urls: list) -> list:
    """
    Creates full urls list merging core and specific parts of municipality urls.
    """
    full_urls = []
    for part in urls:
        part = str(part)
        full_urls.append(f"{core_url}{(part[2:-2])}")
    return full_urls

## Functions for extraction of specific values from core (root) url
def choose_td_tags(parsed: bs) -> bs:
    """
    Selects all "td" tags (municipality names) from the source code of the page.
    """
    all_td = parsed.find_all("td")
    return all_td

def get_municipality_numbers(all_a: bs) -> list:
    """
    Gets all municicpality codes.
    """
    numbers = []
    for number in all_a[5:244:2]:
        number= str(number.get_text().splitlines())
        numbers.append(number[2:-2])
    return numbers

def get_municipality_names(all_td: list) -> list:
    """
    Gets all municicpality names.
    """
    names = []
    for name in all_td[1::3]:
        name= str(name.get_text().splitlines())
        names.append(name[2:-2])
    return names

## Function for header extraction
def get_party_names(parsed: bs) -> list:
    """
    Returns names of all "td" tags with class "overflow_name" (electoral party names)
    from the source code of the page.
    """
    all_td_names = parsed.find_all("td", {"class": "overflow_name"} )
    names = []
    for name in all_td_names:
        name= str(name.get_text().splitlines())
        names.append(name[2:-2])
    return names

## Functions for extraction of specific values from municipality specific urls

def get_party_votes (parsed: bs) -> list:
    """
    Returns all "td" tags with class "cislo" (votes of each electoral party)
    from the source code of the page.
    """
    all_td_votes = parsed.find_all("td", {"class": "cislo"} )
    votes = []
    for number in all_td_votes[10::3]:
        number = str(number.get_text().splitlines())
        number = number.replace('\\xa0', ' ')               # replacing strange decimal deliminators
        votes.append(number[2:-2])
    return votes

def choose_td_numbers(parsed: bs, sa: str) -> bs:
    """
    Selects all "td" tags with classes "cislo"
    and headers "sa" from the source code of the page.
    'sa2' - registered voters
    'sa3' - number of the submitted envelopes
    'sa6' - valid votes
    """
    all_td_numbers = parsed.find("td", {"headers": sa})
    return all_td_numbers

def get_number(all_td_numbers: bs) -> str:
    """
    Gets a number of all submitted envelopes, registered voters or turnout.
    """
    number = str(all_td_numbers.get_text())
    number = number.replace('\xa0', ' ')                # replacing strange decimal deliminators
    return number

def make_list_spec_urls(url_region: str) -> list:
    """
    Extracts a list of full municipality specific urls.
    """
    parsed1 = get_parsed_request(send_request_get(url_region))
    core_url = url_region[:35]              # 35 starting symbols identical for all municipality urls
    spec_urls = get_urls(choose_a_tags(parsed1))                # specific part of municipality url
    full_urls = get_full_urls(core_url, spec_urls)
    return full_urls

def make_header(full_urls: list) -> list:
    '''
    Extracts header according to the first municipality example.
    '''
    parsed2 = get_parsed_request(send_request_get(full_urls[0]))              # one url for example of party names
    header_start = ["code", "location", "registered", "envelopes", "valid"]
    header_end = get_party_names(parsed2)             # electoral party names
    header = header_start + header_end
    return header

def make_names_list (url_region) -> list:
    '''
    Makes a list of all municipality names in a chosen region (root url).
    '''
    parsed1 = get_parsed_request(send_request_get(url_region))
    municipality_names = get_municipality_names(choose_td_tags(parsed1))
    return municipality_names

def make_codes_list (url_region: str) -> list:
    '''
    Makes a list of all municipality codes in a chosen region (root url).
    '''
    parsed1 = get_parsed_request(send_request_get(url_region))
    municipality_codes  = get_municipality_numbers(choose_a_tags(parsed1))
    return municipality_codes

# Main program    
if __name__ == "__main__":

    ## Arguments count validation
    try:
        file_name = sys.argv[2]
        url_region = sys.argv[1]    

    except IndexError:
        print('''Two arguments must be given. The first is an url address of the region
(territorial unit) and the second is a name of the new file.csv.''')
        exit(1)

    ## Arguments validation
    if url_region == "" or file_name == "":
        print('''Two arguments must be given. The first is an url address of the region
 (territorial unit) and the second is a name of the new file.csv.''')
        exit(2)
    elif not url_region.startswith("https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj="):
        print("Url address must start with 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj='.")
        exit(3)
    elif not file_name.endswith(".csv"):
        print("The url must end with '.csv'.")
        exit(4)
    elif len(url_region) < 71:
        print("Url address length must be 71 symbols at least.")
        exit(5)
    else:

        ## Url response validation
        try:
            urlretrieve(url_region)
        except HTTPError as err:
            print("Web page response incorrect, error code:", err.code)
        else:
            parsed = str(get_parsed_request(send_request_get(url_region)))
            if "Page not found" in parsed:                # Url response "Page not found!"
                print("Web page not found")
            else:

                ## Final .csv file write
                print("DOWNLOADING DATA FROM SELECTED URL:", url_region)
                full_urls = make_list_spec_urls(url_region)
                municipality_codes = make_codes_list(url_region)
                municipality_names = make_names_list(url_region)

                with open(file_name, mode = "w", newline='', encoding = "utf-8") as new_csv:
                    writer = csv.writer(new_csv,  dialect = "excel")
                    writer.writerow(make_header(make_list_spec_urls(url_region)))
                    print("SAVING TO FILE:", file_name)
                    for code, name, url in zip(municipality_codes, municipality_names, full_urls):
                        parsed = get_parsed_request(send_request_get(url))
                        number_registred = get_number(choose_td_numbers(parsed, "sa2"))
                        number_envelopes = get_number(choose_td_numbers(parsed, "sa3"))
                        number_valid_votes = get_number(choose_td_numbers(parsed, "sa6"))
                        votes_per_party = get_party_votes(parsed)
                        row_start = [code, name, number_registred, number_envelopes, number_valid_votes]
                        row = row_start + votes_per_party
                        writer.writerow(row)
                    print("EXITING election_scraper")
