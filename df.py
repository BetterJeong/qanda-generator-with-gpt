import pandas as pd

file_path = './datas/output.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

questions = []
answers = []
current_text = ""
is_question = None

for line in lines:
    line = line.strip()
    if line.startswith('Q:'):
        if current_text and is_question is not None:
            if is_question:
                questions.append(current_text)
            else:
                answers.append(current_text)
        current_text = line[3:].strip()
        is_question = True
    elif line.startswith('A:'):
        if current_text and is_question is not None:
            if is_question:
                questions.append(current_text)
            else:
                answers.append(current_text)
        current_text = line[3:].strip()
        is_question = False
    else:
        current_text += " " + line.strip()

if current_text and is_question is not None:
    if is_question:
        questions.append(current_text)
    else:
        answers.append(current_text)

min_length = min(len(questions), len(answers))

df = pd.DataFrame({'Q': questions[:min_length], 'A': answers[:min_length]})

print(df)