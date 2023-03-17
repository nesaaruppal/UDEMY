# NESTING
{
    Key: [LIST],
    Key2: {DICTIONARY}
}

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}


# NESTING LIST IN DICT
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# ALSO
["A", "B"["C", "D"]]

# DICTIONARY IN DICTIONARY
travel_log_2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


# LISTS WITH DICTIONARIES
[{
    Key: [LIST],
    Key2: {DICT},
},
    {
    Key: Value,
    Key2: Value,
}]


travel_log_3 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]
