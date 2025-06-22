import json
_config = {
    "url": "https://store.steampowered.com/specials",
    "meta": {
        "name": "Steem game scraper",
        "description": "scraping the most 12 games have a high descount.",
        "auther": "Ahmed Elaarag",
        "version": '0.1'
    },
    "container": [
        {
            "name": "store_sale_divs",
            "selector": 'div[class*="gASJ2lL_xmVNuZkWGvrWg"]',
            "match": "all",
            "type": "node"
        }]
    ,
    "item": [
        {
            "name": "title",
            "selector": 'div[class*="StoreSaleWidgetTitle"]',
            "match": "first",
            "type": "text"
        },
        {
            "name": "image_url",
            "selector": 'img[class="_2eQ4mkpf4IzUp1e9NnM2Wr"]',
            "match": "first",
            "type": "node"
        },
        {
        "name": "tags",
            "selector": 'div[class*="_2bkP-3b7dvr0a_qPdZEfHY"] a',
            "match": "all",
            "type": "text"
        },
        {
        "name": 'release_date',
            "selector": 'div[class*="_3a6HRK-P6LK0-pxRKXYgyP"] > div[class="_1qvTFgmehUzbdYM9cw0eS7"]',
            "match": "first",
            "type": "text"
        },
        {
        "name": "review_score",
            "selector": 'div[class*="_3ZWs0kB-1tuqQtie9KK-E7"] > div',
            "match": "first",
            "type": "text"
        },
        {
        "name": 'review_counts',
            "selector": 'div[class*="_3ZWs0kB-1tuqQtie9KK-E7"] div[class="_1wXL_MfRpdKQ3wZiNP5lrH"]',
            "match": "first",
            "type": "text"
        },
        {
        "name": 'original_price',
            "selector": 'div[class*="StoreSalePriceWidgetContainer"] div[class*="_3fFFsvII7Y2KXNLDk_krOW"]',
            "match": "first",
            "type": "text"
        },
        {
        "name": 'sale_price',
            "selector": 'div[class*="StoreSalePriceWidgetContainer"] div[class*="_3j4dI1yA7cRfCvK8h406OB"]',
            "match": "first",
            "type": "text"
        },
        {
        "name": 'currency',
            "selector": 'div[class*="StoreSalePriceWidgetContainer"] div[class*="_3j4dI1yA7cRfCvK8h406OB"]',
            "match": "first",
            "type": "text"
        }
        ]
}
def get_config(load_from_file=False):
    if load_from_file:
        with open('config.json', 'r') as f:
            return json.load(f)
    return _config

def generate_config():
    with open("config/config.json", 'w') as f:
        json.dump(_config, f, indent=4)


if __name__ == __name__:
    generate_config()