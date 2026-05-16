import pandas as pd
import numpy as np
import os

def create_dummy_data():
    """Generates small dummy CSV files for testing the pipeline."""
    if os.path.exists('xy_train.csv') and os.path.exists('x_test.csv'):
        print("Data files already exist. Skipping dummy data generation.")
        return

    # Sample data
    data = {
        'text': [
            "Breaking: Scientists discover a new planet made entirely of chocolate!",
            "The president signed a new bill into law today regarding healthcare.",
            "Click here to win a free iPhone! Totally not a scam.",
            "Local library to host a community reading event next Saturday.",
            "Aliens have landed in Central Park and are asking for directions.",
            "Economic indicators show a slight growth in the tech sector this quarter."
        ],
        'label': [1, 0, 1, 0, 1, 0] # 1 for Fake, 0 for Real
    }
    
    # Training data (6 samples repeated to have enough for split)
    train_df = pd.DataFrame(data)
    train_df = pd.concat([train_df] * 10, ignore_index=True)
    train_df.to_csv('xy_train.csv', index=False)
    
    # Test data
    test_data = {
        'text': [
            "New study finds that eating pizza makes you live forever.",
            "The stock market saw a minor dip in afternoon trading.",
            "Elvis spotted buying groceries in a small town in Nevada."
        ]
    }
    test_df = pd.DataFrame(test_data)
    test_df.to_csv('x_test.csv', index=False)
    
    print("Dummy data files 'xy_train.csv' and 'x_test.csv' created successfully.")

if __name__ == "__main__":
    create_dummy_data()
