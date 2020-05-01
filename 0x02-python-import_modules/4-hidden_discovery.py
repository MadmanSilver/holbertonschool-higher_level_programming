#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for ob in dir(hidden_4):
        if ob[0:2] != '__':
            print(ob)
