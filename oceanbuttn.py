# -*- coding: utf-8 -*-
from settings import *

import requests
import argparse


parser = argparse.ArgumentParser(description='Power button for DigitalOcean droplets')
parser.add_argument('--droplet', default=DROPLET_ID, help='a droplet to push the button on')
parser.add_argument('--token', default=AUTH_TOKEN, help='auth token to access DigitalOcean API')
parser.add_argument('--action', choices=['power_on', 'shutdown'], default='power_on', help='action to be performed on the droplet (power_on is default)')
args = parser.parse_args()

headers = {'Authorization': ('Bearer %s' % args.token)}
droplet_acton_url = 'https://api.digitalocean.com/v2/droplets/%s/actions' % args.droplet
payload = {'type': args.action}

r = requests.post(droplet_acton_url, data=payload, headers=headers)
print(r.text)

