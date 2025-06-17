def bytes_to_MB(bytes: int) -> float :
    file_size = bytes / 1024 / 1024
    return round(file_size, 2)
