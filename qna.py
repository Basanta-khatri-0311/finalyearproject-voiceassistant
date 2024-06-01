# import torch
# from transformers import BertTokenizer, BertModel
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# # Load the dataset
# def load_dataset(file_path):
#     dataset = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             if '|' in line:
#                 question, answer = line.strip().split('|')
#                 dataset.append({'question': question.strip(), 'answer': answer.strip()})
#     return dataset

# # Preprocess the dataset to fit BERT input format
# def preprocess_dataset(dataset, tokenizer):
#     questions = [item['question'] for item in dataset]
#     answers = [item['answer'] for item in dataset]
    
#     encoded_questions = tokenizer(questions, padding='max_length', truncation=True, max_length=64, return_tensors='pt')
#     encoded_answers = tokenizer(answers, padding='max_length', truncation=True, max_length=64, return_tensors='pt')
    
#     encoded_dataset = []
#     for i, item in enumerate(dataset):
#         encoded_item = {
#             'question': item['question'],
#             'answer': item['answer'],
#             'question_input_ids': encoded_questions['input_ids'][i],
#             'question_attention_mask': encoded_questions['attention_mask'][i],
#             'answer_input_ids': encoded_answers['input_ids'][i],
#             'answer_attention_mask': encoded_answers['attention_mask'][i]
#         }
#         encoded_dataset.append(encoded_item)
#     return encoded_dataset

# # Load and preprocess dataset
# dataset_file = 'dataset.txt'
# dataset = load_dataset(dataset_file)

# # Tokenization
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# # Preprocess the dataset
# encoded_dataset = preprocess_dataset(dataset, tokenizer)

# # BERT model for generating embeddings
# model = BertModel.from_pretrained('bert-base-uncased')

# # Calculate embeddings for a given text
# def calculate_embedding(text, tokenizer, model):
#     inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=64)
#     with torch.no_grad():
#         outputs = model(**inputs)
#         embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
#     return embeddings

# # Prediction function with BERT
# def predict_answer(question, dataset, tokenizer, model):
#     question_embedding = calculate_embedding(question, tokenizer, model)
#     best_answer = None
#     best_similarity = -1  # Initialize with a low value
    
#     for item in dataset:
#         answer_embedding = calculate_embedding(item['answer'], tokenizer, model)
#         similarity_score = cosine_similarity([question_embedding], [answer_embedding])[0][0]
#         if similarity_score > best_similarity:
#             best_similarity = similarity_score
#             best_answer = item['answer']
    
#     return best_answer


# import torch
# from transformers import BertTokenizer, BertModel
# from sklearn.metrics.pairwise import cosine_similarity

# # Load the dataset
# def load_dataset(file_path):
#     dataset = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             if '|' in line:
#                 question, answer = line.strip().split('|')
#                 dataset.append({'question': question.strip(), 'answer': answer.strip()})
#     return dataset

# # Preprocess the dataset to fit BERT input format
# def preprocess_dataset(dataset, tokenizer):
#     encoded_dataset = []
#     for item in dataset:
#         encoded_item = tokenizer(item['question'], item['answer'], padding='max_length', truncation=True, max_length=128, return_tensors='pt')
#         encoded_dataset.append(encoded_item)
#     return encoded_dataset

# # Load and preprocess dataset
# dataset_file = 'dataset.txt'
# dataset = load_dataset(dataset_file)

# # Tokenization
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# # Preprocess the dataset
# encoded_dataset = preprocess_dataset(dataset, tokenizer)

# # BERT model for generating embeddings
# model = BertModel.from_pretrained('bert-base-uncased')

# # Calculate embeddings for a given text
# def calculate_embedding(inputs, model):
#     with torch.no_grad():
#         outputs = model(**inputs)
#         embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
#     return embeddings

# # Prediction function with BERT
# def predict_answer(question, dataset, tokenizer, model):
#     question_inputs = tokenizer(question, padding=True, truncation=True, max_length=128, return_tensors='pt')
#     question_embedding = calculate_embedding(question_inputs, model)
    
#     best_answer = None
#     best_similarity = -1  # Initialize with a low value
    
#     for item in dataset:
#         answer_embedding = calculate_embedding(item, model)
#         similarity_score = cosine_similarity([question_embedding], [answer_embedding])[0][0]
#         if similarity_score > best_similarity:
#             best_similarity = similarity_score
#             # Update best_answer to the corresponding text from the dataset
#             best_answer = tokenizer.decode(item['input_ids'][0], skip_special_tokens=True)
    
#     return best_answer


import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        for line in file:
            if '|' in line:
                question, answer = line.strip().split('|')
                dataset.append({'question': question.strip(), 'answer': answer.strip()})
    return dataset

# Preprocess the dataset to fit BERT input format
def preprocess_dataset(dataset, tokenizer):
    encoded_dataset = []
    for item in dataset:
        encoded_question = tokenizer(item['question'], padding='max_length', truncation=True, max_length=128, return_tensors='pt')
        encoded_answer = tokenizer(item['answer'], padding='max_length', truncation=True, max_length=128, return_tensors='pt')
        encoded_item = {
            'question_input_ids': encoded_question['input_ids'],
            'question_attention_mask': encoded_question['attention_mask'],
            'answer_input_ids': encoded_answer['input_ids'],
            'answer_attention_mask': encoded_answer['attention_mask']
        }
        encoded_dataset.append(encoded_item)
    return encoded_dataset

# Load and preprocess dataset
dataset_file = 'dataset.txt'
dataset = load_dataset(dataset_file)

# Tokenization
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Preprocess the dataset
encoded_dataset = preprocess_dataset(dataset, tokenizer)

# BERT model for generating embeddings
model = BertModel.from_pretrained('bert-base-uncased')

# Calculate embeddings for a given text
def calculate_embedding(input_ids, attention_mask, model):
    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embeddings

# Prediction function with BERT
def predict_answer(question, dataset, tokenizer, model):
    question_inputs = tokenizer(question, padding=True, truncation=True, max_length=128, return_tensors='pt')
    question_embedding = calculate_embedding(question_inputs['input_ids'], question_inputs['attention_mask'], model)
    
    best_answer = None
    best_similarity = -1  # Initialize with a low value
    
    for item in dataset:
        answer_embedding = calculate_embedding(item['answer_input_ids'], item['answer_attention_mask'], model)
        similarity_score = cosine_similarity([question_embedding], [answer_embedding])[0][0]
        if similarity_score > best_similarity:
            best_similarity = similarity_score
            best_answer = tokenizer.decode(item['answer_input_ids'][0], skip_special_tokens=True)
    
    return best_answer




