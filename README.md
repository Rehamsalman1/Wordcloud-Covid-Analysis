# Wordcloud-Covid-Analysis

Word Cloud is a visualization technique for text data wherein each word is picturized with its importance in the context or its frequency. 

# Objective:
To help clinicians know more about which symptoms of Covid are most frequent among patients in the dataset and then visualize it with the help of a word cloud. Initial data cleaning was done on Google Colab and further explored with the help of Pandas Library. A couple of cleaning methods were applied and the outputs were generated to be downloaded as the final file. 

## Tools used:
Google Colab, Python

## Method :
Once initial data cleaning was done in python both the Word cloud library and matplotlib libraries were imported to help in visualizing the generated plots

There were three primary steps in building a word cloud:
1. Extract the symptoms column (text column)
2. Create and generate a wordcloud image
3. Display the frequency using matplotlib 


<img width="400" alt="code1" src="https://user-images.githubusercontent.com/42086991/174860710-cd05ecc3-c8fe-461b-b3ac-f9515687995e.png">

This is an extract of the Code for getting the Top words that are most frequent in the symptoms file. The firsts step was to load the dataset. Once it was saved in a dataframe, a new variable called text that helps to concatenate all the words in the symptom1 column and count the bag of words for each instance. The concatenation happens with the “join” word in the code. The stopwords were added to make sure unnecessary words were removed from the text to make the wordcloud more relevant. 
Additionally, another variable holds a list of values that were manually excluded to improve the results. Further discussion as to why this list was added is explained in the next chapter.
The astype ensures that each value of the text variable holds a string rather than any other data-type as this would hamper the results. 


<img width="400" alt="code2" src="https://user-images.githubusercontent.com/42086991/174860677-4988a8fa-c8a5-4099-840d-b330714d039a.png">
Once the text had the data from the column it was passed to the WordCloud object that took the stopwords and the text as parameters and saved in a new variable. The variable was then used to pass to the PLT object that helped to display the wordcloud image.
There were three different results each with a new finding and improvement from the previous results.

<img width="400" alt="code3" src="https://user-images.githubusercontent.com/42086991/174860575-23cd30e7-8317-4890-84a5-8912ed5d86e8.png">
##STOPWORDS Evaluation:
However, site was being repeated in the cloud and it was not easy to differentiate between the words as they all look similar in terms of the size. Therefore, to improve the NLP technique another test was performed but with more StopWords added such as Injection and Site. Additionally, the previous test only took one column out of the five columns of symptoms in the 1.2 dataset. Therefore, as explained earlier the data was concatenated into one column. This was used for the next dataset. 

<img width="1251" alt="wordcloud" src="https://user-images.githubusercontent.com/42086991/174858105-e5c64136-7489-4e4c-9077-7bb2ac953fd6.png">
The word cloud highlighted that Pain Rash and Fatigue were the highest most frequent words in the symptoms that patients experienced from taking the vaccine. A second test was done to evaluate the results to see if the frequency count matches the visualization.  The code for that test is depicted below.

                 

The value counts method was used in the Bar chart for the top 5 most frequent words in the dataset. 
                                        

The bar chart shows that the model matches the visualization as the frequency count is similar to the biggest words in the Fig above. The word cloud tells clinicians which symptom is most frequent.
<img width="400" alt="wordcloud" src="https://user-images.githubusercontent.com/42086991/174861688-f7028439-cdb1-4c6c-8bb0-060aad82cd11.png">


      
