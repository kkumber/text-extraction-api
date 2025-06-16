import filetype

def get_mime_type(file: bytes) -> str:
    file_type = filetype.guess(file)
    if file_type is None:
        return 'unknown'
    
    return file_type.mime