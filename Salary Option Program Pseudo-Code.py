# Salary Option Program by Samuel Denning

# STRUCTURED ENGLISH DESCRIPTION ---
"""
    You are offered two different salary options. 
    One (Option1) says you will be paid $100 per day for (10) days of work
    The other (Option2) says you will be paid double the previous days amount.
    In other words, day one pay is $1, day two is $2, day three is $4, etc.
    Each amount doubling from the last for a total of (10) days of work.
    You want to know which of the two options will provide the most money in 10 days.
"""

# PSUEDOCODE DESCRIPTION ---
"""
    BEGIN
        numeric optionSum1, optionSum2, daysWorked
        assign daysWorked = 10
        compute optionSum1 = 100 * daysWorked
        start loop for x in range(daysWorked + 1)
            optionSum2 += x + x
        end loop 
        if (optionSum1 > optionSum2):
            print("Option 1 is better")
        elif (optionSum1 < optionSum2):
            print("Option 2 is better")
        elif (optionSum1 == optionSum2):
            print("Option 1 and Option 2 pays the same")
    END
"""