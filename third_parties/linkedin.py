import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """ scrape information from LinkedIn profiles
    Manually scrape information from LinkedIn profile"""
    
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/jferna57/10bc76afe0c6ae82bc0c85ff14cd4c43/raw/a57282b6d3fa916bf9d975caa54b8dc977e8b0ca/jferna57-linkedin.json"
        response = requests.get (
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10
        )
    
    data = response.json().get("person")
    
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["certifications"]
    }
    return data

if __name__ == "__main__":
    print (
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/jferna57",
            mock=True
        )
    )