# type: ignore

"""Activities from the Activity Endpoint."""
from dataclasses import dataclass

@dataclass
class Activity:
    """Activity class"""

@dataclass
class DonationActivity(Activity):
    """A donation activity"""


@dataclass
class ParticipantBadgeActivity(Activity):
    """"Badge Activity"""


@dataclass
class TeamBadgeActivity(Activity):
    """Team Badge Activity"""

def create_activity(json_data: dict):
    """
    To deal with the activity endpoint, this will create activities.
    """