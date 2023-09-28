import openai
import os


# OpenAI KEY
OPENAI_API_KEY = "OpenAI 인증 키"

# txt 경로 설정
source_folder = '/path/to/source_folder'
destination_folder = '/path/to/destination_folder'


def read_txt_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f'Error: {e}')
        return None


def create_response_txt_files(source_folder, destination_folder):
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        for filename in os.listdir(source_folder):
            if filename.endswith('.txt'):
                source_file_path = os.path.join(source_folder, filename)
                destination_file_path = os.path.join(destination_folder, filename)
                abstract = read_txt_content(source_file_path)

                if abstract is not None:
                    with open(destination_file_path, 'w') as dest_file:
                        results = get_gpt_response(abstract)
                        dest_file.write(results)

                    print(f'Created modified {filename} in {destination_folder}')
    except Exception as e:
        print(f'Error: {e}')


def get_gpt_response(text):
    # openai API 키 인증
    openai.api_key = OPENAI_API_KEY
    model = "gpt-3.5-turbo"

    # 질문
    query = text

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query}
    ]

    # ChatGPT API 호출
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    return response['choices'][0]['message']['content']


create_response_txt_files(source_folder, destination_folder)
