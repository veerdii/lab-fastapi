from functools import lru_cache

@lru_cache()
def get_dict():
    return config.Settings()