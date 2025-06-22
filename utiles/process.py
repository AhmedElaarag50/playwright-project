import pandas as pd
from selectolax.parser import Node
from datetime import datetime
import re

def get_number(input_str:str, pattern:str, do_what:str="findall"):
    if do_what == "match":
        number = re.match(pattern, input_str).group()
        return float(re.sub(r',', '.', number))
    elif do_what == "findall":
        price = re.findall(pattern, input_str)[0]
        return price
    else:
        raise ValueError("The function expects eithor match function or findall function.")


def reformat_date(date:str, input_format:str='%b %d, %Y', out_format:str='%Y-%m-%d'):
    dt_obj = datetime.strptime(date, input_format)
    return datetime.strftime(dt_obj, out_format)

def get_attribute(node: Node, attr:str):
    if node is None or not issubclass(Node, type(node)):
        raise ValueError("get_attribute function expects a selectolax Node should be provided.")
    return node.attributes.get(attr)

def post_process_attrs(atters: dict):
    transform = {}
    transform['image_url'] = lambda n: get_attribute(n, "src")
    transform['tags'] = lambda input_list: input_list[:5]
    transform['release_date'] = lambda date: reformat_date(date)
    transform['review_counts'] = lambda num: get_number(input_str=num, pattern="([0-9]+[,]*)+", do_what="match")
    transform['original_price'] = lambda price: float(get_number(price, pattern="([0-9]+[.]*)+", do_what="findall"))
    transform['sale_price'] = lambda price: float(get_number(price, pattern="([0-9]+[.]*)+", do_what="findall"))
    
    transform['currency'] = lambda price: get_number(price, pattern="\D", do_what="findall")
    for k, v in transform.items():
        if k in atters:
            atters[k] = v(atters[k])
    atters['discount_pct'] = round((atters['original_price'] - atters['sale_price']) / atters['original_price'] * 100, 3)
    return atters
    

def save_to_file(file_name:str=f"{datetime.now().strftime("%Y-%m-%d")}_extract.csv", data:list[dict]=None):
    if data is None:
        raise ValueError("The function expects python list of dictionaries.")
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
    print("game data is saved")