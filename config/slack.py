from slacker import Slacker

class Slack():
    def __init__(self):
        self.token = 'xoxe.xoxp-1-Mi0yLTQwMDA2NjMwNzAzOTEtNDAyNzg1NTQ4NzkyMS00MDE1MTYzNTI3Mzc5LTQwMjc4OTUxODk4MjUtYmQwNGFmMjI4NzU2ZDFkZGM0MDZjOWRjNDlmM2VmZDg5NTAyOTNlYjZlY2Q4MzE1N2RhMTMxN2U5YzI2ZjkzZA'

    def notification(self, pretext=None, title=None, fallback=None, text=None):
        attachments_dict = dict()
        attachments_dict['pretext'] = pretext  # test1
        attachments_dict['title'] = title  # test2
        attachments_dict['fallback'] = fallback  # test3
        attachments_dict['text'] = text  # test4

        attachments = [attachments_dict]

        slack = Slacker(self.token)
        slack.chat.post_message(channel='#realmessage', text=None, attachments=attachments, as_user=None)