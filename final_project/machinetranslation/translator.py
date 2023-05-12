'''
Author: Robxxt
Email: rdragan@student.42heilbronn.de
Date: 12-05-2023
Description:    This module calls the IBM Watson Translation API
                Supports english to franch and franch to english translations.
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['WATSON_TRANSLATION_API_KEY']
url = os.environ['WATSON_TRANSLATION_URL']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    Translates the given text from english to franch.
    '''
    if len(english_text) == 0:
        return ''
    french_text = language_translator.translate(
    text = english_text,
    model_id = 'en-fr').get_result()
    return french_text['translations'][0]['translation']


def french_to_english(french_text):
    '''
    Translates the given text from franch to enlgish.
    '''
    if len(french_text) == 0:
        return ''
    english_text = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result()
    return english_text['translations'][0]['translation']
