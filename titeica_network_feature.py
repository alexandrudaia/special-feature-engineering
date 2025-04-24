import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist

def create_titeica_feature(data):
    """
    Create a new feature using Țițeica network principles
    
    Args:
        data: DataFrame with 4 predictor columns
    Returns:
        numpy array with new feature based on Țițeica network properties
    """
    # Step 1: Normalize data for affine invariance
    normalized_data = (data - data.mean()) / data.std()
    points = normalized_data.values
    
    # Step 2: Calculate centro-affine invariants using pairwise distances
    distances = cdist(points, points)
    
    # Step 3: Generate Țițeica characteristic based on volume preservation
    titeica_feature = np.log1p(
        np.sum(distances, axis=1) * 
        np.exp(np.std(points, axis=1))
    )
    
    return titeica_feature

def process_dataset(file_path):
    """
    Process the dataset and add the Țițeica feature
    
    Args:
        file_path: Path to the CSV file with 4 predictors
    """
    try:
        # Load dataset
        df = pd.read_csv(file_path)
        
        # Verify column count
        if len(df.columns) != 4:
            raise ValueError(f"Expected 4 columns, but found {len(df.columns)}")
        
        # Create and add new feature
        df['titeica_feature'] = create_titeica_feature(df)
        
        # Save enhanced dataset
        output_path = 'train_with_titeica_feature.csv'
        df.to_csv(output_path, index=False)
        
        return df
        
    except Exception as e:
        print(f"Error processing dataset: {str(e)}")
        return None

# Example usage:
"""
# Process the dataset
enhanced_df = process_dataset('train.csv')

if enhanced_df is not None:
    print("\nFirst few rows with new feature:")
    print(enhanced_df.head())
    
    print("\nNew feature statistics:")
    print(enhanced_df['titeica_feature'].describe())
"""
