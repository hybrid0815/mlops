import yaml

filepath = 'yaml_example.yaml'

with open(filepath) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

print(data['version'])
print(data['price'])
print(data['category'])
print(data['course_dev'])
print(data['dev_details'])
print(data['short_description'])