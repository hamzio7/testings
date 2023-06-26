import json
import os

def add_contents_to_json():
    themes_json_path = "themes_test.json"
    themes_new_json_path = "themes_test.json"

    with open(themes_json_path, 'r') as json_file:
        json_content = json_file.read()

    json_object = json.loads(json_content)
    themes_array = json_object["themes"]

    for theme_obj in themes_array:
        folder = theme_obj["folder_name"]
        folder_path = os.path.join("themes", folder)
        contents = os.listdir(folder_path)
        contents_array = []

        if contents:
            for name in contents:
                content_object = {"name": name}
                contents_array.append(content_object)

        theme_obj["contents"] = contents_array
        print("addContentsToJson:", folder)

    with open(themes_new_json_path, 'w') as json_file:
        json.dump(json_object, json_file)

# Call the function
add_contents_to_json()
