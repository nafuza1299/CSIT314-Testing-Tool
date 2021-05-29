import case_generator
import API_tester
import glob
import os

json_files = []
for file in glob.glob("*.json"):
    if(file !="output.json"):
        json_files.append(file)

'''
Testing tool for APIs.
Can generate and run test cases based on specified JSON.

'''

def main():
    flag = True
    while flag:
        user_input = str(input("\n1. Generate Test Case \n2. Run Test Case \n3. Quit\n"))
        if(user_input == "1"):

            # print all existing json files in current dir. that is not output.json
            print('Files in the system:')
            for files in json_files:
                print(files)

            if (len(json_files) <= 0):
                print("No JSON files in the system")

            json_file = str(input("\nSelect JSON file for input\n"))
            option_1 = str(input("\nDo you want to generate DELETE cases?(Y/N) \n"))
            option_2 = str(input("\nDo you want to generate PUT cases?(Y/N) \n"))
            id = str(input("\nID Key\n"))

            if(option_1.lower() == "y"):
                option_1 = 1

            elif(option_1.lower() == "n"):
                option_1 = 0

            if (option_2.lower() == "y"):
                option_2 = 1

            elif (option_2.lower() == "n"):
                option_2 = 0

            case_generator.run_generation(json_file, id, option_1, option_2)

        elif (user_input == "2"):
            if os.path.exists("output.json"):
                API_tester.testing_tool()
            else:
                print("output.json is missing please generate it first.")

        elif(user_input == "3"):
            flag = False

main()