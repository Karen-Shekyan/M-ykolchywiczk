#BE CAREFUL WITH REQUESTS! THEY SPEND REAL MONEY!!!!
#Code provided by Alanine for use of integrating the Astica Cognitive API into third party code
#https://github.com/alanine/astica-cognitive-api

import requests
import json
import base64
import os

def asticaAPI(endpoint, payload, timeout):
    response = requests.post(endpoint, data=payload, timeout=timeout, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'error', 'error': 'Failed to connect to the API.'}

with open("keys/key_api0", "r") as file:
    asticaAPI_key = file.read().strip()

asticaAPI_timeout = 35 # seconds  Using "gpt" or "gpt_detailed" will increase response time.

asticaAPI_endpoint = 'https://www.astica.org:9141/vision/describe'
asticaAPI_modelVersion = '2.0_full' # '1.0_full' or '2.0_full'

def gen_prompt(inputImg):
    #Input Method 2: base64 encoded string of a local image (slower)
    path_to_local_file = inputImg
    with open(path_to_local_file, 'rb') as file:
        image_data = file.read()
    image_extension = os.path.splitext(path_to_local_file)[1]
    #For now, let's make sure to prepend appropriately with: "data:image/extension_here;base64" 
    asticaAPI_input = f"data:image/{image_extension[1:]};base64,{base64.b64encode(image_data).decode('utf-8')}"


    '''
    DO NOT
    I REPEAT
    DO FUCKING NOT
    USE GPT OR GPT_DETAILED
    THEY WILL DRAIN THE ACCOUNT FASTER THAN I DO MY JUGS OF MILK
    DO NOT USE GPT
    I BEG YOU
    actually gonna use gpt~
    '''
    asticaAPI_visionParams = 'gpt' # comma separated options; leave blank for all; note "gpt" and "gpt_detailed" are slow.
    '''
        '1.0_full' supported options:
            description
            objects
            categories
            moderate
            tags
            brands
            color
            faces
            celebrities
            landmarks
            gpt new (Slow - be patient)
            gpt_detailed new (Much Slower)

        '2.0_full' supported options:
            description
            objects
            tags
            describe_all new
            text_read new
            gpt new (Slow - be patient)
            gpt_detailed new (Much Slower)
    '''

    # Define payload dictionary
    asticaAPI_payload = {
        'tkn': asticaAPI_key,
        'modelVersion': asticaAPI_modelVersion,
        'visionParams': asticaAPI_visionParams,
        'input': asticaAPI_input,
    }

    # Call API function and store result
    asticaAPI_result = asticaAPI(asticaAPI_endpoint, asticaAPI_payload, asticaAPI_timeout)

    ret = ""

    print('\nastica API Output:')
    print(json.dumps(asticaAPI_result, indent=4))
    print('=================')
    print('=================')

    # Handle asticaAPI response
    if 'status' in asticaAPI_result:
        # Output Error if exists
        if asticaAPI_result['status'] == 'error':
            print('Output:\n', asticaAPI_result['error'])
        # Output Success if exists
        if asticaAPI_result['status'] == 'success':
            if 'caption_GPTS' in asticaAPI_result and asticaAPI_result['caption_GPTS'] != '':
                print('=================')
                print('GPT Caption:', asticaAPI_result['caption_GPTS'])
            if 'caption' in asticaAPI_result and asticaAPI_result['caption']['text'] != '':
                print('=================')
                print('Caption:', asticaAPI_result['caption']['text'])
            if 'CaptionDetailed' in asticaAPI_result and asticaAPI_result['CaptionDetailed']['text'] != '':
                print('=================')
                print('CaptionDetailed:', asticaAPI_result['CaptionDetailed']['text'])
            if 'objects' in asticaAPI_result:
                print('=================')
                print('Objects:', asticaAPI_result['objects'])
        ret = asticaAPI_result['caption']['text']
    else:
        print('Invalid response')
    return ret

#gen_prompt("img/test0.jpg")
#gen_prompt("img/test1.jpg")
#gen_prompt("img/test2.jpg")
#gen_prompt("img/test3.jpg")
#gen_prompt("img/test4.png")
#gen_prompt("img/test5.png")
#gen_prompt("img/test6.png")
#gen_prompt("img/test7.png")
#gen_prompt("img/test8.png")
#gen_prompt("img/test9.jpg")
#gen_prompt("img/test10.jpg")
#gen_prompt("img/test11.jpg")
#gen_prompt("img/test12.jpg")
#gen_prompt("img/test13.jpg")

#4-8 are PNGS!!!!! 
#print(gen_prompt("img/test7.png"))