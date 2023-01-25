from googletrans import Translator, constants
import yaml

language = "ru"

translator = Translator()

with open("file.yml", "r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

with open("output.yml", "w") as out:
    for key1, value1 in data.items():
        if isinstance(value1, dict):
            print(f"{key1}:")
            out.write(f"{key1}:\n")
            #Перебір всіх ключів і значень
            for key2,value2 in value1.items():
                if type(value2) == int or type(value2) == float:
                    print(f'''  {key2}: {value2}''')
                    out.write(f'''  {key2}: {value2}\n''')
                else:
                    translated = translator.translate(value2, dest=language)
                    print(f'''  {key2}: "{translated.text}"''')
                    out.write(f'''  {key2}: "{translated.text}"\n''')
        else:
            if type(value1) == int or type(value1) == float:
                print(f'''{key1}: {value1}''')
                out.write(f'''{key1}: {value1}\n''')
            else:
                translated = translator.translate(value1, dest=language)
                print(f'''{key1}: "{translated.text}"''')
                out.write(f'''{key1}: "{translated.text}"\n''')
