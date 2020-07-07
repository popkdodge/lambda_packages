import math
import re
import pandas


def get_match(string, pattern):
    # a service function to look for patterns in strings
    found = None
    if not string != string:
        try: 
            found = pattern.search(str(string))
        except Exception as e: 
            print(f"Unexpected error: {e} for {string}")
        if found != None:
            value = re.compile("\d{1,}").search(found[0])
            return int(value[0])
    return 0 


def convert_time(col):  
    # expects a dataframe column

    for index, row in col.iteritems():
        min_p = re.compile("\d{1,}\sminutes")
        sec_p = re.compile("\d{1,}\sseconds")    
        hr_p = re.compile("\d{1,}\shours")            
        mins = get_match(row, min_p)
        secs = get_match(row, sec_p)
        hrs = get_match(row, hr_p)
        time = mins * 60 + secs + hrs * 60 * 60
        col[index] = time