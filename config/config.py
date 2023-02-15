# config/config.py
"""This module reads the config file & saves it to dict: config_dict."""
import yaml


with open('config/config.yaml', 'r') as file:
    config_dict = yaml.safe_load(file)
    file.close()
