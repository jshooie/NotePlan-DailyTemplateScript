import datetime
import os

start_date_pending = True
end_date_pending = True
weekends_pending = True
file_path_pending = True
user_path = os.path.expanduser("~")
rel_path = "/Library/Mobile Documents/iCloud~co~noteplan~NotePlan/Documents/Calendar"
dst_path = user_path + rel_path

print("Daily Journal Template Creator for Noteplan")

# Get Start Date
while start_date_pending:
    print("\nStart Date (first day for file creation):")

    while True:
        start_yr_txt = input("  Year (2000-2100):\n  >>>")
        try:
            start_yr = int(start_yr_txt)
        except ValueError:
            print("\nValueError: Please enter a 4-digit integer between 2000 and 2100.\n")
            continue
        if 2000 <= start_yr <= 2100:
            break;
        else:
            print("\nValueError: Please enter a 4-digit integer between 2000 and 2100.\n")

    # Get Start Month
    while True:
        start_month_txt = input("\n  Month (1-12):\n  >>>")
        try:
            start_month = int(start_month_txt)
        except ValueError:
            print("\nValueError: Please enter a number between 1 and 12.\n")
            continue
        if 1 <= start_month <= 12:
            break;
        else:
            print("\nValueError: Please enter a number between 1 and 12.\n")

    # Get Start Month
    while True:
        start_day_txt = input("\n  Day (1-31):\n  >>>")
        try:
            start_day = int(start_day_txt)
        except ValueError:
            print("\nValueError: Please enter a number between 1 and 31.\n")
            continue
        if 1 <= start_day <= 31:
            break;
        else:
            print("\nValueError: Please enter a number between 1 and 31.\n")

    try:
        start_date = datetime.datetime(start_yr, start_month, start_day)
    except ValueError:
        print("\nValueError: Day inputed is out of range for the month. Please try again.")
        continue

    print("\nStart Date: " + start_date.strftime("%B %d, %Y"))
    start_date_correct = input("\nIs this correct? [Y/N]:\n>>>")
    if start_date_correct == "Y" or start_date_correct == "y":
        start_date_pending = False


# Get End Date
while end_date_pending:
    print("\nEnd Date (last day for file creation):")

    while True:
        end_yr_txt = input("  Year (2000-2100):\n  >>>")
        try:
            end_yr = int(end_yr_txt)
        except ValueError:
            print("\nValueError: Please enter a 4-digit integer between 2000 and 2100.\n")
            continue
        if 2000 <= end_yr <= 2100:
            break;
        else:
            print("\nValueError: Please enter a 4-digit integer between 2000 and 2100.\n")

    # Get end Month
    while True:
        end_month_txt = input("\n  Month (1-12):\n  >>>")
        try:
            end_month = int(end_month_txt)
        except ValueError:
            print("\nValueError: Please enter a number between 1 and 12.\n")
            continue
        if 1 <= end_month <= 12:
            break;
        else:
            print("\nValueError: Please enter a number between 1 and 12.\n")

    # Get end Month
    while True:
        end_day_txt = input("\n  Day (1-31):\n  >>>")
        try:
            end_day = int(end_day_txt)
        except ValueError:
            print("\nValueError: Please enter a number between 1 and 31.\n")
            continue
        if 1 <= end_day <= 31:
            break;
        else:
            print("\nValueError: Please enter a number between 1 and 31.\n")

    try:
        end_date = datetime.datetime(end_yr, end_month, end_day)
    except ValueError:
        print("\nValueError: Day inputed is out of range for the month. Please try again.")
        continue
    if end_date <= start_date:
        print("ValueError: End date must be after start date. Please try again.")
        continue

    print("\nEnd Date: " + end_date.strftime("%B %d, %Y"))
    end_date_correct = input("\nIs this correct? [Y/N]:\n>>>")
    if end_date_correct == "Y" or end_date_correct == "y":
        end_date = end_date + datetime.timedelta(days=1)
        end_date_pending = False

# Include weekends?
while weekends_pending:
    incl_weekends_txt = input("\nCreate templates for weekends [Y/N]:\n>>>")
    if incl_weekends_txt == "Y" or incl_weekends_txt == "y":
        incl_weekends = True
        weekends_pending = False
        print("\nTemplates will be created for weekends.")
    elif incl_weekends_txt == "N" or incl_weekends_txt == "n":
        incl_weekends = False
        weekends_pending = False
        print("\nTemplates will not be created for weekends.")
    else:
        print("Invalid input. Please try again.")

# Validate filepath
while file_path_pending:
    print("\nDefault filepath to store .txt files is: " + dst_path)
    chg_path = input("\nWould you like to change the destination? [Y/N]\n>>>")
    if chg_path == "N" or chg_path == "n":
        file_path_pending = False
    else:
        new_path = input("\nPlease enter the new path:\n>>>")
        if os.path.isdir(new_path):
            print("New path is: " + new_path)
            path_correct = input("\nIs this correct? [Y/N/Default]\n>>>")
            if path_correct == "Default" or path_correct == "default":
                print("\nDefault path will be used.")
                file_path_pending = False
            elif path_correct == "Y" or path_correct == "y":
                print("\nFile path updated.")
                dst_path = new_path
                file_path_pending = False
        else:
            print("Path name is not valid. Please try again.")#

# Create .txt files
# Define range of days
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

# Iterate through days
weekend = set([5, 6])
for date in daterange(start_date, end_date):
    if incl_weekends:
        filename = date.strftime("%Y%m%d") + ".txt"
        filename_path = dst_path + "/" + filename
        content = "# " + date.strftime("%B %-d, %Y") + "\n\n### To-Dos\n"

        try:
            f = open(filename_path, "x")
            f.write(content)
            f.close()
        except FileExistsError:
            print("File " + filename + " already exists and will not be overwritten.")

    elif not incl_weekends and date.weekday() not in weekend:
        filename = date.strftime("%Y%m%d") + ".txt"
        filename_path = dst_path + "/" + filename
        content = "# " + date.strftime("%B %-d, %Y") + "\n\n### To-Dos\n"

        try:
            f = open(filename_path, "x")
            f.write(content)
            f.close()
        except FileExistsError:
            print("File " + filename + " already exists and will not be overwritten.")
