import pandas as pd
from analysis import process_dataframe_to_string, get_completion_from_messages, num_tokens_from_string
import prompt_few
import prompt_zero
import config
import openai
import os

eg = True ## few-shot: True, zero-shot: False
openai.api_key = config.OPENAI_API_KEY
csv_file = 'test/new_data/allprompt.csv'
anno_name = csv_file.split('/')[2].split('.')[0]
save_folder = f'test/gpt4_single//{anno_name}/'

output_file = anno_name + '.txt'

outname = output_file.split('.')[0]
if not os.path.exists(save_folder):
    os.makedirs(save_folder, exist_ok=True)

all_data = pd.read_csv(csv_file, encoding='ISO-8859-1')
all_responses = []
prompts = []
results = []

print(f"{csv_file}")

for index, row in all_data.iterrows():
    prompt = row['prompt']  # Assuming the column name is 'prompt'
    if eg:
        context = prompt_few.parse_context(prompt)
        prompts.append(prompt)
        results.append(context)
        print(f'flag1: {index}')
        if index==0:
            print(context)
        dic = get_completion_from_messages(context, model="gpt-4")
        all_responses.append(dic)
        cur_out = os.path.join(save_folder, f'{index}.txt')
        print(f'flag2: {index}')
        with open(cur_out, "w", encoding="utf-8") as file:
            file.write(dic)
            
    else:
        print('wrong')
        context = prompt_zero.parse_context(prompt)
        prompts.append(prompt)
        results.append(context)
        print(f'flag1: {index}')
        if index==0:
            print(context)
        dic = get_completion_from_messages(context, model="gpt-4")
        all_responses.append(dic)
        cur_out = os.path.join(save_folder, f'{index}.txt')
        print(f'flag2: {index}')
        with open(cur_out, "w", encoding="utf-8") as file:
            file.write(dic)
            

# Save all responses to a single text file
with open(os.path.join(save_folder, output_file), "w", encoding="utf-8") as file:
    file.write("\n".join(all_responses))

df = pd.DataFrame({'prompt': prompts, 'result': results, 'modi': all_responses})
out_file_name = outname + '.csv'
df.to_csv(os.path.join(save_folder, out_file_name), index=False)

