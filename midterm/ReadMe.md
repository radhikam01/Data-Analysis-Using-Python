
# QUESTION 1

# Using Enron data-set, perform 3 analysis

# Introduction:
Enron started life as a regional natural gas pipeline company, the result of a merger between Houston Natural Gas and InterNorth in 1985. Lay was credited with transforming Enron into the world's largest energy trading company and America's seventh-biggest corporation. The Enron scandal, revealed in October 2001, eventually led to the bankruptcy of the Enron Corporation, an American energy company based in Houston, Texas, and the de facto dissolution of Arthur Andersen, which was one of the five largest audit and accountancy partnerships in the world.

# ANALYSIS 1
# Finding out the count of the number of emails sent from each user in the inbox folder

Enron consists of a lot of employees and these employees have email exchanges on a regular basis. My analysis is based on these email exchanges. It will give the count of the number of emails sent by each employ in the inbox folder.

# Process:

1) Traversing through the mail directory which consists of all the users

2) Using os.listdir, fetching all the users

3) Traversing through all the users to find out the inbox folder of each user

4) Using glob, opening the list of these inbox folder and fetching a particular file 

5) Using email parser, fetching the data for 'From' content

6) Looping through all the inbox files to get all the 'from' content from these files

7) Pushing this 'from' content into a dictionary 

8) Running a counter to find out the count of each user




```python

```

# Results:

!['From Content Emails'](Output Files/From_Content_Emails.jpg)

# Conclusion:

- According to the screenshot, 'greg.johnston@enron.com' has sent the maximum number of emails followed by liz.taylor@enron.com and so on. 
- Therefore, by this analysis we can figure out how many emails have been sent by a particular user.

# ANALYSIS 2:

# Finding out the maximum number of email exchanges in each year

In the Enron dataset, I want to find out the most number of email exchanges in each year. Therefore, my analysis is based on the date of the email and the number of emails.

# Process:

1) Traversing through the mail directory which consists of all the users

2) Using os.listdir, fetching all the users

3) Traversing through all the users to find out the sent_items folder of each user

4) Using glob, opening the list of these sent_items folders and fetching a particular file

5) Using email parser, fetching the email data 

6) Using this email data, parsing the date

7) Through time stamp, fetching the years

8) Using if, checking if the years is not in the list, then add it into the list and increment the counter

9) Looping through all the inbox files

8) Using the counter, checking the files based on the years and adding it into list

9) Writing the result into a csv

# Result:

!['Years Count'](Output Files/Years_Count.jpg)

# Conclusion:
- According to the screenshot of data, the most number of emails were exchanges in the years 2001
- Therefore, this analysis shows us the most number of email exchanges in each year

# ANALYSIS 3

# Finding out the maximum times a particular word is used in the subject line of inbox folder

In the Enron dataset, finding out the maximum number of times a particular word is being used in the subject line while drafting an email. This analysis will give us the most frequently used words in the subject line.

# Process:

1) Traversing through the mail directory which consists of all the users

2) Using os.listdir, fetching all the users

3) Traversing through all the users to find out the inbox folder of each user

4) Using glob, opening the list of these inbox folder and fetching a particular file 

5) Using email parser, fetching the data for 'Subject Line' content

6) Looping through all the inbox files to get all the 'Subject Line' content from these files

7) Pushing all the subject lines into a list

8) Replacing content like 'Re', 'FW', 'Fw' and 'Fwd' by ' ' so as to only get the meaningful words in the subject line

9) Creating a wordcloud to fetch the most frequently used words in the subject line and plotting in a way that the most frequently used word would be shown in the biggest font

# Result:

!['Subject_Frequency'](Output Files/Subject_WordCloud.jpg)

# Conclusion:

- According to the screenshot, the most frequently used words are 'Enron', 'Meeting' and 'Budget' followed by 'Committee', 'Energy' and so on.
- Therefore by this analysis, we can find out the most frequently used words in the subject line


```python

```

# QUESTION 2

# Use NYT API to collect NYT data. Perform 3 analysis on the collected data

# Introduction:

NYTimes.com is an unparalleled source of news and information. There are a lot of data contents from which we can pick up data and analyze it. The topics of data content include : Archive data, Article search data, Books data, Community data, Geographic data etc. NYTimes.com lets us fetch API in order to read the data and analyze it. 

# Collecting Data and Storing Data:

In order to read the data, we have to fetch the API key. 

# Process:

1) Fetch the API key through the NYTimes.com site

2) Defined a function for the date range, that is the start date and the end date.

3) The function will calculate the following:
- If the start date is less than or equal to end date, and the range is defined as the difference between the dates plus 1, it will return us a combined result of start date plus datetime.
- Otherwise, if will return us combined result of start date minus the datetime.

4) Defined a function to convert the data we have generated:
- If the input is a dict, it should convert the input into key, values form 
- Else if convert to list

5) Defined a function to join the .json files with the path:
- Joining the json file with the path as date.pageno.jsonfile
- Returning that particular path with the filename

6) Defined a function to get the data by using the date, query, api_key and the path:
- Looping through the page range of 2, we will get the data by using the request module. 
- The link is provided which contains the date, query, api_key i.e. 
http://api.nytimes.com/svc/search/v2/articlesearch.json?q="+query+"&begin_date=" + date + "&end_date=" + date + "&page=" + str(page) + "&api-key=" + api_key
- Using the previous function which converts data for this particular data which we have generated
- We check if the length of the article is greater than 1, only then we write the contents of the file
- Else we go into the exception block

7) Defined a main function which would read the config file:
- My config file has the path of to the json files and path to the logfile 
- It also contains the query, start dates, end dates and api key
- Assigning the contents of config file to a respective variables
- Creating the logging file with the particular datetime
- Running this function would filter the data coming from api accordingly and write into the json folder

8) The above function will store the data into the required folder

# ANALYSIS 1

# Finding out the most common keywords in all the sections of article search data

Article Search has a wide amount of data. This data is subcategorized according to the keywords in the data. Keywords is an important element in the article search data as it describes the kind of data inside the whole file. My analysis consists of the most frequently used keywords in the article search data. 

# Process:

1) Fetching the path where the .json files are kept

2) Putting a condition which is checking if the files is ending with .json, only then it will go into the variable

3) Looping in all the .json files and opening each file using glob

4) Reading the .json file by using 'json.loads(open(filename).read())'

5) Since it is a dictionary inside a dictionary, we are going inside the 1st dictionary which is 'response' and then the second dictionary which is 'docs' 

6) Once we are inside 'docs', we loop through it to get the 'keywords'

7) Since the keywords has an element called value, we put an if condition and take all the data inside that

8) For all the data inside the variable, we are appending the values into a list from a dictionary where the key == value

9) We then initialize a counter and check for the most frequently used words in those keywords data

10) We categorize it by using most_common function which will give the descending order of values

11) After we have the count and the value, we write it into a csv file

# Result:

!['Keyword_Frequency'](Output Files/Keyword_Frequency.jpg)

# Conclusion:

- According to the data and the screenshot, the most frequently used values in the keyword section is 'Presidential Election of 2016'. This clearly shows that this was the main topic of discussion.
- Therefore this analysis proves that the 'Presidential Election of 2016' was the most frequently used in the data followed by Donald Trump

# ANALYSIS 2

# Finding out top ten sections which are talking about crime and related things in the article search data

In this analysis, I am trying to find out the areas where crime, justice, police and such related things are talked about. The article search data has a number of sections for example World, US, Sports etc. The analysis will be based on the top 10 sections where the topic of crime and justice is talked about.

# Process:

1) Fetching the path where the .json files are kept

2) Putting a condition which is checking if the files is ending with .json, only then it will go into the variable

3) Looping in all the .json files and opening each file using glob

4) Reading the .json file by using 'json.loads(open(filename).read())'

5) Since it is a dictionary inside a dictionary, we are going inside the 1st dictionary which is 'response' and then the second dictionary which is 'docs' 

6) Once we are inside 'docs', we loop through it to get the 'section names'

7) We are also looping through the same files to get the 'lead_paragraph' 

8) We are looping through the lead_paragraph because we need to search the words like crime, justice in the lead_paragraph which will give us the count of the times it has been talked about

9) Since the lead_paragraph is a string, we are tokenizing it so that each word is splitted

10) We now loop through each section_name in the file and then loop through the tokenized lead_paragraph inside it

11) We then search for the words like 'crime', 'justice', 'police' in the tokenized list of words

12) An empty dictionary is opened, and each time the words match we put them into the dictionary and increment it everytime it is found again

13) This way, we have the section name and the words that are matching the given criteria

14) We categorize it by using most_common function and fetching the top 10 sections talking about crime

15) After we have the count and the value, we write it into a csv file

16) This csv file is opened and the contents are put into a list

17) We now plot the graph between the top 10 sections and total number of counts (frequency of words) as x and y axis respectively

# Result:

!['Most_Talked_Crime_Sections'](Output Files/Most_Talked_Crime_Sections.jpg)

# Conclusion:

- According to the screenshot and data, the 'World' section is talking about crime, justice the most. Followed by U.S, NY Region and so on.
- The analysis is hence proving that the section where crime and justice is mostly talked about is 'World'.

# ANALYSIS 3

# Considering the 'Most Popular' API, finding out the most sharing and most viewing of articles in the year 2017 according to months

In this analysis, I am finding out the months in which the sharing was maximum and so on. The same way, I am finding the months in which the views were maximum and so on. The analysis will give us a plot showing the same.

# Process:

1) Fetching the path where the .json files are kept

2) Putting a condition which is checking if the files is ending with .json, only then it will go into the variable

3) Looping in all the .json files and opening each file using glob

4) Reading the .json file by using 'json.loads(open(filename).read())'

5) Since it is a dictionary inside a dictionary, we are going inside the 1st dictionary which is 'copyright' and then the second dictionary which is 'results'

# For total shares:

6) Once we are inside 'docs', we loop through it to get the 'total_shares'

7) We are also looping through the same files to get the 'published_date'

8) We are looping through the published date to get the date in which the sharing happened

9) Using strptime, we strip the time into year, month and date

10) We then take the months from this stripped time and append it into a list

11) Now we run a loop where we check each month and get the total_shares of those months in a dictionary

# For total views:

12) Once we are inside 'docs', we loop through it to get the 'views'

13) We are also looping through the same files to get the 'published_date'

14) We are looping through the published date to get the date in which the viewing happened

15) Using strptime, we strip the time into year, month and date

16) We then take the months from this stripped time and append it into a list

17) Now we run a loop where we check each month and get the views of those months in a dictionary

18) We plot both the graphs where the x axis shows the months data and the y axis shows the number of shares/views

# Result:

!['Most_Sharing'](Output Files/Most_Sharing.jpg)
!['Most_Views'](Output Files/Most_Views.jpg)

# Conclusion:

- According to the screenshot and data presented, the Most shares and most views in 2017 are for the month of February for both.
