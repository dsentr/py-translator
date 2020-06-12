import requests, sys
import json
import argparse


def translate_text(source, target, input_):
  url = "https://translation.googleapis.com/language/translate/v2"
  # make apikey global??
  apikey = "YOUR API KEY HERE"

  querystring = {
    "source":source,
    "target":target,
    "q":input_,
    "key":apikey,
    }

  response = requests.request("GET", url, params=querystring)
  print(type(response))
  data1 = response.json() #converts response to dictionary data type (deserialize)
  print(type(data1))
  print(data1["data"]["translations"][0]["translatedText"])

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Translates words or sentences to another language.')

  parser.add_argument('--translate', metavar='Input', type=str, nargs='+',
                    help='Input the word or words to be tranlsated')

  parser.add_argument('--source', metavar='source', type=str, nargs='+',
                    help='Input the source language using ISO code')

  parser.add_argument('--target', metavar='target', type=str, nargs='+',
                    help='Input the target language using ISO code')

  args = parser.parse_args()

  translate_text(args.source, args.target, args.translate)
