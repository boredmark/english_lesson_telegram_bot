import requests
import sentences
import users


class Bot:

    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.flag_level = None

    def get_updates(self):
        url = f'https://api.telegram.org/bot{self.bot_token}/getUpdates'
        request = requests.get(url)
        return request.json()['result']

    def get_info_from_last_updates(self):
        update = self.get_updates()
        update_id = update[-1]['update_id']
        chat_id = update[-1]['message']['chat']['id']
        text = update[-1]['message']['text']
        user_id = update[-1]['message']['from']['id']
        return {'update_id': update_id,
                'chat_id': chat_id,
                'text': text,
                'user_id': user_id}

    def send_massage(self, chat_id, text):
        url = f'https://api.telegram.org/bot{self.bot_token}/sendMessage'
        requests.post(url, data={'chat_id': chat_id, 'text': text})
        return f"Massage '{text}' was sent "

    @staticmethod
    def create_string_of_sentences(word, user_level):
        result_list = []
        for i in sentences.sentences:
            if int(user_level) == i['level'] and ' ' + word.lower() + ' ' in i['text'].lower():
                result_list.append(i['text'])
        if len(result_list) == 0:
            return 'No matched sentences'
        else:
            result_string = ''
            for i in result_list:
                result_string += i+'\n' + '-------------' + '\n'
            result_string += '/commands - other commands'
            return result_string

    def process_massage(self, input_massage, user_id):
        if input_massage in ['0', '1', '2'] and self.flag_level is False:
            self.flag_level = True
            users.users[user_id] = input_massage
            massage_to_send = f'Your english level is {users.users[user_id]}!\n' \
                              f'Write english word which you want to use in sentence!\n' \
                              f'/commands - other commands'
            return massage_to_send
        if input_massage == '/start' and user_id not in users.users.keys():
            self.flag_level = False
            massage_to_send = 'Hello! ' \
                              'Wellcome to english lesson bot!\n' \
                              'Write your english level from 0 to 2!'
            return massage_to_send
        if input_massage == '/start' and user_id in users.users.keys():
            self.flag_level = True
            massage_to_send = f'Hello, your english level is {users.users[user_id]}\n' \
                              f'Write english word which you want to use in sentence\n' \
                              f'/commands - other commands'
            return massage_to_send
        if input_massage == '/level' and self.flag_level is True:
            massage_to_send = f'Your english level is {users.users[user_id]}\n' \
                              f'Write english word which you want to use in sentence\n' \
                              f'/commands - other commands'
            return massage_to_send
        if input_massage == '/change_level' and self.flag_level is True:
            self.flag_level = False
            massage_to_send = 'Write your english level from 0 to 2'
            return massage_to_send
        if input_massage == '/commands' and self.flag_level is True:
            massage_to_send = '/level - check your current level\n' \
                              '/change_level - change your level\n' \
                              '/start - start bot'
            return massage_to_send
        if self.flag_level is False:
            massage_to_send = 'Write your english level from 0 to 2'
            return massage_to_send
        else:
            massage_to_send = self.create_string_of_sentences(input_massage, users.users[user_id])
            return massage_to_send















