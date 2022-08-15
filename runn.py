from operator import index
from tkinter.tix import Tree
import yaml
import json
from cerberus import Validator


def load_doc():
    with open('./rule_file.yaml', 'r') as stream:
        try:
            return yaml.load(stream,Loader=yaml.Loader)
        except yaml.YAMLError as exception:
            raise exception

with open('./all_rules_file.yaml', 'r') as file:
    configuration = yaml.safe_load(file)

with open('config.json', 'w') as json_file:
    json.dump(configuration, json_file)
    
output = json.dumps(json.load(open('config.json')), indent=2)
a = json.loads(output)
# print(a)
# print(len(a["alert_params"]))
# print(type(a["alert_params"]))

error_flag = False
error_rule = [];

for key, value in a["alert_params"].items():
    # print("Type :: ",value["type"])
    if((value["type"])=="frequency"):
        # print(value)
        with open(r'rule_file.yaml', 'w') as file:
            documents = yaml.dump(value, file)
        schema = eval(open('./FW-FreqencyRule_schema.py', 'r').read())
        v = Validator(schema)
        doc = load_doc()
        if (value["index"][-1])!="*":
            error_flag = True;
            error_rule.append("Error a in '"+ key + "' Index name must be end with * ")
        if v.validate(doc, schema) == False:
            error_flag = True;
            error_rule.append("Error in "+ key)
            error_rule.append(v.errors)
    elif((value["type"])=="any"):
        # print(value)
        with open(r'rule_file.yaml', 'w') as file:
            documents = yaml.dump(value, file)
        schema = eval(open('./FW-AnyRule_schema.py', 'r').read())
        v = Validator(schema)
        doc = load_doc()
        if (value["index"][-1])!="*":
            error_flag = True;
            error_rule.append("Error a in '"+ key + "' Index name must be end with * ")
        if v.validate(doc, schema) == False:
            error_flag = True;
            error_rule.append("Error in "+ key)
            error_rule.append(v.errors)
    elif((value["type"])=="flatline"):
        # print(value)
        with open(r'rule_file.yaml', 'w') as file:
            documents = yaml.dump(value, file)
        schema = eval(open('./FW-FlatlineRle_schema.py', 'r').read())
        v = Validator(schema)
        doc = load_doc()
        if (value["index"][-1])!="*":
            error_flag = True;
            error_rule.append("Error a in '"+ key + "' Index name must be end with * ")
        if v.validate(doc, schema) == False:
            error_flag = True;
            error_rule.append("Error in "+ key)
            error_rule.append(v.errors)
if(error_flag==False):
    print(True)
else:
    print(False)
#     print(error_rule)
    raise Exception(error_rule)











# for value in a["alert_params"].values():
#     # print("Type :: ",value["type"])
#     if((value["type"])=="frequency"):
#         # print(value)
#         with open(r'rule_file.yaml', 'w') as file:
#             documents = yaml.dump(value, file)
#         schema = eval(open('./FW-FreqencyRule_schema.py', 'r').read())
#         v = Validator(schema)
#         doc = load_doc()
#         if v.validate(doc, schema) == False:
#             error_flag = True;
#             error_rule.append("Error in FrequencyRule")
#             error_rule.append(v.errors)
#     elif((value["type"])=="any"):
#         # print(value)
#         with open(r'rule_file.yaml', 'w') as file:
#             documents = yaml.dump(value, file)
#         schema = eval(open('./FW-AnyRule_schema.py', 'r').read())
#         v = Validator(schema)
#         doc = load_doc()
#         if v.validate(doc, schema) == False:
#             error_flag = True;
#             error_rule.append("Error in AnyRule")
#             error_rule.append(v.errors)
#     elif((value["type"])=="flatline"):
#         # print(value)
#         with open(r'rule_file.yaml', 'w') as file:
#             documents = yaml.dump(value, file)
#         schema = eval(open('./FW-FlatlineRle_schema.py', 'r').read())
#         v = Validator(schema)
#         doc = load_doc()
#         if v.validate(doc, schema) == False:
#             error_flag = True;
#             error_rule.append("Error in FlatLineRule")
#             error_rule.append(v.errors)
# if(error_flag==False):
#     print(True)
# else:
#     print(False)
#     print(error_rule)
