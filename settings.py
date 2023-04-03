class Config:

    @property
    def db_url(self):
        return f'sqlite:///proj.db'


proj_conf = Config()
