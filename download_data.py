import spotipy
import json
import spotipy.util as util
import os

def write_to_file(name, data):
    with open('DATA-dobara/' + name , 'w') as outfile:
        json.dump(data, outfile)

            # os.environ['SPOTIPY_CLIENT_ID'] = "8b1ead84f3f645fc9482ebcd0063907b"
            # os.environ['SPOTIPY_CLIENT_SECRET'] = "910bcc984485440c89fe24531c567c97"
            # os.environ['SPOTIPY_REDIRECT_URI'] = "http://appslab.io"


# token = util.prompt_for_user_token('Anas_CH', '')        
token='BQDJ_nvHi37Pwc6AKnTtf_Bt2ETN4O9cmty2tSXPOQfljNa0or3qwBnVJpe85roxTbKjgf78pZbY8KUE-GG6vb6cFibQW-YpAJJI_q_8YraufUYLWxn76W8TYX0PXBdToubLULxGF8QS5-UWkFWCcstQ6AmHJsIjQFhMEq1sjSOmnbelAY3LW3eMmb_p4octPqwdLk79ZPfBxXNbY385e7xpbwakEd8lQDZvNGla7H8t0RZjZ8p2rFBMmEVOSNF7tlITGsYFEKFUCAi7W3M0T6PPAe8'
sp = spotipy.Spotify(auth=token)




for genre in ['Pop', 'Rap']:
    print(genre)
    try:
        results = sp.search(q='genre:'+ genre +'' ,  limit=20,type = 'track')
    except Exception as e:
        print(e)
        continue
    print(results)
    i = 0
    while results:
        write_to_file('DATAFILE.' +  genre + '.' + str(i) + '.json' ,results['tracks'])
        print(results['tracks']['next'])
        #break
        #print(results['tracks'])
        if results['tracks']['next']:
            results = sp.next(results['tracks'])
        else:
            results = None

        if i == 100:
            break
        i += 1
