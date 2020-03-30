import json

def main():
    with open(r"D:\Users\1114154\Documents\Natural language Understanding -Rasa\Weatherbot_Tutorial-master\Weatherbot_Tutorial-master\Full_Code_Latest\data\data.json", 'r') as file:
            nlu = json.load(file)
    print(json.dumps(nlu, indent=4))



if __name__ == '__main__':
    main()
