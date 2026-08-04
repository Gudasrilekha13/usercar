# 🚗 Car Price Prediction

A simple Machine Learning web application that predicts the selling price of a used car based on user inputs. The application is built using Python and Streamlit.

## Features

- Predict used car prices
- Simple and user-friendly interface
- Fast predictions using a trained ML model
- Built with Streamlit

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn

## Project Structure

```
Car-Price-Prediction/
│── app.py
│── model.pkl
│── car_data.csv
│── requirements.txt
│── README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Navigate to the project folder:
```bash
cd Car-Price-Prediction
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

## Input Features

- Car Name
- Year
- Present Price
- Kms Driven
- Fuel Type
- Seller Type
- Transmission
- Owner

## Output

The application predicts the estimated selling price of the car.

## License

This project is for educational purposes.
