# Challenge URL: https://edabit.com/challenge/xbjDMxzpFcsAWKp97
# Note: Tested on edabit


def can_see_stage(seats):
    try:
        seats_in_one_row = len(seats[0])
        for seat_num in range(seats_in_one_row):
            if not all([seats[row_num][seat_num] < seats[row_num + 1][seat_num]
                       for row_num in range(len(seats) - 1)]):
                return False
        return True
    except (IndexError, KeyError):
        raise TypeError("Please provide iterable of iterables as a parameter.")

