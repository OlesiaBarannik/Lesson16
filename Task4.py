class CustomException(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

        with open("logs.txt", "a+") as logger:
            logger.write(self.error_message + "\n")

def get_category(foo_dict: dict, key: str):
    try:
        return foo_dict[key]
    except KeyError as key:
        error_message = f"You don't have key {key} in you dict"
        raise CustomException(error_message)

foo_dict = {"Food": ["Rastishka", "Ramen"], "Milk": ["Galichina"]}

get_category(foo_dict, "Loop")