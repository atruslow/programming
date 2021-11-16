TICKER_LIST = [
    (15, TWTR, 2013, 2021),
    (100, TWTR, 2004, 2011),
    (25, AAPL, 1980, 2021),
    ..
]


find_id(ticker: str, time: int) -> sid

find_id("AAPL", 1990) -> 25
find_id("TWTR", 2014) -> 15

TICKER_LIST_MAP = {i[1]: i i
for i in TICKER_LIST}


def find_id(ticker: str, time: int) -> Optional[int]:
    matching_tickers = TICKER_LIST_MAP[ticker]


for matching_ticker in matching_tickers:
    sid, tkr, start_year, end_year = matching_ticker

if start_year <= time <= end_year:
    return sid

    return None

--



