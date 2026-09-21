def clean_name(name):

    if not name:
        return None
    else:
        cleaned=name.strip().lower()
        return cleaned




cln_name=clean_name("")
print(cln_name)