async def get_data_asynchronous():
    # puts all the page strings
    pages = [str(x) for x in range(toppage)]
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            START_TIME = default_timer()
            tasks = [
                loop.run_in_executor(
                    executor,
                    fetch,
                    # Allows us to pass in multiple arguments to `fetch`
                    *(session, page)
                )
                # runs for every page
                # for every page made runs through all kinds of pages that are available

                for page in pages if int(page) < toppage
            ]
            for response in await asyncio.gather(*tasks):
                pass
