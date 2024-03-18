import json
import os
import pickle
from json import JSONDecodeError
from pprint import pprint


def read_json(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data


def read_all_json_files(folder_path):
    json_list = []
    for root, directories, files in os.walk(folder_path):
        for file in files:
            file_path = root + "/" + file
            #TODO catch exception for not a json file
            try:
                json_object = read_json(file_path)
                json_list.append(json_object)
            except JSONDecodeError:
                # Not a valid json file
                pass
        break # End the walk and don't go into subfolders
    return json_list

def write_pickle(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def load_pickle(file_path):
    with open(file_path, 'rb') as file:
        json_object = pickle.load(file)
        return json_object

if __name__=="__main__":
    #pprint(read_json("data/super_smash_bros/link.json"))
    #pprint(read_all_json_files("data/super_smash_bros/"))

    json_object = read_json("data/super_smash_bros/link.json")
    pickle_file = "data/super_smash_bros/link.pickle"
    write_pickle(json_object, pickle_file)

    pprint(load_pickle(pickle_file))