"""A Teamgorup is a group of teams, naturally."""
from dataclasses import dataclass

@dataclass
class TeamGroup:
    fundraising_goal: float
    group_code: str
    name: str
    number_of_donations: int
    number_of_participants: int
    number_of_teams: int
    sum_of_donations: float


def create_team_group(json_data) -> TeamGroup:
    fundraising_goal: float = json_data.get('fundraisingGoal')
    group_code: str = json_data.get('groupCode')
    name: str = json_data.get('name')
    number_of_donations: int = json_data.get('numDonations')
    number_of_participants: int = json_data.get('numParticipants')
    number_of_teams: int = json_data.get('numTeams')
    sum_of_donations: float = json_data.get('sumDonations')
    return TeamGroup(fundraising_goal, group_code, name, number_of_donations, number_of_participants, number_of_teams,
                     sum_of_donations)
