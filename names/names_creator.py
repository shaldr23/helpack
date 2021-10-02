import os
import json
import pandas as pd
import random


def __parse_file(file_path):
    """
    Supporting function
    """
    objects = []
    with open(file_path, encoding='utf8') as f:
        for line in f:
            obj = json.loads(line)
            obj = {key: val for key, val in obj.items()
                   if key in ['text', 'gender', 'num']}
            objects.append(obj)
    frame = pd.DataFrame(objects)
    return frame


def __choose(frame, gender, use_proba=True):
    """
    Supporting funtion
    """
    if gender == 'm':
        other_gender = 'f'
    if gender == 'f':
        other_gender = 'm'
    frame = frame[frame['gender'] != other_gender]
    names = list(frame['text'])
    if use_proba:
        probas = list(frame['num'])
        chosen = random.choices(names, k=1, weights=probas)[0]
    else:
        chosen = random.choice(names)
    return chosen


def create_name_set(gender: str, use_proba=True) -> dict:
    """
    use_proba: name, surname, midname are chosen with
    probability according to their occurrence in Russia,
    otherwise - choose random ones.
    gender: 'm' or 'f'
    """
    name = __choose(names_frame, gender=gender, use_proba=use_proba)
    surname = __choose(surnames_frame, gender=gender, use_proba=use_proba)
    midname = __choose(midnames_frame, gender=gender, use_proba=use_proba)
    name_set = {'name': name,
                'surname': surname,
                'midname': midname}
    return name_set


exec_dir = os.path.dirname(__file__)
db_loc = os.path.join(exec_dir, 'data/source')
names_file = os.path.join(db_loc, 'names_table.jsonl')
surnames_file = os.path.join(db_loc, 'surnames_table.jsonl')
midnames_file = os.path.join(db_loc, 'midnames_table.jsonl')

names_frame = __parse_file(names_file)
surnames_frame = __parse_file(surnames_file)
midnames_frame = __parse_file(midnames_file)
