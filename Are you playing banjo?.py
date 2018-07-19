def areYouPlayingBanjo(name):
    if name[0] == "R" or name[0] == "r":
        name += " plays banjo"
    else:
        name += " does not play banjo"
    return name
