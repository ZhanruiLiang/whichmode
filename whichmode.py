from __future__ import print_function
import sys
import readline
keyboard = 'wbwbwwbwbwbw'
pitches = ['C', '#C', 'D', '#D', 'E', 'F', '#F', 'G', '#G', 'A', '#A', 'B']
mainPitchPositions = [0, 2, 4, 5, 7, 9, 11]
T = 12

def get_mode(modeName):
    i0 = pitches.index(modeName)
    mode = []
    for i in mainPitchPositions:
        mode.append(pitches[(i0 + i) % len(pitches)])
    return mode

def get_sharps(mode):
    return [x for x in mode if x[0] == '#']

def search_mode(sharps, top=1):
    def estimate(mode):
        sharps1 = set(get_sharps(mode))
        return (len(sharps.difference(sharps1)), 
            len(sharps1.difference(sharps)))
    sharps = set(sharps)
    if top == 1:
        result = min(modes, key=estimate)
    else:
        result = list(sorted(modes, key=estimate))[:top]
    return result

def validate_sharps(sharps):
    for x in sharps:
        if x not in pitches:
            return x
    return None

modes = [get_mode(p) for p in pitches]

# print(get_mode('C'))
# print(search_mode(['#F']))
def process(sharps):
    invalid = validate_sharps(sharps)
    if invalid:
        print('invalid:', invalid)
    else:
        mode = search_mode(sharps)
        print(mode)

if __name__ == '__main__':
    if len(sys.argv) >= 1:
        process(sys.argv[1:])
    else:
        current = ''
        quit = False
        readline.set_startup_hook(lambda: readline.insert_text(current))
        while not quit:
            try:
                current = raw_input('Sharps: ')
            except KeyboardInterrupt:
                quit = True
                break
            sep = ' ' if ',' not in current else ','
            sharps = current.split(sep)
            process(sharps)
