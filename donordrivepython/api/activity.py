from datetime import datetime

# type: ignore

"""Activities from the Activity Endpoint."""


class Activity:
    """Activity class"""

    def __init__(self, created_date, image_url, type):
        self.created_date: str = created_date
        self.image_url: str = image_url
        self.type: str = type

    def better_date(self):
        """Convert the date to a prettier format."""
        my_time_zone = datetime.now().astimezone().tzinfo
        date_and_time_of_activity_utc = datetime.strptime(self.created_date, '%Y-%m-%dT%H:%M:%S.%f%z')
        date_and_time_of_activity_my_time_zone = date_and_time_of_activity_utc.astimezone(my_time_zone)
        pretty_date_time = date_and_time_of_activity_my_time_zone.strftime('%x - %X')
        return pretty_date_time
    def __str__(self):
        return f"{self.better_date()} - An activity of type {self.type} created "


class DonationActivity(Activity):
    """A donation activity"""

    def __init__(self, amount, created_date, image_url, is_incentive, message, title, type):
        super().__init__(created_date, image_url, type)
        self.amount: float = amount
        self.is_incentive: Bool = is_incentive
        self.message: str = message
        self.title: str = title

    def __str__(self):
        if self.is_incentive:
            return f"{self.better_date()} - Incentive reached: {self.message} with {self.title} donation of ${self.amount}."
        return f"{self.better_date()}- {self.title} donation in the amount of ${self.amount}."


class BadgeActivity(Activity):
    """"Badge Activity"""

    def __init__(self, created_date, image_url, message, title, type):
        super().__init__(created_date, image_url, type)
        self.message: str = message
        self.title: str = title

    def __str__(self):
        return f"{self.better_date()}- {self.message}: '{self.title}' badge earned!!"


def create_activity(json_data: dict):
    """
    To deal with the activity endpoint, this will create activities.
    """
    amount = json_data.get('amount')
    created_date = json_data.get('createdDateUTC')
    image_url = json_data.get('imageURL')
    is_incentive = json_data.get('isIncentive')
    message = json_data.get('message')
    title = json_data.get('title')
    type = json_data.get("type")
    if type == "donation":
        return DonationActivity(amount, created_date, image_url, is_incentive, message, title, type)
    elif type == "participantBadge" or "teamBadge":
        return BadgeActivity(created_date, image_url, message , title, type,)
    else:
        return Activity(created_date, image_url, type)
