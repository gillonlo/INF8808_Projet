import pandas as pd

def delete_first_three_letters(filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename,sep=";")
    print(df)

    # Remove the first three letters from the "Squad" column
    df['Team1'] = df['Team1'].apply(lambda x: x[:-3] if isinstance(x, str) and len(x) > 3 else x)

    # Write the modified DataFrame to a new CSV file
    new_filename = filename.replace('.csv', '_modified.csv')
    df.to_csv(new_filename, index=False, sep=';')
    print(f"Modified data has been saved to '{new_filename}'.")

# Example usage:
filename = 'projet_data_3_modified.csv'  # Replace 'data.csv' with the path to your CSV file
delete_first_three_letters(filename)