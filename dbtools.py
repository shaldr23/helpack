import pandas as pd
from IPython.display import display


def frame_response(cursor: 'cursor with all data',
                   only_display: True) -> pd.DataFrame:
    """
    Helps to make beautiful table from response:
    pandas.DataFrame table
    Usage: run the following:
    --------------------------------------------
    conn = sqlite3.connect("<DATABASE>")
    cursor = conn.cursor()
    cursor.execute("<QUERY>")
    print(frame_response(cursor))
    """
    result = cursor.fetchall()
    cols = [d[0] for d in cursor.description]
    result = pd.DataFrame(result, columns=cols)
    if only_display:
        display(result)
    else:
        return result
