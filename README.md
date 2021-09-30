# EC601_project2
 
## Part(a): Twitter API

The results are in the folder "Twitter_API"

* Find all tweets from a specific user

In the folder named "all_tweets", I just use the code which the professor showed in class. It helps me to get all tweets from a specific user. I choose "@BlackMyth_GS" as my test subject and I get all tweets and put it into twitter.json.

* Find tweets from a specific keyword
Sometimes, we need to find tweets by keywords. So I just try it and my keyword is "blackmythwukng". There have lots of tweets, so I just let count=10. I put it into tagfind.json. And the code is in the folder named "find_keyword".

P.S. For account security, I read my key.txt as input. If you want to test the code, please use your own key.

## Part(b): Google NLP

The results are in the folder "Google_NLP". It is the first time I use this, so I am not quite sure about it. I just use the basic dataset which google provides me.

* AutoML Text & Document Classification

This is for text classification. I chose the single-label training method. For the known data set, it will train it and classify the input content according to the defined label. The basic conditions and simple tests of the data set are in the "AutoML_text" folder.

* AutoML Sentiment Analysis

This analysis is mainly aimed at people's emotions. In this section, we used people's opinions on Claritin dataset which is provided by Google. The data set divides people's emotional level into five grades. In my own test, I also selected several different levels of evaluation, and the data sets all gave more appropriate judgments. The result is in the "AutoML_sentiment" folder.