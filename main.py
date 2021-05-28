import case_generator
import test_tool

def main():
    flag = True
    while flag:
        user_input = str(input("\n1. Generate Test Case \n2. Run Test Case \n3. Quit\n"))

        if(user_input == "1"):
            json_file = str(input("Select JSON file for input\n"))
            options = str(input("\nDo you want to generate DELETE cases?(Y/N) \n"))

            if(options.lower() == "y"):
                id =  str(input("ID Key"))
                case_generator.run_generation(json_file,[1], id)

            elif(options.lower() == "n"):
                case_generator.run_generation(json_file, [0])



        elif (user_input == "2"):
            test_tool.testing_tool()
        elif(user_input == "3"):
            flag = False
            break

main()