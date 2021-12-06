# EC601_project2

### Phase 1

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

### Phase 2

## Minimum Valuable Product

For my project, the minimum valuable product must include the following funtion. Convert 2D pictures into reasonable 3D models. If my product can do this, it almost reaches our goal.

## User Story

Sally wants to use her favorite model to make an independent game, so that the game she makes is more likely to be loved by everyone.

Peter wants to obtain a three-dimensional image of his favorite anime character so that he can customize a figure.

As a speaker, Bob wants to use a three-dimensional model to illustrate what he is telling, so that the audience can understand it more easily.

## Social Media Analyser

* Modular design

I think sentiment analysis will have a great effect in business. Secondly, it can also be used by psychologists and sociologists for academic analysis.

So for the modular design of this product, I think it should be divided into the following parts. The interface should use web pages, and if mobile terminals are involved, a mobile app is required. At the same time, we need a background training set and training results as well as a data storage and transmission server. I am also going to add an additional training module, so that we can further study the wrong prediction, to continuously improve the accuracy of the product.

1. Web page and mobile app: This should be the interface of our product. It will be publicly showed to everyone. It must have function to allow user to upload their data. Besides, it will contain the output page to show the result to the user. If the amount of data given by the user is relatively large, it will take a relatively long time. A waiting interface is necessary to tell the user that our analysis is in progress.

2. Background training set and training result: If we want to give out a result to user's data, a training result must be prepared. The amount of data in the training set cannot be small to ensure the initial effect of the product. To improve its accuracy, an additional training module will be added.

3. Additional training module: If customers are not satisfied with some prediction results, they can give feedback through the user interface. This module will add the corresponding data to the background data set to improve the analysis capabilities.

4. Storage: A storage is necessary to store the data uploaded by the user and the final output.

5. Calculation: Server part for computing.

The second and fourth parts must be confidential to ensure the security of user data and the product from being copied.

In this part, I also use twitter API to do it and I try to find with tag game model and that is what I want. From the number of the result I get, I can see how many people are interested in this area and my project will be useful.