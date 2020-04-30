#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as module_file
    all_modules = dir(module_file)
    for i in range(0, len(all_modules)):
        if (all_modules[i][0] != '_'):
            print(all_modules[i])
