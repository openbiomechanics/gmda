"""TO BE EDITED.

TO BE EDITED.

Available defs:
- f: TO BE EDITED.
"""
from io import StringIO
import pandas as pd
import os
import tarfile


def main():
    # Load data
    print("Started!")
    data_dir = os.path.abspath('../data/original')
    zipfile_name = 'gait-maturation-db.tar.gz'
    file = os.path.join(data_dir, zipfile_name)
    data = pd.DataFrame()

    # Write out data
    data.to_csv('', index=False)
    print("Finished!")


if __name__ == '__main__':
    main()
