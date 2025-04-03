from pathlib import Path 
from datetime import datetime 

import requests 
from requests.exceptions import HTTPError
import click 
import pandas as pd 

@click.group()
def tcgcsv():
    pass 

@click.command()
def categories(): 
    """
    Collect and save data for categories/games.
    
    Categories are colloqiually games, but categories may contain 
    other things we're not necessarily interested in. 
    
    This will hit the TCGCSV resource and get available categories.
    
    Ideally, this should only run once a month, or something, new games don't come out often.
    """
    # Initialize where we're saving the data. 
    current_dir = Path(__file__).parent.absolute()
    data_dir = current_dir.parent / "data"
    
    # If the data directory doesn't exist, create it. 
    if not data_dir.exists():
        click.echo(f"Creating data directory at: {data_dir.absolute()}")
        data_dir.mkdir(exist_ok=True, parents=True)
        
    # Prepare the staging area for the new data.
    click.echo("Preparing staging area...")
    today_str = datetime.today().strftime("%Y-%m-%d")
    file_dir = data_dir / today_str / "categories"
    
    if not file_dir.exists():
        click.echo(f"Creating staging area: {file_dir.absolute()}")
        file_dir.mkdir(exist_ok=True, parents=True)
    
    # Collect categories and save them as CSV.
    click.echo("Collecting categories...")
    
    # Make the request
    click.echo("Requesting data from resource...")
    url = "https://tcgcsv.com/tcgplayer/categories"
    try:
        res = requests.get(url)
        res.raise_for_status()
    except HTTPError as e: 
        click.echo(f"HTTP error has occurred: {e}")
    except Exception as e:
        click.echo(f"Other exception has occurred: {e}")
    
    # Convert the response data to a DataFrame for easy CSV export.    
    categories = res.json().get("results")
    df = pd.DataFrame(categories)
    
    # Write out the data
    click.echo("Saving data...")
    output_filepath = file_dir / "categories.csv"
    df.to_csv(output_filepath, index=False)
    
    click.echo("Complete!")


tcgcsv.add_command(categories)


if __name__ == '__main__':
    tcgcsv()