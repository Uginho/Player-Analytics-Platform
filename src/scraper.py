import requests
from bs4 import BeautifulSoup, SoupStrainer
import time

class SoccerScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Window NT 10.0; x64) AppleWebKit/537.36'
        }
    
    def get_page(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def test_scraper(self):
        print("Testing scraper...")
    
    # Let's start with a simple, reliable site
        test_url = "https://httpbin.org/html"
        html_content = self.get_page(test_url)
    
        if html_content:
            print("✅ Successfully fetched webpage!")
            print(f"Content length: {len(html_content)} characters")
            print("First 200 characters:")
            print(html_content[:200])
        else:
            print("❌ Failed to fetch webpage")


    def scrape_player_stats(self):
        url = "https://www.myfootballfacts.com/premier-league/all-time-premier-league/goals-assists/premier-league-players-goals-assists-2024-25/"

        print("Fetching Stats...")
        html_content = self.get_page(url)

        if not html_content:
            print("Failed to fetch website")
            return []

        # Parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Debug to check if we can find any tables
        tables = soup.find_all('table')
        print(f"Found {len(tables)} tables on the page")

        # Find table w player stats
        table = soup.find('table')
        if not table:
            print("Could not find stats table")
            return []

        print("Found table! Getting rows...")

        rows = table.find_all('tr')[1:] # Skips first header row
        print(f"Found {len(rows)} data rows")
        
        players = []

        # get all table rows
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 5: # Make sure row has enough columns
                try:
                    goals_text = cells[3].text.strip()
                    assists_text = cells[4].text.strip()

                    if not goals_text or not assists_text:
                        continue

                    player_data = {
                        'name' : cells[0].text.strip(),
                        'club' : cells[1].text.strip(),
                        'nationality' : cells[2].text.strip(),
                        'goals' : int(goals_text),
                        'assists' : int(assists_text)
                    }
                    players.append(player_data)

                except ValueError as e:

                    print(f"Successfully scraped {len(players)} players!")
                    continue