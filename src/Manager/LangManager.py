# Manager/LangManager.py

class LangManager:
    default_lang = ''

    def get_defalut_lang(self, config_path = 'config/config.json'):     #从config.json里面读取默认语言
        with open(config_path, 'r') as f:
            config = json.load(f)
            self.default_lang = config['default-lang']

    def __init__(self):
        get_defalut_lang()

    
