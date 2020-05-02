import os
import arrow
import huey

# from app import main

# https://huey.readthedocs.io/en/latest/guide.html#scheduling-tasks
# https://github.com/coleifer/huey
# https://github.com/coleifer/peewee

"""
cron format
minute hour day-of-month month day-of-week


50 15 * * 0,1,2,3,4

"""


def get_target_datetime():
    """
    returns a date time
    """
    target_timezone = "Asia/Taipei"

    year = 2020
    month = 5
    day = 2
    hour = 12
    minute = 00
    sec = 0

    user_time_utc = arrow.Arrow(year, month, day, hour, minute, sec)
    # user_time_utc = arrow.utcnow()
    user_time_target_timezone = user_time_utc.to(target_timezone)

    return user_time_target_timezone


# periodic task >> https://huey.readthedocs.io/en/latest/api.html#Huey.periodic_task
@huey.periodic_task(validate_datetime=get_target_datetime, retries=5)
def custom_scheduled_task():
    print("I am working!!")


# @huey.task(priority=10)
# def send_email(to, subj, body):
#     return mailer.send(to, "", subj, body)


if __name__ == "__main__":
    # requested_time = get_target_datetime()
    # print(requested_time)

    BACKEND_FILENAME = "huey.db"

    HUEY_BACKEND = os.path.join(".", BACKEND_FILENAME)

    huey = huey.SqliteHuey(filename=HUEY_BACKEND)
