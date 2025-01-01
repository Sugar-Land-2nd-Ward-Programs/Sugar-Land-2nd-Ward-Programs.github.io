"""
Sunday Schedules for 2025

December 2024 by Pete Slater
"""
sunday = {
   "January 05" : ["Fast", "January 5th"],
    "January 12" : ["Normal", "January 12th"],
    "January 19" : ["Normal", "January 19th"],
    "January 26" : ["Normal", "January 26th"],
    "February 02" : ["Fast", "February 2nd"],
    "February 09" : ["Normal", "February 9th"],
    "February 16" : ["Normal", "February 16th"],
    "February 23" : ["Normal", "February 23rd"],
    "March 02" : ["Fast", "March 2nd"],
    "March 09" : ["Normal", "March 9th"],
    "March 16" : ["Normal", "March 16th"],
    "March 23" : ["Normal", "March 23rd"],
    "March 30" : ["Fast", "March 30th"],
    "April 06" : ["General", "April 6th"],
    "April 13" : ["Normal", "April 13th"],
    "April 20" : ["Easter", "April 20th"],
    "April 27" : ["Normal", "April 27th"],
    "May 04" : ["Fast", "May 4th"],
    "May 11" : ["Normal", "May 11th"],
    "May 18" : ["Stake", "May 18th"],
    "May 25" : ["Normal", "May 25th"],
    "June 01" : ["Fast", "June 1st"],
    "June 08" : ["Normal", "June 8th"],
    "June 15" : ["Normal", "June 15th"],
    "June 22" : ["Normal", "June 22nd"],
    "June 29" : ["Normal", "June 29th"],
    "July 06" : ["Fast", "July 6th"],
    "July 13" : ["Normal", "July 13th"],
    "July 20" : ["Normal", "July 20th"],
    "July 27" : ["Normal", "July 27th"],
    "August 03" : ["Fast", "August 3rd"],
    "August 10" : ["Normal", "August 10th"],
    "August 17" : ["Normal", "August 17th"],
    "August 24" : ["Normal", "August 24th"],
    "August 31" : ["Normal", "August 31st"],
    "September 07" : ["Fast", "September 7th"],
    "September 14" : ["Normal", "September 14th"],
    "September 21" : ["Normal", "September 21st"],
    "September 28" : ["Normal", "September 28th"],
    "October 05" : ["General", "October 5th"],
    "October 12" : ["Fast", "October 12th"],
    "October 19" : ["Normal", "October 19th"],
    "October 26" : ["Normal", "October 26th"],
    "November 02" : ["Fast", "November 2nd"],
    "November 09" : ["Normal", "November 9th"],
    "November 16" : ["Normal", "November 16th"],
    "November 23" : ["Stake", "November 23rd"],
    "November 30" : ["Normal", "November 30th"],
    "December 07" : ["Fast", "December 7th"],
    "December 14" : ["Normal", "December 14th"],
    "December 21" : ["Christmas", "December 21st"],
    "December 28" : ["Normal", "December 28th"],
    "ZZZ" : "End of List"
}

# Expand meeting type. Not done in base dict because of the origin of the table
meeting_type = {
    "Normal" : "Sacrament Meeting",
    "Fast" : "Fast and Testimony Meeting",
    "Ward" : "Ward Conference",
    "Stake" : "Stake Conference",
    "General" : "General Conference",
    "Easter" : "Easter Service",
    "Primary" : "Primary Program",
    "Christmas" : "Christmas Program",
}

def sunday_type(keydate):
    """
        Return type of meeting and pretty format for keydate
    """
    [sunday_type, format_date] = sunday[keydate]
    meeting = meeting_type[sunday_type]
    return meeting, format_date

