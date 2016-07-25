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
    column_names = ['time', 'stride_interval']
    with tarfile.open(file) as tar:
        for member in tar.getmembers():
            if '.txt' in member.name:
                f = tar.extractfile(member)
                x = f.read().decode('utf-8')
                content = StringIO(x)
                df = pd.read_csv(content, sep="\t", names=column_names)
                name = member.name
                name = name.replace('data/', '')
                name = name.replace('.txt', '')
                import re
                x = re.match('([0-9]+)-([0-9]+)', name)
                df['subject_id'] = int(x.groups()[0])
                data = pd.concat([data, df], axis=0)

    # Clean up data.frame
    data = data[['subject_id'] + column_names]
    data = data.sort_values(['subject_id', 'time'])

    # Write out data
    data.to_csv('../data/prepped/intervals.csv', index=False)
    print("Finished!")


if __name__ == '__main__':
    main()
