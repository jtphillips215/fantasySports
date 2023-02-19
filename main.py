import scraper

# base URL as site uses RESTful scheme
BASE_URL = 'https://www.racing-reference.info/loopdata/'

# setting years as range for next gen car, setting races as a range of race numbers from 1 to 36
years = range(2022, 2024)
races = range(1, 37)

# iterating over each race during each year
for year in years:
    for race in races:
        if race < 10:
            url = BASE_URL + f'{year}-0{race}/W/'
        else:
            url = BASE_URL + f'{year}-{race}/W/'

        # calling scraper to get data
        data_frame = scraper.scrape(url)

        print(data_frame)
