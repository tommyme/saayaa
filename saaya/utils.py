def strip(fp):
    return '.'.join(fp.split('.')[:-1])


def FingerPrints(fp):
    fps = []
    while(fp != ''):
        fps.append(fp)
        fp = strip(fp)
    return fps
