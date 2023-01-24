def dostuff():
    global now, toppage
    # if 60 seconds have passed since the last update
    if time.time()*1000 > now + 1000:
        prevnow = now
        now = float('inf')
        c = requests.get(
            "https://api.hypixel.net/skyblock/auctions?page=0").json()
        if c['lastUpdated'] != prevnow:
            now = c['lastUpdated']
            toppage = c['totalPages']
            main()
        else:
            now = prevnow
    time.sleep(0.25)


while True:
    dostuff()
