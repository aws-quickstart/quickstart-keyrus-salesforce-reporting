"""This will convert the raw data from describe-appflow into a valid YAML template"""

import sys, json
import collections
import yaml

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def ToTitleCase(name):
    temp = name.split('_')
    return ''.join(upperFirst(ele) for ele in temp)

def upperFirst(name):
    if name[:1].islower():
        return name[:1].upper() + name[1:]
    return name

def dict_merge(dct, merge_dct):
    """ Recursive dict merge. 
    Originally from https://gist.github.com/angstwad/bf22d1822c38a92ec0a9
    Modified by Dan Afonso to convert camelCase to TitleCase
    and also handle lists
    Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
    ``dct``.
    :param dct: dict onto which the merge is executed
    :param merge_dct: dct merged into dct
    :return: None
    """

    # this is a recursive copy of lists following the same logic
    if isinstance(merge_dct, list):
        for v in merge_dct:
            if isinstance(v, dict):
                dct.append({})
                dict_merge(dct[-1], v)
            else:
                dct.append(v)
        return 
    for k, v in merge_dct.items():
        name = ToTitleCase(k)
        if (k in dct and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], collections.Mapping)):
            dict_merge(dct[name], merge_dct[k])
        elif (isinstance(merge_dct[k], list)):
            if not k in dct:
                dct[name] = []
            dict_merge(dct[name], merge_dct[k])
        else:
            dct[name] = merge_dct[k]

def dictToKeyValue(d, keyName = 'Key', valueName = 'Value'):
    outArray = []
    for key in d:
        outArray.append({keyName: key, valueName: d[key]})
    return outArray

# print(ToTitleCase("holeString"))
# print(ToTitleCase("HoleString"))
# print(ToTitleCase("hole_String_1"))

# print (dictToKeyValue({"DESTINATION_DATA_TYPE": "character varying",
#                 "SOURCE_DATA_TYPE": "id"}))
# sys.exit(0)

af = json.loads(sys.stdin.read())
if not ("flowName" in af):
    print("Could not find FlowName. Aborting")
    sys.exit(2)

flowName = ToTitleCase(af["flowName"])
properties = {}
out = {"Resources": {flowName: {"Type": "AWS::AppFlow::Flow", "Properties": properties}}}
for section in ["description", "destinationFlowConfigList", "flowName", 
        "kmsArn", "sourceFlowConfig", "tags", "tasks", "triggerConfig"]:
    if section in af:
        cfnSection = ToTitleCase(section)
        if isinstance(af[section], list):
            properties[cfnSection] = []
            dict_merge(properties[cfnSection], af[section])
        elif isinstance(af[section], dict):
            properties[cfnSection] = {}
            dict_merge(properties[cfnSection], af[section])
        else:
            properties[cfnSection] = af[section]

# Next we need to do a pass where we change the KEY: Value stuff in
# the "Tasks" list. API give back sensib "KEY: VALUE" mappings but CFN wants
# [ { Key: name, Value: value}, ... ] format
for task in properties["Tasks"]:
    replaceWith = dictToKeyValue(task["TaskProperties"])
    task["TaskProperties"] = replaceWith

print(yaml.safe_dump(out, indent=2))
# dict_merge(out[af["flowName"]])
# Recursively copy the object and apply transforms


