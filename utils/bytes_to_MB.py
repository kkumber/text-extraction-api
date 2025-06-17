def bytes_to_MB(bytes: int) -> float :
    file_size = bytes / 1048576
    return round(file_size, 2)
