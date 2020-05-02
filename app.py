
import arrow
import datetime
import dateutil
from datetime_play import *
from tasks import add_number,send_email

# shift alt up/down to duplicate code lines

def main():
    TARGET_TIMEZONE = "US/Eastern"

    # for debugging
    DT_FORMAT = "YYYY-MM-DD HH:mm:ss ZZ"

    YYYY_MM_DD_TODAY = arrow.utcnow().format("YYYY-MM-DD")  # YEAR, MONTH, DAY

    # Parse date string to datetime object
    YYYY_MM_DD_TODAY_TIMESTAMP = arrow.get(YYYY_MM_DD_TODAY)

    TODAYS_TRIGGER_TIME = YYYY_MM_DD_TODAY  # 2020-05-01

    TODAY_TARGET = (
        arrow.get(YYYY_MM_DD_TODAY_TIMESTAMP)
        .shift(hours=15, minutes=40)
        .replace(tzinfo=dateutil.tz.gettz(TARGET_TIMEZONE))
    )

    # logging
    print("\n")
    print(f"    Today's trigger >>> {TODAY_TARGET.format(DT_FORMAT)}")
    print("\n")

    return TODAY_TARGET




