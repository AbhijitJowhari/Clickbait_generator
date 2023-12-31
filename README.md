# **Clickbait_generator**

This a repository that contains the API for the clickbait generator. All the required files are stored as a package in the ‘API’ folder.

## ***Instructions to run the model***
* The model needs the weights.sav file to load the weights. Please use the below link to download the weights.sav file and store it in the API folder.
> https://drive.google.com/file/d/183ogoZ3mqCo7E9OqDxbR7IlCUaaMs-Fr/view?usp=sharing
* After keeping ***all the required files*** in the API folder, Open CMD in that folder and pass the following argument:
> python run.py

Here note that if the libraries mentioned in the disclaimer section are not installed then it will first install them and then run the API. This may take a few minutes.
* After this the API shall run and the model is ready for testing.

## ***DISCLAIMER***

* When my model is put to testing, it many a time is expected to generate sentences which don't make much sense. It is therefore my humble request to the evaluator to please also focus on the semantics. I did not have the adequete RAM to train the model on whole of the data. Even google colab and kaggle could not handle the dataset and repeatedly crashed.

  I also urge the evaluator to generate atleast 20 sentences while testing to get a fair idea of the model's performance.

* Please have a proper internet connection while testing if the local machine on which model is being tested does not have one (or more) of the following libraries installed:
  >torch==2.0.1
  >joblib==1.2.0,
  >streamlit==1.23.1

* The frontend should load in about 30 seconds after run.py is executed from cmd. Please be a little patient :)

* The command line commands loaded in the python script are for a windows based PC. Therefore please use a windows OS to run the code.

## ***Some examples of text generated by my model !***

* Where's The World .
* Here's The Documentary About .
* Tell You Are The Worst .
* Stephanie Birth Month .
* 27 Last-Minute Stocking Inclusive America .
* 36 Seriously Prescribed Emotion .
* Charli Network Competition Should You Laugh .
* How Romance's Hottest Ryan Gosling Hip Were Horrified .
* Can We Know What You're Slightly Obsessed With Meghan Trainor .
* Shaggy Turns Apple's Founder Into Paying Darkest Textbook Easy, Bestow Upon Your Zodiac Sign .

*NOTE:* The above generated text does not make much sense but is semantically sound in most of the cases. as aforementioned I didn't have the reqiured RAM to train the model I have therefore trained the model on only 20% of the data . [Even this took 5 hours of training ! :( ]

<img width="254" alt="20%" src="https://github.com/AbhijitJowhari/Clickbait_generator/assets/127199703/385407f6-7e75-4af1-b2f1-bebe05234162">



Now Let me breeze you through my work.

## ***A walk-through***

* **Run.py:** This is the main python file responsible for putting together all of the stuff and running my language model.

* **app.py:** This is repsonsible for the API of my model. This also provides my model a very rudimentary frontend which is designed using some basic Streamlit scripts.

* **Clickbait_generator.py:** This is the heart of my model. This puts togeather all the files (like weights.sav,seed.sav etc.) and returns a randomly generated clickbait when queried using the API.

* **Weights.sav:** This file stores all the trained weights of the model. This is basically my trained model which gets loaded everytime a query is received.

* **seed.sav:** This is the manual seed used to contruct the generator object which inturn is used to generate the clickbait from a multinomial probability distribution as we shall later see.

* **stoi.sav:** This file stores a python dictionary which maps all the unique set of words in the training data to its unique index

* **itos.sav:** This files stores the inverse mapping of the above dictionary stored in the above file.

* **notebook.ipynb:**  This is the notebook which containes the training code of the model. It is to be kindly noted that this notebook file is not required to run my model and is just for the evaluator to asses my training of the model. 


## ***Detailed attestation***
<font size="100"> _But, Talk is cheap, I'll show you the code !_ </font> 


### **notebook.ipynb**
---
First I import all the necessary modules and libraries.

Then from the training data, I segregated all the headlines which were clickbaits into a seperate training list:

<img width="669" alt="1" src="https://github.com/AbhijitJowhari/Clickbait_generator/assets/127199703/6e668961-d84e-4941-8186-b97a85a685e8">

Then I contruct dictionaries which store unique words accross all the training examples. I also construct the inverse mapping of the dictionary. As we shall later see, these dictionaries go hand-in-hand to construct a unique elements tensor. Here I have also prepapred a list of inputs to be given to our neural network.

<img width="687" alt="2" src="https://github.com/AbhijitJowhari/Clickbait_generator/assets/127199703/bb652dc0-74ab-4584-9da4-3f01258c250e">

Below, I convert the inputs to One-hot encodings to feed into the neural network. This is a rudimentary way of converting a word to a vector in a finite dimensional vector space for further processing.

<img width="702" alt="3" src="https://github.com/AbhijitJowhari/Clickbait_generator/assets/127199703/ff8d05af-81b5-48c8-b609-d2ef2883d98d">

### **Clickbait_generator.py** 
---

Here again we import all the necessary modules.

Then define a function which returns the clickbait. Here we convert the words to vectors using one-hot encoding. Then feed it into a neural network consisting of randomly generated torch weights. I have kept no hidden layers in this model to keep it simple and save time.

At the end I have used the'softmax' acivation function to get the probability distribution as the output .


<img width="434" alt="CB1" src="https://github.com/AbhijitJowhari/Clickbait_generator/assets/127199703/aacdbee8-1e7f-43d7-836f-778e758451af">![softmax](https://github.com/AbhijitJowhari/Clickbait_generator/assets/127199703/81cfe7ab-b46f-4b08-acfb-e71efd406b57)

### **app.py**
---

Here, this is my API-cum-frontend python code. This has been coded using the streamlit library.


<img width="208" alt="AP1" src="https://github.com/AbhijitJowhari/Clickbait_generator/assets/127199703/1bd4cfb0-f5ad-4538-a430-4595c4562183">

### **run.py**
---

This is the file which runs whole of my language model along with its frontend.


<img width="307" alt="R1" src="https://github.com/AbhijitJowhari/Clickbait_generator/assets/127199703/38b529af-379d-4e7b-bef7-7566f0643c6f">


### **Hyperparameters used**
---

* Learning_rate : 1200
* epoches : 200
* number of hidden layers : Nil
* Vector encoding used  : One-hot encoding
* activation function : softmax
* loss fuction: logarithm of the softmax probability

  ## ***Acknowledgements***
I would give a lot of credit to Andrej Karpathy whom I followed to build this clickbait generator. Also, some of my code snippits are mainly inspired from his work. The video that I followed is:
> https://www.youtube.com/watch?v=PaCmpygFfXo

I would also like to thank shivam kolhe for his GeeksForGeeks article which I followed:
> https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/

I also took help from this medium article:
> https://towardsdatascience.com/using-joblib-to-speed-up-your-python-pipelines-dd97440c653d
