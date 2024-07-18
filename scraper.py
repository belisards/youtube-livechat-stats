import os, re
from livechat_scraper.scrapers import livechat_scraper
from livechat_scraper.scrapers import livechat_scraper
from livechat_scraper.constants import scraper_constants as sCons

url_id = "https://www.youtube.com/watch?v=Xp8pH3tCQ5E"

def parse_youtube_id(url_or_id):
    # Regular expression to extract the video ID from a YouTube URL
    # Example usage
    # print(parse_youtube_id('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))  # Output: dQw4w9WgXcQ
    # print(parse_youtube_id('dQw4w9WgXcQ'))  # Output: dQw4w9WgXcQ
    regex = (
        r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/|youtube\.com/v/|youtube\.com/shorts/|youtube\.com/playlist\?list=)([^&/%\?]{11})'
    )
    
    # Match the input string against the regex
    match = re.match(regex, url_or_id)
    
    if match:
        # If a match is found, return the video ID
        return match.group(1)
    elif len(url_or_id) == 11:
        # If the input string is 11 characters long, assume it is a video ID
        return url_or_id
    else:
        # Return None if no valid video ID is found
        return None

yt_id = parse_youtube_id(url_id)

TARGET_FOLDER = "output/"

if not os.path.exists(TARGET_FOLDER):
    os.makedirs(TARGET_FOLDER)


print(f"Getting: {url_id}")

scraper = livechat_scraper.LiveChatScraper(url_id)

scraper.scrape()

output_file = TARGET_FOLDER + yt_id

scraper.write_to_file(sCons.OUTPUT_JSON, output_file)

print(f"JSON file saved to: {output_file}")