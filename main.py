from googletrans import Translator, constants
import yaml

translator = Translator()


#========================================================#
#                     Varibles                           #
#========================================================#

language = "ru"  #change language
file_name_in = "file.yml" # input file name
file_name_out = "output.yml" # output file name

#========================================================#
#                     Varibles                           #
#========================================================#


with open(file_name_in, "r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

with open(file_name_out, "w") as out:
    for key1, value1 in data.items():
        if isinstance(value1, dict):
            print(f"{key1}:")
            out.write(f"{key1}:\n")
            for key2,value2 in value1.items():
                if isinstance(value2, list):
                    print(f"  {key2}:")
                    out.write(f"  {key2}:\n")
                    for item in value2:
                        if type(item) != str:
                            print(f'''    - {item}''')
                            out.write(f'''    - {item}\n''')
                        else:
                            translated = translator.translate(item, dest=language)
                            print(f'''    - "{translated.text}"''')
                            out.write(f'''    - "{translated.text}"\n''')
                elif type(value2) == int or type(value2) == float:
                    print(f'''  {key2}: {value2}''')
                    out.write(f'''  {key2}: {value2}\n''')
                else:
                    translated = translator.translate(value2, dest=language)
                    print(f'''  {key2}: "{translated.text}"''')
                    out.write(f'''  {key2}: "{translated.text}"\n''')
        else:
            if isinstance(value1, list):
                print(f"{key1}:")
                out.write(f"{key1}:\n")
                for item in value1:
                    if type(item) != str:
                        print(f'''  - {item}''')
                        out.write(f'''  - {item}\n''')
                    else:
                        translated = translator.translate(item, dest=language)
                        print(f'''  - "{translated.text}"''')
                        out.write(f'''  - "{translated.text}"\n''')
            elif type(value1) == int or type(value1) == float:
                print(f'''{key1}: {value1}''')
                out.write(f'''{key1}: {value1}\n''')
            else:
                translated = translator.translate(value1, dest=language)
                print(f'''{key1}: "{translated.text}"''')
                out.write(f'''{key1}: "{translated.text}"\n''')
