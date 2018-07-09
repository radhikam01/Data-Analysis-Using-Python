
# DATA ANALYSIS ON DIFFERENT KINDS OF WORLD MUSIC GENRES, ALBUMS, BANDS AND THEIR REVIEWS

# Introduction:

The music industry has provided us with millions of amazing songs which come from all over the world. Being a music fan, my final project is based on analysis of different kinds of music genres, albums and bands from across the world.

# ANALYSIS 1

# FINDING OUT THE TOP AND DISTINCT GENRES FROM ACROSS THE WORLD

Overview: This analysis has two parts. The first part finds out the top 10 genres from across the world which are the most common.
The second analysis finds out the distinct genres based on the years.

# Part 1: Top 10 genres from across the world 

# Process:

1. Reading the World_Music_Band_Detais.csv file which consists of all the bands details with their genres
   using pandas pd.read_csv 
   

2. Using groupby, grouping by all the band genres 


3. Using the function count, counting the band genres and then using sort_values function to sort the values 
   of the count 
    
    
4. Using tail function, picking out the top 10 genres which are already sorted in ascending order


5. Creating a new column called 'others' which has all the other genres apart from these top 10 genres


6. The others column is created by using shape function to get the demensions of our dataframe and subtracting it 
   from the sum of the top 10 genres
   
    
7. Defines 10 colors in the variable called colors 


8. Using plot.pie, created a pie plot for all the top genres


9. Using plt.Circle, created a white circle and added that on this pie chart to create a donut chart


10. Using plt.show, showcasing a donut chart which has the top 10 genres from across the world

# Result:

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_1/Donut_Chart_Genres.PNG)

# Part 1 Conclusion: 

According to the screenshot: 
- the genre which has the most number of songs is 'Rock'. Therefore, the top most genre is Rock which is 32.5% of all the top 10 genres.
- Followed by 'Rock' is 'Alternative' which has 26.6% of all the top 10 genres. 

# Part 2: Number of Distinct Genres Released in a Particular Year

# Process:

1. Using drop_duplicates function, dropping all the duplicates so that we only have unique and distinct genres

2. Using groupby, grouping by the year of the band formation and taking the count of all the genres for that year
   by using the count function

3. Putting this data into a dataframe by using pd.Dataframe

4. Resetting the index to align the columns by using reset_index function

5. Using plot.barh, plotting a horizontal bar graph for this particular data

6. The result of the the dataframe is written into a csv file using to_csv()

# Result:

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_1/Distinct_Genres.PNG)

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_1/Distinct_G_Plt.PNG)

# Part 2 Conclusion:

According to the screenshots: 
- In 2005 there were the most distinct number of genres released with a count being of 111.
- Following that is 2006 with a count of 98 genres and then 2003 with a count of 94 genres.

# ANALYSIS 2

# FINDING OUT THE MOST PROLIFIC BANDS AND ALBUMS ACROSS THE WORLD

Overview: This analysis has two parts. The first part finds out the top 10 most productive bands based on the number of albums released by that particular bands. The second part finds out the top 10 most productive albums based on the number of reviews recieved by that particular album.

# Part 1: Most Prolific Top 10 Bands By The Number of Albums Released

# Process:

1. Reading the World_Music_Band_Detais.csv, World_Music_Album_Details.csv and World_Music_Review_Details.csv file 
   using pandas pd.read_csv 
    
2. Since we want to get a dataframe in which all the band names are there according to their albums, we merge the 
   bands and albums dataframes to create a new dataframe based on the band_id and album_id
    
3. Using pd.merge, we take the bands data into left and albums data into right, taking the id of bands and bands_id
   from albums data we create a new dataframe called music_bands_albums_join
    
4. Using groupby, grouping by the new dataframe by taking the bands and albums id and counting the sorted values using
   count() and sort_values() function
    
5. Using tail function, picking out the top 10 bands which are already sorted in ascending order

6. Creating a new column called "bands_count" for the count of the top 10 bands with their IDs

7. Resetting the index to align the columns by using reset_index function

8. Using the indexed file, merging it with bands_details table to get the band names instead of their IDs

9. Using sns.barplot, plotting a bar graph to showcase the count and the band names which are the most productive by
   the number of albums released
    
10. Used palette as 'Greens' with an edgecolor of '0.2' 

11. The result of the the dataframe is written into a csv file using to_csv()

# Result:

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_2/bands_top10.PNG)

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_2/top10_plot.PNG)

# Part 1 Conclusion:

According to the screenshots:
- 'Led Zeppelin' is the most productive bands because it has the most number of albums 
   released. The total number of albums released by 'Led Zeppelin' is 23.
- Following that is 'Megadeth' which has 18 number of albums released and is second most productive band

# Part 2: Most Prolific Top 10 Albums By The Number of Reviews Recieved

# Process:

1. Using pd.merge, merging the previous dataframe where we got all the bands according to album IDs to the reviews file to
   get the reviews for those particular albums. Naming this dataframe as music_bands_albums_reviews_join
    
2. Using groupby, in the new dataframe 'music_bands_albums_reviews_join' grouping by the Albums IDs and taking the 
   count of the IDs of the reviews of those particular Albums IDs
    
3. Sorting the result using sort_values() and using tail() function, picking out the top 10 genres which are 
   already sorted in ascending order
    
4. Putting this count into a new column called as 'reviews_count' which also has the respective album IDs

5. Using this file, merging it with 'music_bands_albums_join' table to get the album names instead of their IDs

6. Creating a new column with band name along with the album name in the same column

7. Using sns.barplot, plotting a bar graph to showcase the count and the album names which are the most productive by
   the number of reviews recieved for that particular album
    
8. Used palette as 'Blues' with an edgecolor of '0.2' 

9. The result of the the dataframe is written into a csv file using to_csv()

# Result:

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_2/albums_top10.PNG)

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_2/albums_top10_plot.PNG)

# Part 2 Conclusion:

According to the screenshots:
- Qrixkuor's "Legion" where the band's name is Qrixkuor and the album's name is 'Legion' is the most productive album because it has the   most number of reviews recieved. The total number of reviews recieved by 'Legion' is 46.
- Following that is Qrixkuor's "Scars of the Crucifix" which has 30 number of reviews recieved and is the second most productive album

# ANALYSIS 3

# Finding out the Top 10 Albums According to Review Scores Given by Listeners

Overview: Millions of people listen and critic music acording to their taste and genre. This analysis finds out the top 10 albums of all times based on the number of scores given by reviewers. 

# Process:

1. Reading the World_Music_Band_Detais.csv, World_Music_Album_Details.csv and World_Music_Review_Details.csv file using pandas pd.read_csv 

2. Using pd.merge, joining the bands details data with the albums details data on the bands ids in both the files using a left join. Naming this as music_bands_albums_join.

3. Using pd.merge, joining the previous generated file with reviews details data on the Album IDs from both the files
   using a left join. Naming this as music_bands_albums_reviews_join.
   
4. Using groupby function, grouping on the Album IDs and taking the count of that using review IDs

5. Only taking into account the reviews which have got a score of more than 8, as I am considering only those to be the top reviews albums

6. Calculating the average score of the albums by calculating the sum of albums scores grouped by Album ids and dividing it by the count of those albums

7. Putting this data into a dataframe using pd.Dataframe

8. Sorting this data into ascending order and using tail function, picking out the top 10 albums using tail(10)

9. Creating a new column called 'average_score' to put in the average scores

10. Using pd.merge, joining the previous data frame which has average score and albums with the music_bands_albums_join
    on the album_id and extracting only the albums names, band names and average scores
    
11. Creating a new column with band name along with the album name in the same column
    
12. Plotting a horizontal bar graph with this data and using annotate function, showing the average score on that particular bar

13. Used color as yellow and edgecolor as 0.2

14. The result of the the dataframe is written into a csv file using to_csv()

# Result:

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_3/top10_reviewscores.PNG)

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_3/top10_reviewscores_plot.PNG)

# Conclusion:

According to the screenshots: 
- 'Anaclasis: A Haunting Gospel of Malice & Hatred' where 'Anaclasis' is the Band name and 'A Haunting Gospel of Malice & Hatred' is the    top most album with an average score of 0.9675. This means that this album is the most reviewed album by the listeners.
- Following that is 'Realm of Chaos: Slaves to Darkness' where 'Realm of Chaos' is the band name and 'Slaves to Darkness' is the second    top most album with an average score of 0.940526. 

# ANALYSIS 4

# FINDING OUT THE FORMATION OF TOTAL BANDS AND ALBUMS ACROSS ALL THE YEARS AND MOST NUMBER OF WORDS USED IN REVIEWS

Overview: This analysis gives us the total number of bands formed and the total number of albums created over all the years.
This analysis also tells us what the reviewers have been talking about the most in their reviews.

# Part 1: Creating of Total Number of Bands and Albums Across all Years

1. Reading the World_Music_Band_Detais.csv, World_Music_Album_Details.csv and World_Music_Review_Details.csv file using    pandas pd.read_csv

2. Using groupby function, grouping by the Band formation Year and taking count of ID

3. Using cumsum() function, taking a sum of all the counts according to the count of each year and putting this into      music_bands_count

4. Using groupby function, grouping by the Album Release Year and taking count of ID

5. Using cumsum() function, taking a sum of all the counts according to the count of each year and putting this into      music_albums_count

6. Using pd.DataFrame, creating a dataframe of these two files - music_bands_count and music_albums_count so that we      have the count of both bands and albums with year column

7. Using sns.heatmap, creating a heatmap to show the variation of creation and release of bands and albums according to    each year

8. Used a linewidth of 0.5 to distinguish between each year

9. The result of the the dataframe is written into a csv file using to_csv()

# Result:

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_4/Bands_albums_creation.PNG)

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_4/bands_albums_heatmap.PNG)

# Part 1 Conclusion:

According to the screenshots:
- 2017 has the most number of albums released which is 12618 to be precise followed by 2016 which is 12614 and 2015 which is 11818. The   screenshot also shows that in 1986, 1984, 1982, 1981, 1980   and 1978 there were no new album releases.

- According to the screenshots, 2016 has the most number of band formations which is 11261 followed by 2015 which is 11234 and 2014 which is 11118. The screenshot also shows that 1979, 1973, 1971, 1969, 1968, 1966, 1965, 1964 and 1963 there were no new band formations

# Part 2: Most Number of words used in Reviews given by Listeners

# Process:

1. Using the World_Music_Reviews_Details.csv, taking out the reviews columns to show the most used words in reviews by    creating a wordcloud of the same

2. Removing all the stop words, keeping the background_color as Black, width as 1600 and height as 800

3. Plotting the reviews in such a way that the most used words in reviews would be in bigger fonts

# Result:

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_4/wordcloud.PNG)

# Conclusion:
According to the wordcloud screenshot:
- The most used word in reviews in 'death metal' followed by 'sound' and 'song'.
- This conclusion tells us that the listeners have reviewed most about 'death metal' and therefore there are a lot of 'death metal' fans   out there.

# ANALYSIS 5

# FINDING OUT TOTAL NUMBER OF ACTIVE/NON-ACTIVE BANDS ACCORDING TO GENRE AND COUNTRY

Overview: Many bands start off with a great career but end up splitting after a few years. This analysis tells us about the total number of active and non-active bands according to the genre and country

# Process:

1. Reading the 'World_Music_Bands_Details.csv' file as it has all the bands with their country and genre using
   pandas pd.read_csv 
    
2. Defined a function called 'replace_punctuation' with parameter as raw and replacement = ''. This function is 
   replacing all the punctuations in the input string with a space
    
3. Using the regex function, compiling the string and escaping all the punctuations in the input string 

4. Using re.sub, generating an output with only the input string of the genre

5. Defined another function called 'split terms' with parameter as raw. This function is splitting the input string 
   on all spaces and punctuations by using the function .split() and getting a new output with only the terms
    
6. To get a list of unique terms of genres, putting these terms into a single list called all_terms

7. Using np.unique, getting all the unique terms and their counts

8. Using pd.DataFrame, putting these terms into a dataframe and using sort_values, sorting by count in a descending manner.

9. Since I want to represent my data with a binary matrix where each column represents the unique term and each row
   represents the a band, using MultiLabelBinarizer will transform between iterable of iterables and multilabel format
    
10. We are creating binary terms and putting them in a variable called binarized terms

11. Tranforming the data into new data by using pca.fit_transform to transform the binary term into array like

12. I want to create clusters for my genre data, hence using DBSCAN, creating clusters using dbscan

13. Using np.unique, taking out the unique number of clusters which in my case are 5

14. Looping through all the cluster data to pull out the top genre terms in each cluster and take out the count 

15. Defined a function called as count_terms to iterate through each genre and take out the count of terms and then 
    putting it into a dataframe called as counted_terms
    
16. Looping through all the clusters to pull out the cluster data and put them into its location using indices

17. Using groupby, grouping by the Country and counting the terms of genre and then sorting the values

18. Taking out only those genres which have active as the Band_Status 

19. Taking out only the top most genre out of all the unique terms

20. Defining color for the clusters and creating horizontal bar graphs representing only the active bands 

21. Overlaying the horizontal bars which are representing all the bands so that we can get both 'Active' and 'Non-Active' bands data
    
22. Showcasing the plots according to clusters which shows both active and non-active bands

# Result:

![alt text](https://github.com/radhikam01/maheshwari_radhika_spring2017/blob/master/Final/Analysis/Ana_5/cluster_plot.PNG)

# Conclusion:

According to the screenshot:
- US is at the top of each cluster and has the most number of Active and Non-Active bands.
- This is followed by Germany which has the second most number of Active and Non-Active bands.

According to the 5 clusters:
1. In Metal genre, US has close to 70 Active bands out of total of 120. But Germany has 20 Active and more than 20 Non-Active bands.
2. In Rock genre, US has less than 100 Active bands out of total of almost 200 bands which tells us that in Rock genre, more Non-Active bands are present
3. In Death genre, US has total of 20 bands, only 6 are active
4. In Alternative genre, US has 75 active bands out of a total of 140 bands which tells us that there are more Active bands of Alternative genre in US
5. In Pop genre, US has more than 30 Active bands out of 48 total bands which tells us that there are more Active bands of Pop genre in the US
