from flask import Flask, request, jsonify
import os
import tempfile
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from config import model_name
from utils import format_user_question
from file_processing import clone_github_repo, load_and_index_files
from questions import ask_question, QuestionContext
from flask_cors import CORS
from flask_restful import Resource, Api
import shutil

app = Flask(__name__)
cors = CORS(app)
api = Api(app)


repo_index = None
repo_documents = None
repo_file_type_counts = None
repo_filenames = None


class CloneRepository(Resource):
    def post(self):
        global repo_index, repo_documents, repo_file_type_counts, repo_filenames
        data = request.get_json()
        github_url = data.get('github_url')
        try:
            if github_url:
                with tempfile.TemporaryDirectory() as local_path:
                    if clone_github_repo(github_url, local_path):
                        repo_index, repo_documents, repo_file_type_counts, repo_filenames = load_and_index_files(local_path)
                        return jsonify({'message': 'Repository cloned successfully.', 'repo': github_url})
                    else:
                        return jsonify({'error': 'Failed to clone the repository.'})
            else:
                return jsonify({'error': 'Missing github_url parameter.'})
        except Exception as e:
            return jsonify({'error': str(e)})


class AskQuestion(Resource):
    def post(self):
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        data = request.get_json()
        user_question = data.get('question')

        if user_question:
            if repo_index is None:
                return jsonify({'answer': '🙏 Apologies, Dev, but this repository includes files that RepoReader does not support. Kindly attempt with an alternative repository. 🔄💖'})

            llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.8)

            template = """
            Repo: {repo_name} | Conv: {conversation_history} | Docs: {numbered_documents} | Q: {question} | FileCount: {file_type_counts} | FileNames: {filenames}

            Instr: 
            1. Answer based on context/docs.
            2. Focus on repo/code.
            3. Consider:
                a. Purpose/features - describe.
                b. Functions/code - provide details/samples.
                c. Setup/usage - give instructions.
            4. Provide creative suggestions for contributions to this repository or codebase if requested.
            5. Unsure? Say "I am not sure".
            

            Answer:
            """

            prompt = PromptTemplate(
                template=template,
                input_variables=["repo_name", "conversation_history", "question", "numbered_documents", "file_type_counts", "filenames"]
            )

            llm_chain = LLMChain(prompt=prompt, llm=llm)

            conversation_history = ""
            repo_name = data.get('repo_name') 
            github_url = data.get('github_url') 

            question_context = QuestionContext(repo_index, repo_documents, llm_chain, model_name, repo_name, github_url, conversation_history, repo_file_type_counts, repo_filenames)
            
            user_question = format_user_question(user_question)

            try:
                answer = ask_question(user_question, question_context)
                conversation_history += f"Question: {user_question}\nAnswer: {answer}\n"
                return jsonify({'answer': answer})
            except Exception as e:
                return jsonify({'error': str(e)})
        else:
            return jsonify({'error': 'Missing question parameter.'})


class ResetRepository(Resource):
    def post(self):
        data = request.get_json()
        req = data.get('request')
        req = str(req)
        if req == "Reset github repo":
            global repo_index, repo_documents, repo_file_type_counts, repo_filenames
            repo_index = None
            repo_documents = None
            repo_file_type_counts = None
            repo_filenames = None
            
            return jsonify({'message': 'Repository data has been reset.'})
        else:
            return jsonify({'message': 'Invalid request'})


api.add_resource(CloneRepository, '/clone')
api.add_resource(AskQuestion, '/ask')
api.add_resource(ResetRepository, '/reset')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000 ,debug=True)
