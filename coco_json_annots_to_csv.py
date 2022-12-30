import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np
import cv2
import json

def json_to_csv(path, result_write_file):# all_images):

    all_labels_ids = []
    all_labels_names = []
    object_ids = []
    names = []
    index1 = 0
    file_names = []
    bboxes = []
    xmin, ymin, xmax, ymax = [], [], [], []

    with open(path, 'r') as f:
        data = json.load(f)

    for i, obj1 in enumerate(data['images']):

                for t, obj2 in enumerate(data['annotations']):
                    #print('obj2', obj2)
                    #print('obj1', obj1)
                    if obj1['id']==obj2['image_id']:
                        file_names.append(obj1['file_name'])
                        file_n = str(obj1['file_name'])
                        file_n = file_n.split('scene 1/')[-1]

                        names.append(file_n)
                        label_id = obj2['category_id']
                        #label_name = obj0['name']
                        all_labels_ids.append(label_id)

                        index1 += 1
                        #print('index1', index1)
                        bbox = obj2['bbox']
                        bboxes.append(bbox)

                        xmin.append(bbox[0])
                        ymin.append(bbox[1])
                        xmax.append(bbox[0] + bbox[2])
                        ymax.append(bbox[1] + bbox[3])

    xmin = pd.DataFrame(xmin)
    ymin = pd.DataFrame(ymin)
    xmax = pd.DataFrame(xmax)
    ymax = pd.DataFrame(ymax)
    names = pd.DataFrame(names)
    all_labels_ids = pd.DataFrame(all_labels_ids)
    all_labels_names = pd.DataFrame(all_labels_names)
    result = pd.concat((names, all_labels_ids,  xmin, ymin, xmax, ymax), axis=1)

    result.columns = ['filename', 'label_id', 'xmin', 'ymin', 'xmax', 'ymax']
    result.to_csv(result_write_file)
    print('done converting json to csv')
    return result


def run_json_to_csv():

        #all_images = os.listdir('results/eyal01/eyal01_all')

        # Path to read data
        path_read = 'results/evan02/instances_default.json'

        # Path to write file
        path_write = 'results/evan02/annotations.csv'

        csv_file = json_to_csv(path_read, path_write)

        print('Successfully converted json to csv.')
        return csv_file

run_json_to_csv()