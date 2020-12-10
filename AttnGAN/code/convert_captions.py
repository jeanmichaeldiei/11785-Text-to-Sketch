
# Python code to 
# demonstrate readlines() 
  
# Using readlines() 
file1 = open('../data/CelebA/captions.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines: 
    # writing to file 
    file2 = open('../data/CelebA/sketch_texts/captions_{}.txt'.format(count), 'w')
    file2.truncate(0)
    file2.writelines(line.strip()) 
    file2.close() 
    count += 1
file1.close()
print(count)

file3 = open('../data/CelebA/example_filenames.txt', 'w') 
file3.truncate(0)
for i in range(count):
    file3.writelines('sketch_texts/captions_{}\n'.format(i)) 
file3.close()




# Add test files to example_filenames.txt
test = np.load("../data/CelebA/test/filenames.pickle", allow_pickle = True)
print(type(test))
print(len(test))
test = np.array(test[:200]).astype(str)

# Using readlines() 
file3 = open('../data/CelebA/example_filenames.txt', 'w') 
file3.truncate(0)
for f in test:
    folder = f[:-4]
    file3.writelines('text/{}/{}\n'.format(folder,f)) 
file3.close()