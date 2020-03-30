import logging
from rasa_core import config as policy_config
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig


logfile = './logs/dialogue_model.log'


def train_core(domain_file, model_path, training_data_file, policies=policy_config.load('policy.yml')):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    agent = Agent(domain_file, policies=policies)
    training_data = agent.load_data(training_data_file)
    agent.train(training_data)
    agent.persist(model_path)
    return agent


def run_core(core_model_path, nlu_model_path, action_endpoint_url):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    nlu_interpreter = RasaNLUInterpreter(nlu_model_path)
    action_endpoint = EndpointConfig(url=action_endpoint_url)
    agent = Agent.load(core_model_path, interpreter=nlu_interpreter, action_endpoint=action_endpoint)

    print("Sera is ready to talk! Type your messages here or send 'stop' to STOP!")
    while True:
        a = input()
        if a == 'stop':
            break
        responses = agent.handle_text(a)
        for response in responses:
            print(response["text"])
    return agent


if __name__ == '__main__':
    actionConfig = utils.read_yaml_file('endpoints.yml')
    # train_core('domain.yml', './models/dialogue', './data/stories.md')
    run_core('./models/dialogue', './models/nlu/default/weathernlu',
             actionConfig["action_endpoint"]["url"])
