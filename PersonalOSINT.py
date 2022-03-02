#!/bin/python3
import os
from InstagramOSINT import *

username = input("Enter a name you want to search: ")
searchParse = username.split()
isPhone = False
phone = (input("Enter a phone number if you want to initiate a phone scan. Press Enter if you do not want to initiate "
               "a phone scan: "))
phone.strip()

if phone == "":
    isPhone = False
else:
    phone = int(phone)
if "+" in phone:
    phone.replace("+", "")

if phone == int and len(str(phone)) == 10:
    isPhone = True
else:
    isPhone = False


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class PersonOSINT:

    def usernameSearch(self):
        """
        Get a username from the user and use sherlock to search for it in different websites.
        Use verbose mode for sherlock and put the results into a file of their own.
        """

        print(colors.BOLD + colors.OKGREEN + "Disclaimer: Some of the found usernames might be false positives."
                                             " I recommend checking each link to verify.")
        os.system(f"sherlock {username} --verbose -o UserSearch.txt")

        def Instagram():
            """
            We are going to use InstagramOSINT from github to crawl information about an instagram account on here.
            """

            print(colors.OKBLUE + "Processing Instagram data...")
            instagram = InstagramOSINT(username)
            print(instagram.username + " profile summary:\n")
            try:
                instagram.scrape_profile()
                if instagram.scrape_profile() is instagram.profile_data:
                    instagram.save_data()
                    instagram.scrape_posts()
            except:
                pass

        Instagram()

        def Twitter():
            """
            We are going to be using twint from Github to scrape the whole twitter account.
            """

            print(colors.OKGREEN + "Scraping Twitter data...")
            os.system(f"twint -u {username} -ho -o TwitterScrapeData.txt")
            print(colors.OKGREEN + "Twitter scraping completed.")

        Twitter()

    def phoneSearch(self):
        """
        We will be using the phoneinfoga tool here which we will install on our system.
        """

        if phone == "":
            print(colors.WARNING + "No phone number given. Moving on with scan...")
        elif isPhone is True:
            os.system(colors.OKBLUE + f"phoneinfoga scan -n +{phone}")
        else:
            print(colors.FAIL + "Invalid phone number input. Use E164 or Internal formats only.")

    def birthDate(self):
        """
        we will use Twitter scraping for this. We can search the name then use intext:"birthday" and see what we
        can find in different social media platforms. We will search using the twint tool.
        """
        print(colors.OKGREEN + "Looking for birthday references on Twitter...")
        os.system(f"twint -u {username} -s birthday -ho -o BirthdayTwitterScrape.txt")

    def createFolder(self):
        """
        Once the user inputs a search by a name, see if a folder already exists in that name.
        If it does not exist, create one and store everything in there.
        """
        if os.path.exists(f"{username}"):
            os.chdir(f"{username}")
        else:
            os.mkdir(f"{username}")
            os.chdir(f"{username}")

    if __name__ == '__main__':
        createFolder("")
        usernameSearch("")
        phoneSearch("")
        birthDate("")
