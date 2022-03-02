# OSINTAutomation

Automate OSINT using this simple script. Starting with person based OSINT and will be developed to include more OSINT procedures.

The program accepts a username as input and checks if the username exists on different sites using Sherlock. Once that's done, it will scrape data from Instagram
and Twitter and store it in the folder as well. If a phone number is entered, it will initiate a phone scan. Lastly, it will scrape twitter using the birthday 
keyword to help find the birth date of the target.

All results will be stored in a folder named after the username. 


## Table of Contents
[Installation](#Installation)

[Usage](#Usage)

[Credits](#Credits)

[Upcoming Features](#Upcoming_Features)

## Installation
`git clone https://github.com/zabsec/OSINTAutomation`

`chmod +x setup.sh`

`sudo ./setup.sh`


## Usage

`./PersonalOSINT.py`

## Credits
A huge thank you to the creators of 

  https://github.com/twintproject/twint,
  
  https://github.com/sundowndev/PhoneInfoga,
  
  https://github.com/sherlock-project/sherlock, and
  
  https://github.com/sc1341/InstagramOSINT!
  
This automation tool is dependent on the tools you've made so I'm very grateful for your work. 

 
##  Upcoming Features
- Help menu
- Better implementation so arguments can be inserted at the command line
- More options for scraping already available social media sites
- Partial LinkedIn Scraping
