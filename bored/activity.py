import requests


def random_activity():
    req = requests.get("https://www.boredapi.com/api/activity/", timeout=10)
    data = req.json()
    print(data["activity"])


def activity_by_type(activity_type: str):
    req = requests.get(
        f"https://www.boredapi.com/api/activity/?type={activity_type}", timeout=10
    )
    data = req.json()
    print(data["activity"])


def activity_by_participants(activity_participants: int):
    req = requests.get(
        f"https://www.boredapi.com/api/activity/?participants={activity_participants}",
        timeout=10,
    )
    data = req.json()
    print(data["activity"])


if __name__ == "__main__":
    random_activity()
    activity_by_type("cooking")
    activity_by_participants(4)
