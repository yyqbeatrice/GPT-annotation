
modifier_dic_zero = '''
    "Subject": "Refers to the primary object or focal point within an image, capturing the viewer's attention and serving as the central focus.",
    "Style": "Encompasses the artistic approach and desired visual characteristics in the image. It includes elements such as the choice of artistic medium, artistic references, and rendering techniques.",
    "Mood": "Represents the emotional or intellectual message that the image should convey to the viewer, evoking a specific sentiment or thought.",
    "Lighting": "Describes how the scene in the image is illuminated, encompassing attributes like light quality, source, and direction to set the visual ambiance.",
    "Environment": "Relates to the setting or context in which the image takes place, spanning physical locations and imaginative or fictional realms.",
    "Color": "Refers to the color scheme and palette employed within the image, encompassing considerations of vibrancy, saturation, and the selection of specific colors to create a particular visual impact.",
    "Element Value": "Involves technical and compositional aspects of the image, potentially including technical specifications like resolution, aspect ratios, and descriptive terms that define the image.",
    "Composition": "Relates to the arrangement of elements within the image frame, encompassing considerations of camera angles, settings, and principles of organization to achieve a desired visual composition.",
    "Repeating term": "Identifies and describes elements that are recurrent or duplicated within the image, highlighting patterns or repetitions.",
    "Negative prompt": "Relate to the exclusion of specific elements or aspects from the image description, indicating what should not be included.",
    "Collective Noun": "Involve the use of specific numbers or collective nouns to describe groups of objects within the image, specifying quantities or groupings of subjects.",
'''


INSTRUCTION = f"""
    To identify the modifier categories mentioned in the provided prompt using the given definitions:
    1. Consider the modifier one by one. 
    2. Generate a Python list containing the recognized modifiers. 

    Modifier Definitions:
    ```
    {modifier_dic_zero}
    ```
    """



### pure example
prompt_1 = "scary horror creature!!! nendoroid!!! figurine, studio lighting, grey background, no shadow, trending on artstation, 4 k, highly detailed!!!"
example_1 = "['Subject', 'Style', 'Mood', 'Lighting', 'Element Value']"

prompt_2= "inside of a lemonade fast food restaurant, direct wide angle view from the exterior looking in through shop windows and front glass door, atmospheric, dreamy, realistic, full frame, 35mm film, photography, gregory crewdson, gregory crewdson"
example_2 = "['Style', 'Environment', 'Element Value', 'Composition']"

prompt_3= "a photograph portrait of old jerma985 in his eighties who looks like jerma985 wearing a blazer in the 1990s, jerma985, looks like jerma985, taken in the early 1990s, taken on a 1990s camera, realistic, hyperrealistic, very realistic, highly detailed, very detailed, extremely detailed, detailed, digital art, trending on artstation, headshot and bodyshot"
example_3 = "['Subject', 'Style', 'Element Value', 'Composition', 'Repeating term']"

prompt_4 = "an artwork of a broken wine bottle in the medium of dry pigments"
example_4 = "['Collective Noun', 'Style', 'Subject']"

prompt_5 = "album cover of an avant-garde Japanese bjd geisha vampire queen with porcelain skin in Victorian red dress in the style of dark-fantasy lolita fashion painted by Yoshitaka Amano, Takato Yamamoto, Christopher Shy, DMT art, symmetrical vogue face portrait, intricate detail, artstation, cgsociety, artgerm, gold skulls, rococo, no hands"
example_5 = "['Subject', 'Style', 'Color', 'Element Value', 'Composition', 'Negative prompt', 'Collective Noun']"




### following is for few-shot prompting
def parse_context_few(text):
    new_context = [
    {'role': 'system', 'content': f'{INSTRUCTION}'},
    {"role": "system", "name":"example_user", "content": f"{prompt_1}"},
    {"role": "system", "name": "example_output", "content": f"{example_1}"},
    {"role": "system", "name":"example_user", "content": f"{prompt_2}"},
    {"role": "system", "name": "example_output", "content": f"{example_2}"},
    {"role": "system", "name":"example_user", "content": f"{prompt_3}"},
    {"role": "system", "name": "example_output", "content": f"{example_3}"},
    {"role": "system", "name":"example_user", "content": f"{prompt_4}"},
    {"role": "system", "name": "example_output", "content": f"{example_4}"},
    {"role": "system", "name":"example_user", "content": f"{prompt_5}"},
    {"role": "system", "name": "example_output", "content": f"{example_5}"},
    {"role": "user", "content": f"{text}"}
     ]
    return new_context


### following is for zero-shot prompting
def parse_context_zero(text):
    new_context = [
    {'role': 'system', 'content': f'{INSTRUCTION}'},
    {"role": "user", "content": f"{text}"}
     ]
    return new_context
