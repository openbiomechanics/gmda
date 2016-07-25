"""TO BE EDITED.

TO BE EDITED.

Available defs:
- f: TO BE EDITED.
"""
import pandas as pd
import os


def main():
    # Load data
    print("Started!")
    data_dir = os.path.abspath('../data/original')
    file = os.path.join(data_dir, 'details.csv')
    data = pd.read_csv(file)

    # Clean up column names
    column_names = data.columns
    column_names = [s.replace('(1-50)', '') for s in column_names]
    column_names = [s.replace('/', '_per_') for s in column_names]
    column_names = [s.replace('-', '_') for s in column_names]
    column_names = [s.lower() for s in column_names]
    data.columns = column_names

    # Impute missing values
    data.loc[11:14, 'group'] = 'Young-Middle'
    data.loc[34:38, 'group'] = 'Middle-Old'

    # Write out data
    data.to_csv('../data/prepped/details.csv', index=False)

    print("Finished!")


if __name__ == '__main__':
    main()
