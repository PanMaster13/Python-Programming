import datetime

now = datetime.datetime.now()

app_name = input("Enter the applicant's name:")

int_name = input("Enter the interviewer's name:")

print(int_name, "will interview", app_name, "at 9.30 am on", now.year,
      "-", now.month + 1, "-", now.day)
