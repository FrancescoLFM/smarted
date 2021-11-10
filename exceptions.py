class InvalidArgumentsError(Exception):
    def __init__(self, message="Invalid Arguments"):
        self.message = message
        super().__init__(message)
    
    def __str__(self):
        return f"{self.message}"

class CommandError(Exception):
    def __init__(self, message = "Unknown command"):
        super().__init__(message)

class InvalidLine(Exception):
    def __init__(self, message = None):
        super().__init__(message)

class LanguageNotSupported(Exception):
    def __init__(self, lang = None):
        message = f"Language not supported yet: {lang}"
        super().__init__(message)