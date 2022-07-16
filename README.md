# Wordcloud-Covid Vaccine-Analysis

Word Cloud is a visualization technique for text data wherein each word is picturized with its importance in the context or its frequency. 

# Objective:
To help clinicians know more about which symptoms of Covid Vaccine were most frequent among patients in the dataset and then visualize it with the help of a word cloud. Initial data cleaning was done on Google Colab and further explored with the help of Pandas Library. A couple of cleaning methods were applied and the outputs were generated to be downloaded as the final file. 

## Tools used:
Google Colab, Python

## Method :
Once initial data cleaning was done in python both the Word cloud library and matplotlib libraries were imported to help in visualizing the generated plots

There were three primary steps in building a word cloud:
1. Extract the symptoms column from the original file - covidvaccine.xlsx
2. Create and generate a wordcloud image
3. Display the frequency using matplotlib 


<img width="400" alt="code1" src="https://user-images.githubusercontent.com/42086991/174860710-cd05ecc3-c8fe-461b-b3ac-f9515687995e.png">

This is an extract of the Code for getting the Top words that are most frequent in the symptoms file. The firsts step was to load the dataset. Once it was saved in a dataframe, a new variable called text that helps to concatenate all the words in the symptom1 column and count the bag of words for each instance. The concatenation happens with the “join” word in the code. The stopwords were added to make sure unnecessary words were removed from the text to make the wordcloud more relevant. 
Additionally, another variable holds a list of values that were manually excluded to improve the results. Further discussion as to why this list was added is explained in the next chapter.
The "astype" ensures that each value of the text variable holds a string rather than any other data-type as this would hamper the results. 


<img width="400" alt="code2" src="https://user-images.githubusercontent.com/42086991/174860677-4988a8fa-c8a5-4099-840d-b330714d039a.png">"

Once the text had the data from the column it was passed to the WordCloud object that took the stopwords and the text as parameters and saved in a new variable. The variable was then used to pass to the PLT object that helped to display the wordcloud image.
There were three different results at each iteration and new imporvements were done to the code accordingly.

### STOPWORDS:

At one interation, it was identified that the word "site" and "Injection" were appearing larger than the symptoms in the visualisation. As they were repeated in most rows and were irrelevant to our findings to improve the NLP technique more StopWords were added such as "Injection and Site" to create an accurate word cloud for visualisation. 

<img width="400" alt="code3" src="https://user-images.githubusercontent.com/42086991/174860575-23cd30e7-8317-4890-84a5-8912ed5d86e8.png">

### VISUALISED WORD CLOUD:
<img width="1251" alt="wordcloud" src="https://user-images.githubusercontent.com/42086991/174858105-e5c64136-7489-4e4c-9077-7bb2ac953fd6.png">
After few iterations and cleaning of data the word cloud depicted that "Pain" "Headache" and "Fatigue" were the most frequent words and therefore, the most common symptoms that patients experienced from taking the vaccine for Coronavirus.

A second test was done to evaluate the results to see if the frequency count matches the visualization. The code for that test is depicted below.
      
<img width="688" alt="Screen Shot 2022-07-16 at 7 38 23 PM" src="https://user-images.githubusercontent.com/42086991/179361772-21bd445e-ba82-4cf5-a142-e8df9562e802.png">

The value counts method was used in the Bar chart for the top 5 most frequent words in the dataset. 

<img width="530" alt="Screen Shot 2022-07-16 at 7 38 32 PM" src="https://user-images.githubusercontent.com/42086991/179361786-260392e9-6c4e-4b58-b4e3-c22b01e5c02b.png">
The bar chart shows that the model matches the visualization as the frequency count is similar to the biggest words in the Fig above. The word cloud tells clinicians which symptom is most frequent but to get a deeper analysis about the patients a dashboard was created with a summarization of the key values from the dataset.
