import os
import uuid
from itertools import permutations

from django.utils.text import slugify


def generate_datafile(keywords, answers):
    """
    :param keywords: A list of keyword lists which will be converted to questions. Format: [(k1, k2), (k3)]
    :param answers: A list of strings. Each one of them evaluated as an answer for the question.
    :return:
    """
    file_path = "/tmp/rivescript/{}.rive".format(slugify(str(uuid.uuid4())))

    # Create the temporary directory if it is not exist
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError:
            return None

    file = open(file_path, 'w')

    # Find all combinations of the given keywords
    for p_keys in permutations(keywords):
        p_keys = list(p_keys)

        # Generate questions and print them to the file
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

        # Print the answers under each question
        for i in range(len(answers)):
            file.write("- " + answers[i] + "\n")

        file.write("\n")

    return file_path

