from transformers import AutoModel, AutoTokenizer
import torch
import json
import xml.etree.ElementTree as ET
from tqdm import tqdm
from os.path import join

def find_best_match(text_1, text_list, tokenizer, model):
    # Encode the texts
    def encode_text(text):
        inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
        return outputs.last_hidden_state.mean(dim=1)
    
    text_1_embedding = encode_text(text_1)
    text_list_embeddings = torch.cat([encode_text(text) for text in text_list])
    
    # Compute cosine similarities
    similarities = torch.nn.functional.cosine_similarity(text_1_embedding, text_list_embeddings)
    
    # Find the best match
    best_match_idx = similarities.argmax().item()
    best_match_text = text_list[best_match_idx]
    
    return best_match_text

def read_jsonl(file_path):
    # Open the file and read each line
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Parse JSON object from each line
            data.append(json.loads(line))
            # Now 'data' is a dictionary representing the JSON object
        file.close()
    return data
            

def coco_search_18(file_path, tokenizer, model, target_list, task_list):
    if 'tp' in file_path:
        gt_task = "Target-Present Search".lower()
    elif 'ta' in file_path:
        gt_task = "Target-Absent Search".lower()
    
    data = read_jsonl(file_path=file_path)

    correct = [0, 0]

    for d in tqdm(data):
        gt_target = d["question_id"].split('-')[-2]

        response = d["text"]

        wrapped_text = f"<root>{response}</root>"

        root = ET.fromstring(wrapped_text)

        task, stimulus = root[0].text.strip().lower(), root[1].text.strip().lower()
        if task not in task_list:
            # print(task)
            task = find_best_match(text_1=task, text_list=task_list, tokenizer=tokenizer, model=model)
            
        if stimulus not in target_list:
            # print(stimulus)
            stimulus = find_best_match(text_1=stimulus, text_list=target_list, tokenizer=tokenizer, model=model)
            

        if task == gt_task:
            correct[0] += 1
        if stimulus == gt_target:
            correct[1] += 1
    print(gt_task)
    print("Behavior accuracy:", correct[0]/len(data), "\nStimulus accuracy:", correct[1]/len(data))

if __name__ == '__main__':
     # Load the model and tokenizer
    model_name='sentence-transformers/all-MiniLM-L6-v2'
    gazette_model_dir = 'llava-v1.5-7b-Gazette_finetune_thinkaloud-ep1'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).cpu()
    target_list = ["bottle", "bowl", "car", "chair", "clock", "cup", "fork", "keyboard", "knife", "laptop", "microwave", "mouse", "oven", "potted plant", "sink", "stop sign", "toilet", "tv"]
    task_list = [i.lower() for i in ["Target-Present Search", "Target-Absent Search", "Object Referral", "Visual Question Answering"]]

    tp_file = join('../data/validation/model_answers/', gazette_model_dir, 'model_generations_tp.jsonl')
    coco_search_18(tp_file, tokenizer, model, target_list, task_list)
    ta_file = join('../data/validation/model_answers/', gazette_model_dir, 'model_generations_ta.jsonl')
    coco_search_18(ta_file, tokenizer, model, target_list, task_list)