import csv
import re
import glob
import random
import sys

argv = sys.argv[1:]
if len(argv) < 2:
    sys.stderr.write("Incorrect arguments. Expecting two arguments: <input_files> <output_file>\n")
    sys.exit(-1)


# removes the lines containing the patterns in the given string
def remove(pattern,string_given):
    return re.sub(".*"+pattern+".*\n?","",string_given)


def remove_dish_labels(text):
    lines = text.split(".")
    extracted = ""
    for line in lines:
        if "<dish>" not in line:
            extracted += (line + ".")
    extracted = re.sub(r"\n", "", extracted)
    return extracted


threshold = 8 # Number of negative samples divided by 3 per file
neg_list = [['file name','start offset','end offset','negative sample']] # A list for all positive examples
path = argv[0]
# path = '../datasets/text-documents-labeled_TEST/*.txt'
files = glob.glob(path)

# iterate over files in the directory
for fle in files:

   # opening the file and reading it as a string
   with open(fle) as f:
      text = f.read()
      
      # Removing all the lines containing dishes
      text_new = remove_dish_labels(text) #remove("</dish>",remove("<dish>",text))

      # Generating three consecutive word matches in the new file
      match_raw = re.compile('([A-Za-z]+ )([A-Za-z]+ ([A-Za-z]+))', re.DOTALL).finditer(text_new)
      i = 1

      # Storing the matches as a list
      if match_raw:
          match_new = []
          for m in match_raw:
                match_new.append(m)
    
      # Random shuffling of the matches
      random.shuffle(match_new)
      for l in match_new:
          # print(i)
          # Finding the offset of the match in the original list
          match0 = re.search(l.group(0),text)
          if match0 is None:
              continue
          neg_list.append([f.name,match0.start(),match0.end(),match0.group(0)])
          match1 = re.search(l.group(1),text)
          neg_list.append([f.name,match1.start(),match1.end(),match1.group(0)])
          match2 = re.search(l.group(2),text)
          neg_list.append([f.name,match2.start(),match2.end(),match2.group(0)])
          i = i + 1
          if(i > threshold):
              break

# Writing output to csv
with open(argv[1], "wb") as f:
    writer = csv.writer(f)
    writer.writerows(neg_list)

