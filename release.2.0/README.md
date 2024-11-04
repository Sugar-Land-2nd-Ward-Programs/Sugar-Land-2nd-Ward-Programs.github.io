# Files:
- main.py - Script loads YAML as a python object (list of dictionaries and lists). Script uses **jinja2** library to render the html template with the YAML data and outputs the result to an HTML file.
- template.html - jinja2 template for HTML rendering
- data.yaml - settings
- output.html - resulting file

# YAML structure
**Why YAML?** It is more user friendly format than json.  

- fast_meeting: false. Automatically changes title to the Fast and testimony meeting. Can be programmed to do something else also.

Structure example:
```yaml
unit: "Sugar Land 2nd Ward"
meeting_title: "Sacrament Meeting"
meeting_date: "July 17, 2022"
fast_meeting: false
meeting_cover_img: "https://assets.ldscdn.org/e4/40/e440b004051c60f0e7b85e8af9b5bfbca156cf2d/houston_texas_mormon_temple.jpeg"
officers:
  - "Presiding": "Bishop Joey Powell"
  - "Conducting:": "Bishop Joey Powell"
program:
  - type: "hymn"
    record:
      descr: "Opening hymn"
      number: 3

  - type: "hymn"
    record:
      descr: "Scarment Hymn"
      number: 5

  - type: "custom"
    record:
      title: "Bearing of Testimonies"
      description: ""

  - type: "speaker"
    name: "John Wick"

  - type: "music"
    record:
      title: "Come ye..."
      description: "Nan and Ann"

  - type: "speaker"
    name: "Reuben Sams"

  - type: "custom"
    record:
      title: "Something else"
      description: "by Mike"

  - type: "hymn"
    record:
      descr: "Closing Hymn"
      number: 7
      
announcements:
  - "The sister missionaries have a new phone number: 346-901-8717"
  - Volleyball Wednesdays - Come join us on Wednesdays at 9PM and have fun!!!

posters:
  - "https://sugar-land-2nd-ward-programs.github.io/Stake%20Monthly%20Flyer.jpg"
  - "https://sugar-land-2nd-Ward-Programs.github.io/Houston%20South%20Stake%20-%20Save%20the%20Date.jpg"

quote_of_the_month:
  quote: "The only limit to our realization of tomorrow is our doubts of today."
  author: "Franklin D. Roosevelt"

calendar:
  - title: "Upcoming temple days"
    description: "November 9, December 14, January 11, February 8, March 8, April 12"
  - title: "Peanut Butter Factory Shift"
    description: "3:15 AM, Saturday, October 26, Hafer Rd."

links:
  - title: "The Light the World Giving Machines are Coming"
    url: https://www.youtube.com/watch?v=0_Ntv6zQ70M&authuser=1
  - title: "Watch the Light the World Video"
    url: https://www.youtube.com/watch?v=0_Ntv6zQ70M&authuser=1


```
