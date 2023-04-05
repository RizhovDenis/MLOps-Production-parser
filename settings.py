class Config:

    parsing_source: str = 'https://ru.investing.com'

    @property
    def db_url(self):
        return f'sqlite:///proj.db'


proj_conf = Config()
