def assets_sql() -> str:
    return """
    INSERT INTO assets(
        rank,
        id,
        name,
        symbol,
        explorer,
        price_usd,
        market_cap_usd,
        volume_usd_24hr,
        vwap_24hr,
        change_percent_24hr,
        supply,
        max_supply,
        date_timestamp
    ) 
    VALUES (
        %(rank)s,
        %(id)s,
        %(name)s,
        %(symbol)s,
        %(explorer)s,
        %(priceUsd)s,
        %(marketCapUsd)s,
        %(volumeUsd24Hr)s,
        %(vwap24Hr)s,
        %(changePercent24Hr)s,
        %(supply)s,
        %(maxSupply)s,
        %(timestamp)s   
    )       
    """