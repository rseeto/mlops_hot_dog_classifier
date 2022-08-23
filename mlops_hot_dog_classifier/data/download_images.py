import config_api
import requests
import os
import time
import re


def get_image_search_info(
    page_num, category, api_key = config_api.SERPAPI_API_KEY    
):
    params = {
        "engine": "google",
        "q": category,
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en",
        "num": "100",
        "tbm": "isch",
        "ijn": page_num,
        "api_key": api_key
    }

    while True:
        image_search_info = requests.get(
            'https://serpapi.com/search.json?', params = params
        )
        if image_search_info.status_code == 200:
            break
        else:
            time.sleep(60)

    return image_search_info.json()


def get_images(image_search_info, sub_raw_folder = ''):
    
    category = image_search_info['search_parameters']['q']
    page_num = image_search_info['search_parameters']['ijn']
    images_results = image_search_info['images_results']

    for i in range(len(images_results)):
        thumbnail_url = images_results[i]['thumbnail']
        thumbnail = requests.get(thumbnail_url)
        if thumbnail.status_code == 200:
            file_ext = re.sub(
                'image/', '.', thumbnail.headers.get('content-type')
            )
            save_file = (
                os.path.abspath(os.path.join(__file__ ,"../../../data/raw"))
                + sub_raw_folder + '/' 
                + category + '/'
                + category 
                + '_pg_' + str(page_num) 
                + '_pos_' + str(i) 
                + file_ext
            )                  
            with open(save_file, 'wb') as f:
                f.write(thumbnail.content)


# def main():
    
#     for page_num in range(10):
#         for category in ['hot dog', 'taco', 'sandwich', 'food']:
#             image_search_info = get_image_search_info(page_num, category)
#             get_images(image_search_info)
    

# def main():
#     TOTAL_PAGES = 1
#     RAW_FOLDER = os.path.abspath(os.path.join(__file__ ,"../../../data/raw")) 
    
#     for page_num in range(TOTAL_PAGES):
#         for category in ['hot dog', 'taco', 'sandwich', 'food']:
#             save_folder = RAW_FOLDER + '/' + category + '/'

#             page_num = 0
#             category = 'taco'

#             params = {
#                 "engine": "google",
#                 "q": category,
#                 "google_domain": "google.com",
#                 "gl": "us",
#                 "hl": "en",
#                 "num": "100",
#                 "tbm": "isch",
#                 "ijn": page_num,
#                 "api_key": config_api.SERPAPI_API_KEY
#             }

#             while True:
#                 r = requests.get(
#                     'https://serpapi.com/search.json?', params = params
#                 )
#                 if r.status_code == 200:
#                     break
#                 else:
#                     time.sleep(60)

#             images_results = r.json()['images_results']

#             for i in range(len(images_results)):
#                 thumbnail_url = images_results[i]['thumbnail']
#                 thumbnail = requests.get(thumbnail_url)
#                 if thumbnail.status_code == 200:
#                     file_ext = re.sub(
#                         'image/', '.', thumbnail.headers.get('content-type')
#                     )
#                     save_file = (
#                         save_folder 
#                         + category 
#                         + '_pg_' + str(page_num) 
#                         + '_pos_' + str(i) 
#                         + file_ext
#                     )                  
#                     with open(save_file, 'wb') as f:
#                         f.write(thumbnail.content)

# # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process



# https://towardsdatascience.com/image-classification-transfer-learning-and-fine-tuning-using-tensorflow-a791baf9dbf3
# https://www.tensorflow.org/datasets/catalog/food101
# https://github.com/alpapado/food-101/blob/master/data/meta/classes.txt
