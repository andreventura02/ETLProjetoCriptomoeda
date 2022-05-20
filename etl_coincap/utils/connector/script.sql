CREATE TABLE assets(
    rank TEXT,
    id TEXT,
    name TEXT,
    symbol TEXT,
    explorer TEXT,
    price_usd NUMERIC,
    market_cap_usd NUMERIC,
    volume_usd_24hr NUMERIC,
    vwap_24hr NUMERIC,
    change_percent_24hr NUMERIC, 
    supply NUMERIC,
    max_supply NUMERIC,
    date_timestamp BIGINT
);