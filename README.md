# Finding Lung Tidal Volume

Our first task was to find a dataset to satisfy the following conditions-
1. It should have "factors such as Age, Gender, Height, and some specific symptoms"
2. It should be a public dataset and be a collection real data

### Finding the dataset

Finding the dataset was the hardest part of this task.
After searching for a while i got to know about many public sources for the datasets such as The Global Health Observation data repository, Data.gov, healthdata.gov, Earth data by nasa and finally the lifesaver The Google's dataset search engine. (https://datasetsearch.research.google.com/)
On google's dataset search engine I found this dataset https://huggingface.co/datasets/ericyxy98/pulmonary-disease-airway-lung-function-dataset/viewer/default/csa
After cleaning and preprocessing the dataset, it was time to traing out model


### Training the model

Now came the training of the models. For this i trained 3 models 
1. A linear regression model with all parameters
2. A neural network with all parameters
3. A neural network with selected parameters

After training the models. it can be seen that model2 i.e the neurl net trained on all the params works the best and hass the least training and validation loss.
After all the models have been saved
