import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import regex as re
import lxml
from lxml.html.soupparser import fromstring
import prettify
import numbers
import htmltext
from pprint import pprint as pp
import json
import random

user_agents_list = [
    # 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

import requests

headers = {
    'authority': 'www.realtor.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.realtor.com',
    'referer': 'https://www.realtor.com/realestateandhomes-search/40391',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': random.choice(user_agents_list),
}

params = {
    'client_id': 'rdc-x',
    'schema': 'vesta',
}

json_data = {
    'query': '\n\nquery ConsumerSearchMainQuery($query: HomeSearchCriteria!, $limit: Int, $offset: Int, $sort: [SearchAPISort], $sort_type: SearchSortType, $client_data: JSON, $bucket: SearchAPIBucket)\n{\n  home_search: home_search(query: $query,\n    sort: $sort,\n    limit: $limit,\n    offset: $offset,\n    sort_type: $sort_type,\n    client_data: $client_data,\n    bucket: $bucket,\n  ){\n    count\n    total\n    results {\n      property_id\n      list_price\n      primary\n      primary_photo (https: true){\n        href\n      }\n      source {\n        id\n        agents{\n          office_name\n        }\n        type\n        spec_id\n        plan_id\n      }\n      community {\n        property_id\n        description {\n          name\n        }\n        advertisers{\n          office{\n            hours\n            phones {\n              type\n              number\n            }\n          }\n          builder {\n            fulfillment_id\n          }\n        }\n      }\n      products {\n        brand_name\n        products\n      }\n      listing_id\n      matterport\n      virtual_tours{\n        href\n        type\n      }\n      status\n      permalink\n      price_reduced_amount\n      other_listings{rdc {\n      listing_id\n      status\n      listing_key\n      primary\n    }}\n      description{\n        beds\n        baths\n        baths_full\n        baths_half\n        baths_1qtr\n        baths_3qtr\n        garage\n        stories\n        type\n        sub_type\n        lot_sqft\n        sqft\n        year_built\n        sold_price\n        sold_date\n        name\n      }\n      location{\n        street_view_url\n        address{\n          line\n          postal_code\n          state\n          state_code\n          city\n          coordinate {\n            lat\n            lon\n          }\n        }\n        county {\n          name\n          fips_code\n        }\n      }\n      tax_record {\n        public_record_id\n      }\n      lead_attributes {\n        show_contact_an_agent\n        opcity_lead_attributes {\n          cashback_enabled\n          flip_the_market_enabled\n        }\n        lead_type\n        ready_connect_mortgage {\n          show_contact_a_lender\n          show_veterans_united\n        }\n      }\n      open_houses {\n        start_date\n        end_date\n        description\n        methods\n        time_zone\n        dst\n      }\n      flags{\n        is_coming_soon\n        is_pending\n        is_foreclosure\n        is_contingent\n        is_new_construction\n        is_new_listing (days: 14)\n        is_price_reduced (days: 30)\n        is_plan\n        is_subdivision\n      }\n      list_date\n      last_update_date\n      coming_soon_date\n      photos(limit: 2, https: true){\n        href\n      }\n      tags\n      branding {\n        type\n        photo\n        name\n      }\n    }\n  }\n}',
    'variables': {
        'query': {
            'type': [
                'single_family',
            ],
            'status': [
                'for_sale',
                'ready_to_build',
            ],
            'unique': True,
            'search_location': {
                'location': '40391, Winchester, KY',
            },
        },
        'client_data': {
            'device_data': {
                'device_type': 'web',
            },
            'user_data': {
                'last_view_timestamp': -1,
            },
        },
        'limit': 42,
        'offset': 0,
        'zohoQuery': {
            'silo': 'search_result_page',
            'location': '40391, Winchester, KY',
            'property_status': 'for_sale',
            'filters': {
                'prop_type': [
                    'single_family',
                ],
            },
        },
        'sort_type': 'relevant',
        'geoSupportedSlug': '40391',
        'by_prop_type': [
            'single_family',
            'home',
        ],
    },
    'operationName': 'ConsumerSearchMainQuery',
    'callfrom': 'SRP',
    'nrQueryType': 'MAIN_SRP',
    'visitor_id': 'ca446ca2-6b4e-4cd3-a1fd-a2c4dd4a7128',
    'isClient': True,
    'seoPayload': {
        'asPath': '/realestateandhomes-search/40391/type-single-family-home',
        'pageType': {
            'silo': 'search_result_page',
            'status': 'for_sale',
        },
        'county_needed_for_uniq': False,
    },
}

# response = requests.get('https://www.realtor.com/realestateandhomes-search/40391', headers=headers, params=params)

# print(response)

with requests.Session() as session:
    zipcode = '40391'
    page = 1
    end_page = 3


    url = ''
    url_list = []

    while page <= end_page:
        url = 'https://www.realtor.com/realestateandhomes-search/' + (zipcode) + '/type-single-family-home/pg-' + str(page)
        url_list.append(url)
        page += 1


    request = ''
    request_list = []

    for url in url_list:
        request = session.get(url, headers=headers, params=params)
        request_list.append(request)
        
soup = ''
soup_list = []

for request in request_list:
    soup = BeautifulSoup(request.content, "lxml")
    soup_list.append(soup)


df_list = []

for soup in soup_list:
    df = pd.DataFrame()
    for i in soup:
        address = soup.find_all('span', 'pc-address')
        # price = soup.find_all('span', 'pc-price')
        # beds = soup.find_all('li', 'pc-meta-beds')
        # baths = soup.find_all('li', 'pc-meta-baths')
        # sq_feet = soup.find_all('li', "pc-meta-sqft")



        df['address'] = address
        # df['price'] = price
        # df['beds'] = beds
        # df['baths'] = baths
        # df['sq_feet'] = sq_feet

    urls = []

    df_list.append(df)

pp(df_list)    

#concatenates all pages of data onto eachother so that all data cmes back correctly
# df = pd.concat(df_list).reset_index().drop(columns='index')


# #sets values as a string which they must be for them to be converted into a json object
# df['address'] = df['address'].astype('str')
# df['price'] = df['price'].astype('str')
# df['beds'] = df['beds'].astype('str')


# # this just replaces everything in the string that contains things that are not the values i want with an empty string and sets those values equal to an altered string
# df.loc[:, 'address'] = df.loc[:, 'address'].replace('</span>', '', regex=True)
# df.loc[:, 'address'] = df.loc[:, 'address'].replace('<span class=\\"collapsedAddress primaryLine\\" data-rf-test-id=\\"abp-streetLine\\">', '', regex=True)
# df.loc[:, 'price'] = df.loc[:, 'price'].replace('</span>', '', regex=True)
# df.loc[:, 'price'] = df.loc[:, 'price'].replace('<span class=\\"homecardV2Price\\" data-rf-test-name=\\"homecard-price\\">', '', regex=True)
# df.loc[:, 'beds'] = df.loc[:, 'beds'].replace('<div class=\\"HomeStatsV2 font-size-small\\"><div class=\\"stats\\">', '', regex=True)
# df.loc[:, 'beds'] = df.loc[:, 'beds'].replace('</div><div class=\\"stats\\">', ' ', regex=True)
# df.loc[:, 'beds'] = df.loc[:, 'beds'].replace('</div><div class=\\"stats\\">', ' ', regex=True)
# df.loc[:, 'beds'] = df.loc[:, 'beds'].replace(' Sq. Ft.</div></div>', '', regex=True)
# df.loc[:, 'beds'] = df.loc[:, 'beds'].replace(' Beds', '', regex=True)
# df.loc[:, 'beds'] = df.loc[:, 'beds'].replace(' Baths', '', regex=True)
# df.loc[:, 'beds'] = df.loc[:, 'beds'].replace(' Bed', '', regex=True)
# df.loc[:, 'beds'] = df.loc[:, 'beds'].replace(' Bath', '', regex=True)



# #selects everything to be returned only that contains the original zipcode
# df = df[df['address'].str.contains(zipcode)]

# # df[['beds', 'baths', 'sq_feet']] = df.beds.str.split(expand=True)

# #simply prints a json object of the dataframe using json loads and dumps to stringify the object and turn it into json
# # print(json.dumps(json.loads(df.to_json(orient='index')), indent=2))
# print(df)