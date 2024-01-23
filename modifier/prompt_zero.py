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

def parse_context(text):
    new_context = [
    {'role': 'system', 'content': f'{INSTRUCTION}'},
    {"role": "user", "content": f"{text}"}
     ]
    return new_context