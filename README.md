# Finding Lung Tidal Volume

Our first task was to find a dataset to satisfy the following conditions-
1. It should have "factors such as Age, Gender, Height, and some specific symptoms"
2. It should be a public dataset and be a collection real data

### Finding the dataset

Finding the dataset was the hardest part of this task.
After searching for a while i got to know about many public sources for the datasets such as The Global Health Observation data repository, Data.gov, healthdata.gov, Earth data by nasa and finally the lifesaver The Google's dataset search engine. (https://datasetsearch.research.google.com/)
On google's dataset search engine I found this dataset https://huggingface.co/datasets/ericyxy98/pulmonary-disease-airway-lung-function-dataset/viewer/default/csa

### Preprocessing the data
This dataset had categorical columns for Race and Disease.
Converting those columns to a proper format interpretable by our model was done by one hot encoding these according to keras documentation
After cleaning and preprocessing the dataset, it was time to traing out model


### Training the model

Now came the training of the models. For this i trained 3 models 
1. A linear regression model with all parameters 
    This was the most simple approach and it gave an mae of about 65 
2. A neural network with all parameters  
    In this model l2 regularisation was used to prevent overfitting.
    This model has 2 hidden layers of size 6 and 8 respectively.
    It achieved an mae of 55
4. A neural network with selected parameters
    this model also uses the same architecture but with the selected features
    It achieved an mae of 60.

After training the models. it can be seen that model2 i.e the neurl net trained on all the params works the best and hass the least training and validation loss.
After all the models have been saved

### Running the model
To run the model, simply clone the repository and run the run.py file

### Model in action
![img](https://github.com/anirudh802/Lung_Capacity_estimation/blob/main/Screenshot%20from%202024-05-23%2018-59-32.png)
