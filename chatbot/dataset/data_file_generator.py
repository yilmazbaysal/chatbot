import os
import errno
from itertools import permutations


def add_question(filename, keywords, answers):
    filename = filename.replace(" ", "-")

    file_path = "/tmp/rivescript/" + filename + ".rive"
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    file = open(file_path, 'w+')

    for p_keys in permutations(keywords):

        p_keys = list(p_keys)

        file.write("+ ")
        for i in range(len(p_keys)):

            file.write("[*] ")
            if len(p_keys[i]) == 1:
                file.write(p_keys[i][0] + " ")
            else:
                file.write('(')

                for j in range(len(p_keys[i])):
                    file.write(p_keys[i][j])
                    if j != len(p_keys[i]) - 1:
                        file.write("|")

                file.write(') ')

            if i == len(p_keys) - 1:
                file.write("[*]\n")

        for i in range(len(answers)):

            file.write("- " + answers[i] + "\n")

        file.write("\n")
