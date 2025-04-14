def main():
    # Ask the user for the file name
    filename = input("Enter the name of the file to read from: ")

    try:
        # Open the file for reading
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File read successfully.")

        # Modify the content from the file
        modified_content = "Modified content: " + content

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
            print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"There was an error: The file '{filename}' does not exist.")
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
    except IOError as e:
        print(f"IOError: {e}")
    finally:
        print("Execution completed.")
        file.close()


if __name__ == "__main__":
    main()
