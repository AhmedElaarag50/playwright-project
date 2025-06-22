from playwright.sync_api import sync_playwright
from utiles.extract  import extract_html_from_url
from utiles.parse import parse_raw_attributes
from utiles.process import post_process_attrs, save_to_file
from config.tools import get_config
import time
from selectolax.parser import HTMLParser
#url = "https://store.steampowered.com/specials"
#element = 'div[class*="gASJ2lL_xmVNuZkWGvrWg"]'
game_data = []
if __name__ == "__main__":
    config = get_config()
    html = extract_html_from_url(config.get("url"), config.get("container")[0].get("selector"))
    nodes = parse_raw_attributes(html, config.get("container"))
    #tree = HTMLParser(html)
    #divs = tree.css(config.get("container").get("selector"))
    print(nodes)
    for node in nodes['store_sale_divs']:
            attrs = parse_raw_attributes(node, config.get("item"))
            attrs = post_process_attrs(attrs)
            #print(attrs)
            game_data.append(attrs)
    save_to_file(data=game_data)
        