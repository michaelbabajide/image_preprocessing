import os
import string
from os import listdir


def image_labels(image_dir):
    """
    Creates a dictionary of image labels based upon the filenames 
    of the image files.
    Parameters:
     image_dir - The (full) path to the folder of images 

    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as image label
    """
    # Get the path of current working directory
    in_files = listdir(image_dir)

    # Define a translation table to replace special characters with spaces
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        
    results_dic = {}
    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            filename = os.path.splitext(in_files[idx])[0]
            filename = filename.translate(translator)
            filename = ''.join((x for x in filename if not x.isdigit()))
            image_label = filename.lower().rstrip(' ')

            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [image_label]
            else:
                print("** Warning: Duplicate files exist in directory:", in_files[idx])

    return results_dic
