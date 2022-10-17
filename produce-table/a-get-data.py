import requests, json, pandas as pd


def get_upw(doi):   

    out = ""
    req = requests.get(f"https://api.unpaywall.org/v2/{doi}?email=m@larri.eu")
    res = req.json()
    if res.get("is_oa"):
        out = "coucou"
    return res.get("is_oa")

d = get_upw("10.1017/S135577181900030X")
print(d)