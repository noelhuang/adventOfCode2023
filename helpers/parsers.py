def parse_txt_as_string(filepath, mode='r'):
    """
    Parses txt file specified in filepath and returns contents as string
    :param filepath:
    :param mode:
    :return:
    """
    with open(filepath, mode) as f:
        my_data = f.read()
    return my_data
