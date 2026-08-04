import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
#load dataset
print("Loading dataset...")
df=pd.read_csv("price.csv")
print(df.head())

# checking missing values
print("missing values")
print(df.isnull().sum())
df=df.dropna()

 #encoding categorical columns
categorical_columns=[
  "Brand",
  "Fuel",
  "Transmission",
  "Owner"
 ]
label_encoders = {}
for column in categorical_columns:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    label_encoders[column] = encoder
print("\n categorical encoding completed")

#features and target
X=df.drop("Price",axis=1)
y=df["Price"]

#train test split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("\n training samples:",len(X_train))
print("testing samples:",len(X_test))

#train random forest model
model=RandomForestRegressor(n_estimators=100,random_state=42)
print("\n training model...")
model.fit(X_train,y_train)

#prediction
y_pred=model.predict(X_test)

#evaluation
mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
rmse= mse**0.5
r2=r2_score(y_test,y_pred)

print("\n=====================================")
print("model performance:")
print("=======================================")
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")

#save model
with open("car_price_model.pkl","wb") as file:
    pickle.dump(model,file)
print("\nModel saved : car_price_model.pkl")

#save label encoders
with open("label_encoders.pkl","wb") as file:
    pickle.dump(label_encoders,file)
print("Label encoders saved : label_encoders.pkl")

#feature importance
importance=pd.DataFrame({"Feature":X.columns,"Importance":model.feature_importances_})
importance=importance.sort_values(by="Importance",ascending=False)
print("\nFeature importance:")
print(importance)
print("\n=========================================")
print("Traaining completed successfully!")
print("=========================================")