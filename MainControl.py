#This python file is the brains of the program.
#This is where all the prompts are asked and where information is given to the user
if __name__ == '__main__':

    search_name = ""

    create_option = ""
    create_folder_location = ""
    create_url_list = []

    crawl_re_list = []
    crawl_seed_urls = []

    print("Welcome, please select what would you like to do:")
    while True:
        initial_task = input("[search] [create] [crawl] [help] [quit]\n")
        initial_task = initial_task.strip()
        initial_task = initial_task.lower()

        if initial_task == "help":
            print("The SEARCH option will ask you what database you'd like to search through.\n"
                  "This assumes that there is a database to search through\n")
            print("The CREATE option will create a database for you to later SEARCH through\n"
                  "You can provide a folder of html documents, a list of website URLs, etc. for me to use to \n"
                  "in order to construct a searchable database\n")
            print("The CRAWl option will go through the internet and retrieve data based on your specifications.\n"
                  "I can then use that data to CREATE a structure for you to SEARCH through\n")
        elif initial_task == "search":
            search_Name = input("What is the name of the database you would like to search through?")
            break
        elif initial_task == "create":
            create_option = input("Please choose what you would like to create the database from:\n"
                                 "[html]\n [url]\n")
            if create_option == "html":
                create_Folder_Location = input("Please input the path of the folder containing your HTML files")
            if create_option == "url":
                create_url_list = input("Please enter in your list of URLS separated by commas")
            break
        elif initial_task == "crawl":
            crawlDomain = input("Please enter a series of re-expressions, separated by commas, that you wish to be allowed domains for the crawl")
            crawl_re_list = crawlDomain.split(",")
            crawlSeed = input("Please enter a series of seed urls, separated by commans, that you wish to begin the crawl with")
            crawl_seed_urls = crawlSeed.split(",")
        elif initial_task == "quit":
            print("Goodbye")
            break
        else:
            print("Sorry, please choose one of the listed options")



