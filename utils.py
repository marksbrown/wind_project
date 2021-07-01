from datetime import datetime
import os

def get_data(raw_loc='data'):
    """
    Generator for raw data within :raw_loc:
    """
    paths = get_paths(raw_loc)
    for path in paths:
        print(path)
        for fn in paths[path]:
            print(fn)
            data = load_wind_data(path, fn)
            yield path, fn, data
            
def get_paths(root_dir='data'):
    """
    Fetch all subdirectories with files
    """
    paths = {}
    for root, dirs, files in os.walk('data'):
        if not files:
            continue
        full_path = os.path.join(root, *dirs)
        paths[full_path] = files
    return paths

def degrees(value, dtype=int):
    """
    >>> degrees("84")
    84
    >>> degrees("361")
    """
    value = value.split('.')[0]
    v = dtype(value)
    if 0 <= v <= 360:
        return v
    else:
        return None

def parse_24time(time):
    """
    
    >>> parse_24time("0010")
    datetime.time(0, 10)
    >>> parse_24time("1345")
    datetime.time(13, 45)
    """
    return datetime.strptime(time, '%H%M').time()

def load_wind_data(path, filename):
    """
    Loads :path/filename: into a dictionary with the key corresponding to time
    """
    loc = os.path.join(path, filename)
    parse_remaining = False
    wind_at_time = {}
    with open(loc) as f:
        for j, row in enumerate(f):
            if row.startswith('Code'):  # Beginning of dataset
                parse_remaining = True
                continue
            if parse_remaining:
                row = row.strip('\n')
                row = row.split()
                if len(row) == 3:
                    current_time = row[0]
                    wind_at_time[current_time] = []
                else:
                    wind_at_time[current_time].append(row)
    
    return wind_at_time

HEADER = {'QC' : int,
           'Height' : int,
           'WS' : float, 
           'WD' : degrees,
           'u' : float,
           'v' : float,
           'w' : float,
           'No. in Cns SW': int,
           'No. in Cns NW': int,
           'No. in Cns V': int,
           'SNR (db) SW': int, 
           'SNR (db) NW': int, 
           'SNR (db) V': int}


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)