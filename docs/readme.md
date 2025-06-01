# Documentation
## WHAT IS THIS?
This is a dynamically updating weekly church program and announcements web page.

## FILES
- **main.py** - main python script that renders HTML pages
- **settings.yaml** - main settings file where most of the page layout is defined
- utils.py - Some additional functions for working with dates
- requirements.txt - Used in the actions to download and install necessary main.py python modules  
### Jinja2 HTML templates
- **template_index.html** - Index page
- template_artlinks.html - Template to show all defined cover arts and their keyword
### Directories
- css, js, assets, img - Supporting files for page styling
- posters - Posters to show on the Index.html page
- lookup - JSON files with various lookup values, such as hymns, art links, temple closure days, cleaning roster

## SETTINGS
Settings file defines layout of the program. Most sections can be commented out and will dissapear from the final HTML page accordingly.  
Special conditions:
- Hymns:
  - All sunday types, except general conference and stake conference, get **opening, sacrament, and closing** hymns automatically added.
  - Intermediate hymns and musical numbers can be added/commented out as needed for each sunday type.
- Sunday types supported:
  - sacrament
  - testimony
  - primary
  - easter
  - ward
  - christmas
  - stake
  - generalconference
- Fast and testimony meeting has a different layout. It will not have intermediate hymns or speakers
- General conference has a different layout. It will not show presiding officers, even if they are defined.
- Stake conference has a different layout.
- There is a placeholder for a christmas sunday, but it has not been used yet. Easter sunday can be copied over to the christmas section as a starter.
- Announcements and posters are defined in settings as a simple list
- Temple day automatically calculates based on lookup/temple_day.json. It considers temple closures or limited availability days
- Cleaning assignments are auto calculated They will only show up if there are actual assiginments coming in the next 2 weeks.


## SETTINGS.YAML reference example
```yaml
unit: "Sugar Land 2nd Ward"
meeting_cover_img: Nativity1 # Get alias from lookups/artlinks.json or from the arlinks web page
#meeting_type: "sacrament" # You can force the page to take a specific layout independently from the Sunday type here. Acceptable values: sacrament, testimony, primary, easter, ward, christmas, stake, generalconference
officers:
  - "Presiding": "Bishop Joey Powell"
  #- "Presiding": "Brother Brent Leavitt"
  - "Conducting": "Brother Jared Draney"
hymns:
  opening:
      number: 3
  sacrament:
      number: 5
  intermediate:
      number: 15
  closing:
      number: 7
meeting_sacrament:
  title: "Sacrament Meeting"
  program:
      - type: "speaker"
        name: "John Wick"

      - type: "speaker"
        name: "John Wick2"

      - type: intermediate_hymn
    
      #- type: "music"
      #  title: "Come ye... " #Music number
      #  description: "Nan and Ann" #Musicians
    
      - type: "speaker"
        name: "Reuben Sams"
    
      - type: custom
        title: "Something else"
        description: "by Mike J"
        
meeting_testimony:
  title: "Fast and Testimony Meeting"
  program:
      - type: custom
        title: "Bearing of Testimonies"
        description: ""


meeting_ward:
  title: "Ward Conference"
  program:

. . .

meeting_easter:
  title: "Easter Service"
  program:

. . .

meeting_primary:
  title: "Primary Program"
  program:
      - type: custom
        title: "Primary Program"
        description: |
          Words and Music Testifying of the Book of Mormon, Another Testament of Jesus Christ
          <br>Directed by Dawnette Moore, Accompanied by Dana Blackburn
          <br>Primary Choir with
          <br>Porter Wrightman, Maggie Moore, Ryan Boyer, Livia Moore, Evangelina Garcia, Theodore Rellaford, Boston Robinson, Piper Wrightman, Bella Moore, Sebastian Garcia, Gresham Robinson, Eliza Moore, Leonor Chen, Ioanna Ozomah, Dylan Moore, Henrie Rellaford

      - type: custom
        title: "Concluding remarks"
        description: "Bishop Joey Powell"

meeting_stake:
  title: "Stake Conference: Houston Texas South Stake"
  program:
      - type: custom
        title: "Leadership Session, Saturday 4:00-5:45 pm"
        description: |
          All members of Stake and Ward Councils and their presidencies, secretaries, and clerks are invited to attend.
          <br>This includes: Bishoprics; Elders quorum presidencies; Aaronic Priesthood quorum and Young Women class advisers; Relief Society, Young Women, Primary and Sunday School presidencies, and secretaries.
          <br>In-person at Lexington

      - type: custom
        title: "Adult Session, Saturday 7:00-8:45 pm"
        description: "All adults. <br>In-person at Lexington"

      - type: custom
        title: "Leadership Session, Sunday 10:00 am - 12:00 pm"
        description: "In-person at Lexington. <br>Via Zoom at Sienna and Rosenberg buildings"

meeting_generalconference:
  title: "General Conference"
  program:
      - type: custom
        title: "Join General Conference"
        description:  |
         Saturday Morning Session - 11:00 am CDT
         <br>Saturday Afternoon Session - 3:00 pm CDT
         <br>Saturday Evening Session - 7:00 pm CDT
         <br>Sunday Morning Session - 11:00 am CDT
         <br>Sunday Afternoon Session - 3:00 pm CDT

      - type: url
        title: "Watch and listen online"
        url: https://www.churchofjesuschrist.org/feature/general-conference?lang=eng

announcements:
  - Volleyball Wednesdays - Come join us on Wednesdays at 9PM and have fun!!!
  - Send announcements to bvl2clerk@gmail.com

posters: # Upload picuters to the GitHub img/ folder. Avoid spaces in the filenames.
  - "./posters/Bonner-family-concert.png"
  - "./posters/Houston%20South%20Stake%20-%20Save%20the%20Date.jpg"

calendar:
  temple_day: # Auto-calculated. Remove or comment this line to hide the next Ward temple day
  cleaning: # Auto-calculated. Remove or comment this line to hide the building cleaning schedule
  custom:
    - title: "Peanut Butter Factory Shift"
      description: "3:15 AM, Saturday, October 26, Hafer Rd."
    - title: "Something else"
      description: "12:00 PM, Church bld"

links:
  - title: "Sign up for the Christmas Party on December 7"
    url: https://www.signupgenius.com/go/10C0448A9A82EAB9-53466299-christmas
  - title: "The Light the World Giving Machines are Coming"
    url: https://www.youtube.com/watch?v=0_Ntv6zQ70M&authuser=1

quote_of_the_month:
  quote: "The only limit to our realization of tomorrow is our doubts of today."
  author: "Franklin D. Roosevelt"
```

## Why YAML?
  - Flexible in representing complex data types such as multi-line strings
  - More human-readable
  - Supports comments
  - Less verbose than JSON
  - Easier for non-technical users
  - Generally preferred for settings files

Example of python structures in YAML:
List `[a,b,c]`
```yaml
- a
- b
- c
```
Dictionary `{a: 1, b: 2}`
```yaml
a: 1
b: 2
```
List of dictionaries `[{a: 1, b: 2}, {a: 4, b: 5}]`
```yaml
- a: 1
  b: 2
- a: 4
  b: 5
```
  
Example of a multi-line string in YAML
```yaml
description: |
  This is a description
  that spans multiple
  lines in the YAML file.
```