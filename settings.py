class Config:

    @property
    def db_url(self):
        return f'sqlite:///test.db'


proj_conf = Config()
