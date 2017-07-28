import sys



relaxed_lower_dedupe_f = sys.argv[1]
incall_data_140_f = sys.argv[2]
relaxed_lower_dedupe_incall_f = sys.argv[3]

# relaxed_lower_dedupe_f = 'relaxed_lower_dedup.txt'
# incall_data_140_f= 'test_dataset_140.txt'
# relaxed_lower_dedupe_incall_f = 'relaxed_lower_dedupe_incall.txt'


def find_subset(line_sub, incall_data_140_f):
    incall_data_140 = open(incall_data_140_f, 'r').read().splitlines()
    test_text = []
    for line in incall_data_140:
        test_text.append((line.lower()).strip())

    for i in test_text:
        if i == line_sub:
            print i
            print line_sub
            return True
    open(incall_data_140_f, 'r').close()
    return False

relaxed_lower_dedupe = open(relaxed_lower_dedupe_f,'r').read().splitlines()
relaxed_text = []
for line in relaxed_lower_dedupe:
    relaxed_text.append(line.strip())
open(relaxed_lower_dedupe_f,'r').close()

relaxed_lower_dedupe_remove = open(relaxed_lower_dedupe_incall_f, 'w')

for line in relaxed_text:
    if not find_subset(line, incall_data_140_f):
        relaxed_lower_dedupe_remove.write('%s\n' % line.strip())
open(relaxed_lower_dedupe_incall_f, 'w').close()


