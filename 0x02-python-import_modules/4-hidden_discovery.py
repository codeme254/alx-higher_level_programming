#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for name in range(0, len(names)):
        if names[name][0] != "_" and names[name][1] != "_":
            print(names[name])
