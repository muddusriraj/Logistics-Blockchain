# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 12:59:24 2023

@author: Sriraj
"""
import requests

ids=[1, 2, 3, 4, 5, 6]
for id in ids:
    url = f"https://api.verbwire.com/v1/nft/data/nftDetails?contractAddress=0xb7C0C23849Cea222648d37153f3A5F7ea9AA3176&tokenId={id}&chain=goerli"
    
    headers = {
        "accept": "application/json",
        "X-API-Key": "sk_live_a59f451a-cd88-481f-8940-66ea032854ec"
    }
    
    response = requests.get(url, headers=headers)
    
    
    link = "https"+ response.text.split("https")[-1].replace('"',"").replace("}", "")
    print(link)
    import urllib.request
    o = urllib.request.urlopen(link)
    b = o.read()
    s = b.decode("utf-8")
    finalist = s[1:].split(',"image"')[0].split(",")
    print("\nNext NFT in List:\n")
    for item in finalist:
        print(item)

