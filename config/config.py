import yaml


with open('config/config.yaml', 'r') as file:
    config_dict = yaml.safe_load(file)
    file.close()
