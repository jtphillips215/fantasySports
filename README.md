# Fantasy Sports Automation Tool
This repository contains program created to automate our family fantasy sports league. Project is currently a work in progress.

## The goals for this project are as follows:
1. Scrape common stats sites for relevant information
    - Most likely using reference site
2. Use that information to automate setting salary prices for fantasy league
    - Data must be imported into fantasy site as a CSV
    - CSV import has required formatting for sheet

## Stretch goals:
1. Use that data to create sheets to share
    - Google sheets will probably be the easiest as it could be shared with a link
2. Visualize the data in some meaningful way to share
    - Alternatively, charts and images are easy to understand so this may be better solution long term

## I'm currently working on:
1. Creating the Web Scraper
    - Using Beautiful Soup, Pandas, and Requests
    - Need to initially get historical data but only add new data as events are completed
2. Creating data frames that can be used to work with that data or send to csv, sheets, or database
    - Probably also using Pandas to_csv feature, but more work needs to be done cleaning up and formatting data
