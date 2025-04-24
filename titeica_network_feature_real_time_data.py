import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist

def calculate_titeica_feature_for_new_row(existing_data, new_row):
    """
    Calculate Țițeica network feature for a new row of data
    
    Args:
        existing_data: DataFrame with existing data including 4 predictors
        new_row: Array-like object containing 4 new predictor values
    Returns:
        float: Țițeica feature value for the new row
    """
    # Convert new_row to correct format if needed
    if isinstance(new_row, pd.Series):
        new_row = new_row.values.reshape(1, -1)
    elif isinstance(new_row, list):
        new_row = np.array(new_row).reshape(1, -1)
    
    # Combine existing data with new row for proper normalization
    combined_data = pd.concat([
        existing_data,
        pd.DataFrame(new_row, columns=existing_data.columns)
    ])
    
    # Normalize all data including new row
    normalized_data = (combined_data - combined_data.mean()) / combined_data.std()
    
    # Get the normalized new row (last row)
    normalized_new_row = normalized_data.iloc[-1:].values
    
    # Calculate distances between new row and all points
    distances = cdist(normalized_new_row, normalized_data.values)
    
    # Calculate Țițeica feature for new row
    titeica_value = np.log1p(
        np.sum(distances) * 
        np.exp(np.std(normalized_new_row))
    )
    
    return titeica_value

# Example usage:
"""
# Load existing dataset
existing_df = pd.read_csv('train.csv')

# Example new row (replace with actual values)
new_row = [1.5, 2.3, 0.8, 1.1]

# Calculate Țițeica feature for new row
new_feature = calculate_titeica_feature_for_new_row(existing_df, new_row)

print(f"Țițeica feature value for new row: {new_feature}")
"""
