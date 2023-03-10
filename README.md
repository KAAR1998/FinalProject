# Ironhack Final Project- Analysis and Predictions on the price of a diamond 

Using a dataset of close to 54,000 diamonds' prices and attributes I conducted data analysis, visualisation and numerous predictions to find the optimal model to predict the price of a diamond based on their characteristics. 

Once the optimal model had been found, I applied it towards building an application that effectively predicts the price of your diamond if all the necessary attributes are are entered. 

#  Data 

The dataset was taken from  Kaggle and can be found here- https://www.kaggle.com/datasets/shivam2503/diamonds. (Author: Shivam Agrawal) 

The dataset includes 11 columns and 53,940 rows

## Columns-
  - Carat Weight 
  - Cut- Quality of the Cut (Ideal (Best), Premium, Very Good, Good, Fair (Worst))
  - Color- Color of Diamond from (D (Best), E, F, G, H, I J (Worst)) 
  - Clarity- Clarity of Diamond (IF (Best), VVS1, VVS2, VS1, VS2, SI1, SI2, I1 (Worst)) 
  - Depth- Total Depth Percentage (TDP = z / mean(x, y) = 2 * z / (x + y))
  - Table- Width of top of diamond relative to widest point  
  - Price- USD ($)
  - x- Length (mm) 
  - y- Width (mm)
  - z- Depth (mm)
    
  
# Process- 

- Cleaned and processed the raw data
- EDA-
  - Visualized data- made distribution, line and scatter plots for the features
  - Found descriptive statistics, plotted box plots
- Anomaly Detection
- Clustering
- Finding best hyperparameters
- Making predictions and making models-
  - Random Forest Regressor - R2 Score: 0.98
  - Multi-Layer Perceptron (MLP) Regressor- R2 Score: 0.97
  - Gradient Boosting Regressor- R2 Score: 0.97
  - KNNeighbours Regressor- R2 Score: 0.96 
  - Decision Tree Regressor- R2 Score: 0.94
  - Feature Selection- R2 Score: 0.94
  - Linear Regression- R2 Score: 0.90
- Regularization- L1 (Lasso) & L2 (Ridge)
- Feature Engineering-
  - Feature Engineering Linear Regression Model- R2 Score: 1.00 
- Hypothesis Testing- 
  - Tested and found that we should reject both Null Hypotheses listed below- 
   - Null Hypothesis (H0): Dimensions (length, width and depth) have no impact on a diamond's price
   - Null Hypothesis (H0): Carats, total depth percentage, and table (width of top of diamond relative to widest point) have no impact on a diamond's    price

# Contents of this Repository- 

- Notebooks-
   - Jupyter Notebook of the code used to apply all of the steps outlined above in the "Process" section 
- Data- 
   - A copy of the original data in the "Raw" folder 
   - A copy of the cleaned data in the "Clean" folder 
 - Models and Scalers- 
    - Pickle files of the predictive models and pre-processing steps (e.g. scaling, transforming) used to create the models 
