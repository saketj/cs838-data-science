import csv
import re
import glob

pos_list = [['file name','start offset','end offset','dish name']] # A list for all positive examples
path = './Debugging_stage/Set_Q/*.txt'
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
with open("./Debugging_stage/debug_posextracted_Q.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(pos_list)
