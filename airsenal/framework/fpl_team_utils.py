"""
Functions to get data on specified FPL teams and leagues
"""

from .utils import fetcher


def get_overall_points(gameweek=None):
    """
    Get our total points
    """
    data = fetcher.get_fpl_team_data()
    if not gameweek:
        return data["entry"]["summary_overall_points"]
    elif isinstance(gameweek, int) and gameweek <= len(data["history"]):
        return data["history"][gameweek - 1]["points"]
    else:
        print("Unknown gameweek")
        return 0


def get_overall_ranking(gameweek=None):
    """
    Get our overall ranking
    """
    data = fetcher.get_fpl_team_data()
    if not gameweek:
        return data["entry"]["summary_overall_rank"]
    elif isinstance(gameweek, int) and gameweek <= len(data["history"]):
        return data["history"][gameweek - 1]["rank"]
    else:
        print("Unknown gameweek")
        return 0


def get_league_standings():
    """
    Get stuff about our mini-league
    """
    data = fetcher.get_fpl_league_data()
    team_name = data["league"]["name"]
    standings = []
    for s in data["standings"]["results"]:
        standings.append(
            {"name": s["entry_name"], "manager": s["player_name"], "points": s["total"]}
        )
    return team_name, standings
