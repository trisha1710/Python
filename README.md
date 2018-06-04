# Python
Genreating messages-:

to generate messages, first create the instance of the class-:
msg = simplefix.FixMessage()

Then we can add tags and fields to it. All the tags mentioned in the python script is added which are below-:

8=FIX.4.2 (always this value)
35=D (always a new order message ‘D’)
55=SYMBOL_N (Symbol meaning the product name: N is a number) Note that in real life this could be a stock like GOOGLE
54=[1-2] side (buy or sell the given symbol/product)
38=N (quantity of the symbol/product that you want to buy or sell)
40=[1-5] (only order types 1-5 per the FIX 4.2 spec: http://btobits.com/fixopaedia/fixdic42/tag_40_OrdType_.html)
59=[0-6] (all time in force orders per FIX 4.2 spec: https://www.onixs.biz/fix-dictionary/4.2/tagNum_59.html)
1=CLIENT_N (random client id)
44=Any price (price at which you will sell or buy the given product)

Append_pair() has been used to add modify and add more fields to the message. 

After setting all the fileds like append_time(), append_data() etc. encode() is used which will return buffer that correctly initialise FIX messages.





MESSAGE PARSER-: 

To extract the messages, FixParser class is used. you can call message by get_message() and if its not complete, it will return none value.
After extracting messages, number of fileds can be checked with count().



Script 2- STATISTICS

using library called pandas, raw data is accessed. once the data is extracted, X variables and Y variables are declared where X is independent variables and Y is response variable. 

Then, using sklearn library, data is split into training and test test to develop machine learning algorithm to analyse data.

By using, calss named LogisticRegression, classifier object is created and classifier,fit method is called.

By using pythoin library called matplotlib, data is visualise through various plots like scatter and histograms.

With the help of classification_report class, you can also get the accuracy of the dataset.
