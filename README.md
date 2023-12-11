# Predicting House Price In Australia Perth
Predict house prices in Australia with suburbs in the Perth area by comparing several model : KKN, SVM, Adaboost, Decision Tree and Random Forest model

# Objective
The main objective of this project is to develop a house price prediction model that can provide accurate estimates based on various features and factors that influence property prices. By using regression models such as linear regression, knn regressor, SVR (Support Vector Regressor), DecisionTree Regressor, RandomForest Regressor, AdaBoost Regressor, Linear Regression, SGD Regressor

# Fictional Background
In recent years, the property market has become one of the most dynamic sectors of the economy. Demand for homes continues to increase, while factors such as location, amenities and market conditions can significantly influence property prices. Therefore, the ability to accurately predict home prices is crucial for buyers, sellers and other stakeholders in the property market.

# Fictional Problem Statement
Real estate company AAA owns a number of properties in fast-growing markets. In an effort to improve sales efficiency and provide a better experience to customers, the company wanted to develop a home price prediction model. This model is expected to help real estate agents and buyers to get accurate and realistic price estimates.

# Result and Conclusion
**BUSINESS:**

- After checking the relationship with house prices in Perth Australia, it turns out that there are several factors that significantly influence the house price. Among others are area, land area, floor area, distance to business center, distance to nearest station.
    
- The distance from the house to the school does not affect the price of the house, but the distance from the house to the nearest station does affect the price. This can happen because to cover the distance from home to school, there is already a lot of public transportation or private vehicles owned by each person. So the distance from the house does not affect the price of the house, but rather the condition of the house that influences the price. So property companies don't need to worry about building houses in various areas. They must remain focused on beautifying and expanding the condition of the house to increase its price value. But you need to pay attention to the distance from your house to the nearest station.

- Houses in the Daiketh, Peppermint Grove, City Beach, Nedlands, Cottesloe suburbs have high average house prices. So a home property business that can be profitable for the company is to build home property in the area. This can be supported because the Daiketh, Peppermint Grove, City Beach, Nedlands, Cottesloe areas are close to shopping or business centers.

- An old house may have a higher price than a new house if the authenticity of the house is maintained, usually the target consumers are people who like old things.

**ABOUT MODEL (Advantages and Disadvantages of the Model)**

- Of all the models, the Random Forest Regressor model is used which has the highest R-squared score than the other models. Apart from that, the Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) values have smaller values than other models.

- The SVR model has a negative r2 value. Shows that it is not suitable to carry out regression especially on this data.

- The modeling created here can accurately predict prices based on the factors mentioned above. It can be said that the r2 value is 75% accurate. Even though the Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) values can be said to be high for measuring house prices.

- But if you look at the SHAP Values, this model can be said to be not good and not ready for deployment. This is because the model variables used as features do not have a big influence on house prices. It could even be said that if the value of the feature variables changes, the predicted change in house prices will only stagnate at 1 price.

- The modeling results can also be said to be overfit, they cannot be used for business purposes, let alone large scale.

**Poor Performance** : The model has unsatisfactory performance in explaining the effect of feature selection on house prices.

**Must Improve**: Further evaluation of the model is needed to identify factors influencing its poor performance.

**Model Adjustment**: Adjustments to the model are required, such as adding more relevant features (because when performing VIF many variables are discarded because they have high multicollinearity), parameter tuning, or using a more complex model.

**Steps That Can Be Taken**:

- Factor Analysis: Identify factors that have a significant impact on price predictions and ensure the model accounts for them correctly.

- Feature Development: Consider adding additional features that might provide more information regarding home prices.

- Hyperparameter Tuning: Tune the model hyperparameters to increase the prediction r-squared with small Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) values.

- Use of Other Models: Consider using a more complex regression model or combining several models (ensemble) to improve performance
