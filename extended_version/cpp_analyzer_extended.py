def get_values(arg_type):
    base_type = arg_type.replace('&','').replace('const', '').strip()