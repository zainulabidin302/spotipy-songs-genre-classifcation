import json
import os
import spotipy

token='BQDJ_nvHi37Pwc6AKnTtf_Bt2ETN4O9cmty2tSXPOQfljNa0or3qwBnVJpe85roxTbKjgf78pZbY8KUE-GG6vb6cFibQW-YpAJJI_q_8YraufUYLWxn76W8TYX0PXBdToubLULxGF8QS5-UWkFWCcstQ6AmHJsIjQFhMEq1sjSOmnbelAY3LW3eMmb_p4octPqwdLk79ZPfBxXNbY385e7xpbwakEd8lQDZvNGla7H8t0RZjZ8p2rFBMmEVOSNF7tlITGsYFEKFUCAi7W3M0T6PPAe8'
spotify = spotipy.Spotify(auth=token)

path = './DATA-dobara/'
path2 = './DATA-dobara-features/'
lis = os.listdir(path)

            
def write_to_file(name, data):
    with open(name, 'w') as f:
        json.dump(data, f)
for f in lis:
    with open(os.path.join(path, f)) as fr:
        a = json.load(fr)
    new_list = []
    for i in range(20):
        new_list.append(a['items'][i]['id'])
                                                                                
    r = spotify.audio_features(tracks=new_list)
    write_to_file(path2 + 'features-' + f, r)
