# config/config.py
"""This module reads the config file & saves it to dict: config_dict."""
import os
import yaml
from config.utils import get_project_root


# get root path
root = get_project_root()

# the relative file path
path_db = 'become_qa_auto.db'
path_driver = 'chromedriver_linux64/chromedriver'

# add the relative path to the database file from there
db_path = os.path.join(root, path_db)
driver_path = os.path.join(root, path_driver)

# Update path to DB if project root has been changed
with open("config/config.yaml", "r") as yamlfile:
    config_dict = yaml.load(yamlfile, Loader=yaml.FullLoader)
    config_dict["DB"]["path"] = db_path
    config_dict["UI"]["driver_path"] = driver_path


with open("config/config.yaml", "w") as yamlfile:
    data = yaml.dump(config_dict, yamlfile)
