"""
Sunday Schedules for 2024

January 2024 by Pete Slater
"""
sunday = {
    "January 07" :  ["Fast","January 7th"],
    "January 14" :  ["Normal","January 14th"],
    "January 21" :  ["Normal","January 21st"],
    "January 28" :  ["Normal","January 28th"],
    "February 04" :  ["Fast","February 4th"],
    "February 11" :  ["Ward","February 11th"],
    "February 18" :  ["Normal","February 18th"],
    "February 25" :  ["Normal","February 25th"],
    "March 03" :  ["Fast","March 3rd"],
    "March 10" :  ["Normal","March 10th"],
    "March 17" :  ["Normal","March 17th"],
    "March 24" :  ["Normal","March 24th"],
    "March 31" :  ["Easter","March 31st"],
    "April 07" :  ["General","April 7th"],
    "April 14" :  ["Fast","April 14th"],
    "April 21" :  ["Normal","April 21st"],
    "April 28" :  ["Normal","April 28th"],
    "May 05" :  ["Fast","May 5th"],
    "May 12" :  ["Normal","May 12th"],
    "May 19" :  ["Stake","May 19th"],
    "May 26" :  ["Normal","May 26th"],
    "June 02" :  ["Fast","June 2nd"],
    "June 09" :  ["Normal","June 9th"],
    "June 16" :  ["Normal","June 16th"],
    "June 23" :  ["Normal","June 23rd"],
    "June 30" :  ["Normal","June 30th"],
    "July 07" :  ["Fast","July 7th"],
    "July 14" :  ["Normal","July 14th"],
    "July 21" :  ["Normal","July 21st"],
    "July 28" :  ["Normal","July 28th"],
    "August 04" :  ["Fast","August 4th"],
    "August 11" :  ["Normal","August 11th"],
    "August 18" :  ["Normal","August 18th"],
    "August 25" :  ["Normal","August 25th"],
    "September 01" :  ["Fast","September 1st"],
    "September 08" :  ["Normal","September 8th"],
    "September 15" :  ["Normal","September 15th"],
    "September 22" :  ["Normal","September 22nd"],
    "September 29" :  ["Normal","September 29th"],
    "October 06" :  ["General","October 5th and 6th"],
    "October 13" :  ["Fast","October 13th"],
    "October 20" :  ["Primary","October 20th"],
    "October 27" :  ["Normal","October 27th"],
    "November 03" :  ["Fast","November 3rd"],
    "November 10" :  ["Normal","November 10th"],
    "November 17" :  ["Normal","November 17th"],
    "November 24" :  ["Stake","November 24th"],
    "December 01" :  ["Fast","December 1st"],
    "December 08" :  ["Normal","December 8th"],
    "December 15" :  ["Normal","December 15th"],
    "December 22" :  ["Normal","December 22nd"],
    "December 29" :  ["Normal","December 29th"],
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
}

def sunday_type(keydate):
    """
        Return type of meeting and pretty format for keydate
    """
    [sunday_type, format_date] = sunday[keydate]
    meeting = meeting_type[sunday_type]
    return meeting, format_date

