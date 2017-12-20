import os
import numpy as np
import json
ls = os.listdir('./DATA-dobara-features')
def extract_features(a, label):

    selected_features = ['danceability', 'duration_ms','tempo', 'liveness', 'acousticness', 'loudness', 'energy', 'speechiness', 'valence'] 
    features_list = []    
    for item in a:
        row = []
        for selected_feature in selected_features:
            row.append(item[selected_feature])
        row.append(label)
        features_list.append(row)
    return features_list
new_array = []
for fname in ls:

    with open('DATA-dobara-features/'+fname) as js:
        a = json.load(js)
        if fname.startswith('features-DATAFILE.Pop') == True:

            
           output =  extract_features(a, 0)
        else:

            output = extract_features(a, 1)
        new_array.extend(output) 
res = np.array(new_array)

np.save('final-dobara.npy', res)
