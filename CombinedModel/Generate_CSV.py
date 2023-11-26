import subprocess
import os
import re
import glob
from joblib import Parallel, delayed


def extract_probabilities(output_text):
    """
    Extracts probabilities from the output text of result.txt.

    Parameters:
        output_text (str): The text content of result.txt.

    Returns:
        list: A list containing the extracted probabilities, or None if probabilities are not found.
    """
    match = re.search(r'Probability \[(.*?), (.*?)\]', output_text)
    if match:
        probabilities = [float(match.group(1)), float(match.group(2))]
        return probabilities
    else:
        return None


def execute_and_read_output():
    current_directory = "D:/CS4211/SubmissionModels/CombinedModel"  #TODO: Change to the file path of the curreny working directory
    pcsp_files = glob.glob(current_directory + "/" + "pcsp2/*.pcsp")
    file_names = ['pcsp2/' + os.path.basename(file).split('.')[0] for file in pcsp_files]
    print(file_names)
    #result = process_pcsp(current_directory, file_names[0])
    result = Parallel(n_jobs=-2)(delayed(process_pcsp)(current_directory, name) for name in file_names)
    with (open('MDP_pred.csv', 'w') as csv):
        csv.write('date,P1Name,P2Name,P1WinProb,P2WinProb\n')
        csv.writelines(result)


def process_pcsp(current_directory, file_name):
    result_file_path = current_directory + "/" + "result2/" + os.path.basename(file_name) + ".txt"
    pcsp_file_path = current_directory + "/" + file_name + ".pcsp"
    # Define the command and arguments
    command = 'D:/CS4211/PAT/PAT3.Console.exe' #TODO: Change to the correct file path of PAT3.Console.exe
    args = ['-pcsp', pcsp_file_path, result_file_path]
    execute = [command] + args
    # Run the command
    subprocess.run(execute, check=True)
    # Read the result from result.txt
    with open(result_file_path, 'r') as file:
        output = file.read()
        probabilities = extract_probabilities(output)
        if (probabilities == None): return
        splitted = file_name.split('_')
        p1win = round(sum(probabilities) / 2, 4)
        p2win = 1 - p1win
        return f"{splitted[2]},{splitted[3].replace('-', ' ')},{splitted[4].split('.')[0].replace('-', ' ')},{p1win:.4f},{p2win:.4f}\n"


if __name__ == "__main__":
    execute_and_read_output()
