import arrow

# list of timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
utc = arrow.utcnow()
est = utc.to("US/Eastern")  # Eastern Standard Time
mst = utc.to("US/Mountain")  # Mountain Standard Time
pst = utc.to("US/Pacific")  # Pacific Standard Time
tst = utc.to("Asia/Taipei")  # Taipei Standard Time
pst = utc.to("Asia/Hong_Kong")  # Hong Kong


print(f"US/Eastern {est.format(DT_FORMAT)}")
print(f"US/Mountain {mst.format(DT_FORMAT)}")
print(f"US/Pacific {pst.format(DT_FORMAT)}")
print(f"Asia/Taipei {tst.format(DT_FORMAT)}")
print(f"Asia/Hong_Kong {pst.format(DT_FORMAT)}")
