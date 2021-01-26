
import mhtifier
import os
from pathlib import Path

def main():

    mht_root_path = '/media/m/KINGSTON/WorkStuffs/Notebooks/Exports_mht/'
    html_root_path = '/media/m/KINGSTON/WorkStuffs/Notebooks/Exports_html'

    for (dirpath, dirnames, filenames) in os.walk(mht_root_path):
        sub_path = dirpath.split('Exports_mht')[1]
        html_path = html_root_path + sub_path
        try:
            os.mkdir(html_path)
        except FileExistsError:
            pass

        for filename in filenames:
            if filename.endswith('mht'):
                mht_filepath = os.path.join(dirpath, filename)
                name = Path(filename).stem + '.html'
                html_filepath = os.path.join(html_path, name)
                print(mht_filepath)
                print(html_filepath)
                mhtifier.unpack(mht_filepath, html_filepath)
                #inp = input('>>>')




if __name__ == "__main__":
    main()
