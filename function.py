
def inputt():
    number_day = int(input())
    number_ot = int(input())
    late_day = int(input())
    return number_day,number_ot,late_day

def validate_number(number_day,number_ot,late_day) :
    if not isinstance(number_day, int) or number_day < 0 or number_day > 30:
        return False, "number_day must be integer and between 0-30 and not equal 0"
    # Validate that number_ot is an integer no more than number_day*3
    if not isinstance(number_ot, int) or number_ot < 0 or number_ot > number_day*3:
        return False, "number_ot must be integer and no more than number day*3"
    # Validate that late_day is an integer no more than number_day
    if not isinstance(late_day, int) or late_day < 0 or late_day > number_day:
        return False, "late_day must be integer and no more than number day"
    return True

def display_compensation(number_day,number_ot,late_day) :
    if validate_number(number_day,number_ot,late_day) == True :
        return number_day * 340 + number_ot * 60 + ((number_day-late_day)*1000)
    else :
        return validate_number(number_day,number_ot,late_day)