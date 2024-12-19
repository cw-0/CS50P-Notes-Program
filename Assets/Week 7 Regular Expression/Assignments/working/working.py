import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):

    match = re.search(r"^(?P<before_hour>[0-9]|1[0-2]){1}(?P<before_minute>:[0-5][0-9])?\s(?P<before_am_or_pm>(AM to|PM to)){1}\s(?P<after_hour>[0-9]|1[0-2]){1}(?P<after_minute>:[0-5][0-9])?\s(?P<after_am_or_pm>(AM|PM)){1}$", s, flags=re.I)
    try:
        if match:
            before_hour = match.group("before_hour")
            after_hour = match.group("after_hour")
            before_am_or_pm = match.group("before_am_or_pm")
            after_am_or_pm = match.group("after_am_or_pm")


            if match.group("before_minute"):
                before_minute = match.group("before_minute")
            else:
                before_minute = ":00"
            if match.group("after_minute"):
                after_minute = match.group("after_minute")
            else:
                after_minute = ":00"


            if after_am_or_pm.lower() == "pm" and int(after_hour) != 12:
                converted_after_hour = int(after_hour) + 12
            else:
                converted_after_hour = after_hour


            if before_am_or_pm.lower() == "pm to" and int(before_hour) != 12:
                converted_before_hour = int(before_hour) + 12
            else:
                converted_before_hour = before_hour

            if int(converted_before_hour) <10:
                converted_before_hour = "0" + converted_before_hour

            if int(converted_after_hour) <10:
                converted_after_hour = "0" + converted_after_hour

            if int(converted_before_hour) == 24:
                converted_before_hour = "00"

            if int(converted_after_hour) == 24:
                converted_after_hour = "00"

            if int(before_hour) == 12 and before_am_or_pm.lower() == "am to":
                converted_before_hour = "00"

            if int(after_hour) == 12 and after_am_or_pm.lower() == "am":
                converted_after_hour = "00"
            if int(after_hour) == 12 and after_am_or_pm.lower() == "pm":
                converted_after_hour = "12"



            time = f"{converted_before_hour}{before_minute} to {converted_after_hour}{after_minute}"
            return time
        else:
            raise ValueError
    except ValueError:
        raise ValueError



if __name__ == "__main__":
    main()
