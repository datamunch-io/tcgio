# TCG Stonks - Trading Card Price Tracking 

A daily price tracker with alerts for trading cards. Think of US Stock Exchange biggest winners and losers, but for trading cards.

## Setup 

`pip install -r requirements.txt`

## Journal

### Concept: 
1. Get prices of available SKUs 
2. Save prices into a data store
3. Compare today's prices to yesterday's prices 
4. Surface SKUs that have changed a significant percentage chance

After that... How do we deliver these price changes? Doesn't matter, the above is a good enough starting point to get coding. 

### To Do: 

1. Set up ingestion pipeline
    1. ~~Categories (games)~~ **Done** 
    2. ~~Groups (sets)~~ **Done** 
        1. Refactor groups to take category/game name instead of category id 
    3. ~~SKUs (cards)~~ **Done** 
    4. Create an ingestion script to scrape all cards and prices for all tcgs.
2. Set up a database (postgres)
    1. DDL for tables 
    2. Load jobs to get ingested data into the database.
    3. Stored procs to calculate a % change based on a date range
        1. Yesterday
        2. 7 days
        3. 30 days
    4. Create jobs to run stored procs daily
3. Research how to deliver these price changes
4. ~~Implement setuptools for click cli~~ **Done** 