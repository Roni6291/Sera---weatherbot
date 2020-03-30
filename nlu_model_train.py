import logging
import pprint
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer, Interpreter




logfile = './logs/nlu_model_train.log'


def train_nlu(data_path, configs, model_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    training_data = load_data(data_path)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_path, fixed_model_name='weathernlu')


def run_nlu(nlu_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    interpreter = Interpreter.load(nlu_path)
    pprint.pprint(interpreter.parse("What is the weather at Toronto"))
    pprint.pprint(interpreter.parse("What is the temperature at Tokyo"))
    pprint.pprint(interpreter.parse("I am planning a trip to Auckland. What is the weather out there?"))
    pprint.pprint(interpreter.parse("hello Sera"))

if __name__ == '__main__':
    # train_nlu('./data/nlu.md', './config.json', './models/nlu')
    run_nlu('./models/nlu/default/weathernlu')

