import os
import pandas as pd
pd.options.display.max_colwidth = 400
pd.options.display.max_columns = 90

def getAPIkeys():
    ''' 
    input: none
    output: a list of the API keys in the current GitHub directory
    '''
    tokens = []
    # get API tokens
    with open('.env.development') as f:
        data = f.read()

    for line in data.split('\n'):
        head,sep,tail = line.partition(' = ')

        tokens.append(tail)

    return tokens

def getLatLon(row):
    import googlemaps
    gmaps = googlemaps.Client(key=mapsAPIkey)

    # add the various bits of the address together into a string to pass to the api
    addressStr = f"{row['BorrowerAddress']}, {row['BorrowerCity']}, {row['BorrowerState']} {row['BorrowerZip']}"
    print(addressStr)
    
    geocode_result = gmaps.geocode(addressStr)    

    # set default values to be returned if info is missing. Should be overwritten below.
    lat,lng,county = -999,-999,'Not Found'

    # if an address is malformed or missing, geocode will return an empty list
    # so if the list is > 0, we shoudl be able to extract the needed information
    if len(geocode_result) > 0:
        if 'address_components' in geocode_result[0]: # this should prevent crashes if the address component is missing
            address = geocode_result[0]['address_components']
            for item in address[::-1]:
                if 'administrative_area_level_2' in item['types']:
                    county = item["long_name"]
                    break

        if 'geometry' in geocode_result[0]: # this should prevent crashes if the geometry is missing
            geometry = geocode_result[0]['geometry']
            lat = geometry['location']['lat']
            lng = geometry['location']['lng']
    
    return lat,lng,county

####################################################
workDir = '/home/alp/Google Drive/Python/analysis/PPP_analysis/'

_,_, mapsAPIkey = getAPIkeys()

# this program will get a list of the unprocessed chunks
# of the data file, select the first one and process it (by adding geolocation data)
# save it back to the chunk file and then rename it.
#
# on the next run, the list of files won't include the one that has been processed already.
# thus, after multiple runs, it will process all the files.

import glob
workDir = '/home/alp/Google Drive/Python/analysis/PPP_analysis/'

file_names = sorted(glob.glob(f"{workDir}re_df_chunk*.json"))
fileN = file_names[0]

temp = pd.read_json(fileN)

print(f"processing file -- {fileN}")

temp[['lat','lng','county']] = temp.apply(getLatLon, axis = 'columns',result_type = 'expand')

temp.to_json(fileN,orient='records')

os.rename(fileN,f"{fileN}.done")

