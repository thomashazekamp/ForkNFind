# ForkNFind - CA400
- Thomas Hazekamp 
20423602
- Eoin Daly
20424366

- Project Supervisor: Brian Davis

## Introduction
Our project is a restaurant recommendation application for mobile devices, a user will be able to input their interests and reviews for restaurants and using this information and a machine learning recommendation system, the user will receive recommendations of other restaurants that they should be interested in trying.
## Outline
The project will be a full stack application with its main goal of providing relevant restaurant recommendations to users, based on user information and restaurant information, to do this we will implement a robust recommendation system. 
Our recommendation system will be built using a hybrid approach which will take into account both collaborative filtering, like user preference and whether they have rated a restaurant positively, and content based filtering, like the food at a restaurant. We plan to use the python library LightFM and use a Yelp dataset to train and test the model.
The recommendation system will be tested and evaluated using different evaluation techniques to validate that it is performing as expected and will have iterative improvements made to improve the overall performance.
User’s will be able to leave a review for a restaurant and using text analytics and sentiment analysis, we will be able to extract the key features and conclude whether the review was positive or negative
Using the Google Maps API and the user's current location we will be able to get user specific information about the restaurants in the nearby location and be able to display them in the UI.
## Background
While on our INTRA internships we identified a problem about the limited availability of tools for discovering restaurants that would suit our individual tastes and preferences. Due to our busy workloads we would have benefited from an efficient application that would have given user specific recommendations for places to get lunch. This is why we came up with our idea for a restaurant recommendation application that would solve this problem and would have made our lives easier.
This application would also be beneficial whilst travelling to a new place as you would be able to get user specific recommendations in a foreign country based on your likes and preferences. It would help avoid ‘Tourist Trap’ restaurants that only care about providing overpriced food.
## Achievements
A mobile app which is accessible and provides strong recommendations for restaurants which the user would be interested in, using machine learning. Our target audience would be anyone who is looking for new places to eat. For the hybrid recommender and sentiment analysis to both have high scores in their individual testing and evaluation.
Justification
This application will be both a time saver and a hassle free solution for users to pick the next restaurant they would like to go to, this will be achieved by using the machine learning recommendation system.
It will be an easy to access mobile app which is always one click away from suggesting your next restaurant.
## Programming languages
- Python
- Javascript
- HTML
- CSS
- SQL

## Programming Tools / Tech Stack
- Django - Used for the backend of the project
- React Native - Used for the frontend/UI of the project
- LightFM - Python library for recommendation engines
- PostgreSQL - Used for our database
- Google Maps API - Used for location and information
- Python NLTK, Stanza - Used for natural language processing

## Hardware
A mobile device for testing the application
## Learning Challenges 
Neither of us have any experience working with React Native and this will be a new learning experience developing a mobile application.
We have some past experience building a simple collaborative filtering recommendation system, but this new hybrid approach is a lot more complex and will require a lot of learning and research.
Neither of us have experience working with text analytics and this will be a new complex area to learn.
## Breakdown of Work

### Eoin Daly
- Backend using Django
- Recommender System using LightFM

### Thomas Hazekamp
- Front-end using React Native
- Text analytics and sentiment analysis