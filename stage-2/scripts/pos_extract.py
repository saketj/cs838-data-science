import csv
import re
import glob
import sys

argv = sys.argv[1:]
if len(argv) < 2:
    sys.stderr.write("Incorrect arguments. Expecting two arguments: <input_files> <output_file>\n")
    sys.exit(-1)

pos_list = [['file name','start offset','end offset','dish name']] # A list for all positive examples
path = argv[0]
# path = './datasets/Set_I_DEV/*.txt'
# path = '../datasets/text-documents-labeled_TEST/*.txt'
files = glob.glob(path)
# iterate over files in the directory
for fle in files:
   # opening the file and reading it as a string
   with open(fle) as f:
      text = f.read()
      match = re.compile('<dish>(.*?)</dish>', re.DOTALL).finditer(text)
      for l in match:
          pos_list.append([f.name,l.start(),l.end(),l.group(1)])

# Writing output to csv
with open(argv[1], "wb") as f:
    writer = csv.writer(f)
    writer.writerows(pos_list)
