import configparser
import sys
import os
import requirements
import api

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        sys.exit(1)

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file {filename}: {e}")
        sys.exit(1)

def main():
    try:
        requirements.run_all_checks()
        requirements.create_files()

    except Exception as e:
        print(f"An error occurred while checking requirements: {e}")
        sys.exit(1)

    try:
        # Read config
        config = configparser.ConfigParser()
        config.read('config.ini')
        gpt_model = config['DEFAULT']['GPT_MODEL']
        api_key = config['DEFAULT']['API_KEY']
        job_posting_file = config['DEFAULT']['JOB_POSTING_FILE']
        resume_file = config['DEFAULT']['RESUME_FILE']
        recommendations_file = config['DEFAULT']['RECOMMENDATIONS_FILE']

        api.set_api_key(api_key)

        job_posting = read_file(job_posting_file)
        resume = read_file(resume_file)

        # Formulate the persona and prompt
        persona = "You are an AI recruiter assistant that is analyzing a resume to determine if the candidate is a good match for a job posting."
        prompt = f"Given the following job description:\n\n{job_posting}\n\nAnd the following candidate's resume:\n\n{resume}\n\nProvide a brief feedback if the resume is already a great match or recommendations on how to improve the resume to be considered a top candidate for this job. The recommandation should start with a mathematical score of the match (0-100) with 100 being a perfect match based on analyzing the entire resume against the job description."

        recommendations = api.get_recommendations(gpt_model, persona, prompt)

        write_file(recommendations_file, recommendations)
        print(f"Recommendations written to {recommendations_file}")
        os.startfile(recommendations_file)
    except configparser.Error as e:
        print(f"Error reading configuration file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()