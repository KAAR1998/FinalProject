# Final Project- Analysis and predictions on the price of a diamond 

Using a dataset of close to 54,000 diamonds' prices and attributes I conducted data analysis, visualisation and numerous predictions to find the optimal model to predict the price of a diamond based on their characteristics. 

Once the optimal model had been found, I applied it towards building an application that effectively predicts the price of your diamond if all the necessary attributes are are entered. The code for the building of the application can be found in the "app" folder within this repository. 

#  Data 

The dataset was taken from  Kaggle and can be found here- https://www.kaggle.com/datasets/shivam2503/diamonds. 

The dataset includes 11 columns and 53,940 rows

## Columns-
  - Carat Weight 
  - Cut- Quality of the Cut (Fair, Good, Very Good, Premium, Ideal)
  - Color- Color of Diamond from J (Worst) to D (Best)
  - Clarity- Clarity of Diamond (I1 (Worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (Best))
  - Depth- Total Depth Percentage = z / mean(x, y) = 2 * z / (x + y) 
  - Table- Width of top of diamond relative to widest point 
  - Price- USD ($)
  - x- Length (mm) 
  - y- Width (mm)
  - z- Depth (mm)
    
  
# Process- 

Cleaned and processed the raw data
EDA-
  - Visualized data- made distribution, line and scatter plots for the features
  - Found descriptive statistics, plotted box plots
Anomaly Detection
Clustering
Finding best hyperparameters
Making predictions and making models-
  - Random Forest Regressor - R2 Score: 0.98
  - Multi-Layer Perceptron (MLP) Regressor- R2 Score: 0.97
  - Gradient Boosting Regressor- R2 Score: 0.97
  - KNNeighbours Regressor- R2 Score: 0.96 
  - Decision Tree Regressor- R2 Score: 0.94
  - Feature Selection- R2 Score: 0.94
  - Linear Regression- R2 Score: 0.90
Regularization- L1 (Lasso) & L2 (Ridge)
Feature Engineering-
  - Feature Engineering Linear Regression Model- R2 Score: 1.00 
Hypothesis Testing- 
  - Tested and found that we should reject both Null Hypotheses listed below- 
    - Null Hypothesis (H0): Dimensions (length, width and depth) have no impact on a diamond's price
    - Null Hypothesis (H0): Carats, total depth percentage, and table (width of top of diamond relative to widest point) have no impact on a diamond's    price!




 

