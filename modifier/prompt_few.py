#### following by chatgpt
modifier_dic_zero = '''
    "Subject": "Refers to the primary objects or focal points within an image, capturing the viewer's attention and serving as the central focus.",
    "Style": "Encompasses the artistic approach and desired visual characteristics in the image. It includes elements such as the choice of artistic medium, artistic references, and rendering techniques.",
    "Mood": "Represents the emotional message that the image should convey to the viewer, evoking a specific sentiment or thought.",
    "Lighting": "Describes how the scene in the image is illuminated, encompassing attributes like light quality, source, and direction to set the visual ambiance.",
    "Environment": "Relates to the setting or context in which the image takes place, spanning physical locations and imaginative or fictional realms.",
    "Color": "Refers to the color scheme and palette employed within the image, encompassing considerations of vibrancy, saturation, and the selection of specific colors to create a particular visual impact.",
    "Element Value": "Involves technical and compositional aspects of the image, potentially including technical specifications like resolution, aspect ratios, and descriptive terms that define the image. It can also encompass expressions conveying intellectual messages to describe certain properties, such as abstract adjectives.",
    "Composition": "Relates to the arrangement of elements within the image frame, encompassing considerations of camera angles, settings, and principles of organization to achieve a desired visual composition.",
    "Repeating term": "Identifies and describes elements that are recurrent or duplicated within the image, highlighting patterns or repetitions.",
    "Negative prompt": "Relate to the exclusion of specific elements or aspects from the image description, indicating what should not be included.",
    "Collective Noun": "Involve specific numbers or collective nouns to describe groups of objects within the image, specifying quantities or groupings of subjects.",
'''

INSTRUCTION = f"""
    In the context of text-image generation, the provided text serves as the prompt. 
    Your task is to label modifiers within the text based on the provided definitions. Note that a single word may belong to multiple modifier categories. 
    
    Follow the steps below:
    1. Output the reasons for recognized modifiers in the provided text. Indicate what expression in the text can be categorized as that modifier.
    2. Produce a Python list on a separate line, enumerating the identified modifier labels.

    Modifier Definitions:
    ```
    {modifier_dic_zero}
    ```
    Output Format:
    ```
    Reasons:
    1. Explanation of the first recognized modifier
    2. Explanation of the second recognized modifier
    ...

    Modifier List:
    ['modifier1', 'modifier2', 'modifier3', ...]
    ```
    """

prompt_1 = "scary horror creature!!! nendoroid!!! figurine, studio lighting, grey background, no shadow, trending on artstation, 4 k, highly detailed!!!"
example_1 = """
'creature', 'figurine' are Subject
'nendoroid', 'trending on artstation' are Style
'scary', 'horror'are Mood
'studio lighting', 'grey background', 'no shadow' are Lighting
'4k', 'detailed' are Element Value

Modifier List:
['Subject', 'Style', 'Mood', 'Lighting', 'Element Value']
"""

prompt_2= "inside of a lemonade fast food restaurant, direct wide angle view from the exterior looking in through shop windows and front glass door, atmospheric, dreamy, realistic, full frame, 35mm film, photography, gregory crewdson, gregory crewdson"
example_2 = """
'realistic', 'photography', 'gregory crewdson' are Style
'inside of a lemonade fast food restaurant' is Environment
'full frame', '35mm film', 'gregory crewdson' are Element Value
'direct wide angle view from the exterior' is Composition

Modifier List:
['Style', 'Environment', 'Element Value', 'Composition']
"""

prompt_3= "a photograph portrait of old jerma985 in his eighties who looks like jerma985 wearing a blazer in the 1990s, jerma985, looks like jerma985, taken in the early 1990s, taken on a 1990s camera, realistic, hyperrealistic, very realistic, highly detailed, very detailed, extremely detailed, detailed, digital art, trending on artstation, headshot and bodyshot"
example_3 = """
'jerma985 ' is Subject
'photograph portrait', 'realistic', 'hyperrealistic',  'very realistic', 'digital art', 'trending on artstation' are Style
'highly detailed, very detailed, extremely detailed, detailed' are Element Value
'headshot and bodyshot' is Composition
'jerma985', '1990s', 'realistic', 'detailed' are Repeating term

Modifier List:
['Subject', 'Style', 'Element Value', 'Composition', 'Repeating term']
"""

prompt_4 = "an artwork of a broken wine bottle in the medium of dry pigments"
example_4 = """
'wine bottle' is Subject
'dry pigments' is Style
'a' in 'a broken wine bottle' is Collective Noun

Modifier List:
['Collective Noun', 'Style', 'Subject']
"""

prompt_5 = "album cover of an avant-garde Japanese bjd geisha vampire queen with porcelain skin in Victorian red dress in the style of dark-fantasy lolita fashion painted by Yoshitaka Amano, Takato Yamamoto, Christopher Shy, DMT art, symmetrical vogue face portrait, intricate detail, artstation, cgsociety, artgerm, gold skulls, rococo, no hands"
example_5 = """
'Japanese bjd geisha vampire queen', 'skulls' are Subject
'album cover', 'avant-garde', 'dark-fantasy lolita fashion', 'Yoshitaka Amano', 'Takato Yamamoto', 'Christopher Shy', 'DMT art', 'artstation', 'cgsociety', 'artgerm', are Style
'red', 'gold' are Color
'intricate detail', Element Value
'symmetrical vogue face portrait' are Composition
'no hands' is Negative prompts
'an' in 'an avant-garde Japanese bjd geisha vampire queen' is Collective Noun

Modifier List:
['Subject', 'Style', 'Color', 'Element Value', 'Composition', 'Negative prompt', 'Collective Noun']
"""

def parse_context(text):
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

