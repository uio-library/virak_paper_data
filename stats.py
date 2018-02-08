from __future__ import print_function
from collections import Counter
import pandas as pd
import numpy as np


def parse(filename, cols):
    # Returns a list of queries

    df = pd.read_csv(filename, sep=',', encoding='utf-8',
                     usecols=cols.keys(), dtype=cols, keep_default_na=False)
    query_col = 'search string cleaned'
    queries = []
    n = 0
    for idx, row in df.iterrows():
        n += 1
        for _ in range(row['searches']):
            queries.append(row[query_col])
    print('%s: Read %d rows' % (filename, n))
    return queries


def print_stats(qr):
    qd = set(qr)

    nchars_qr = np.array([len(x) for x in qr])
    nchars_qd = np.array([len(x) for x in qd])

    nwords_qr = np.array([len(x.split()) for x in qr])
    nwords_qd = np.array([len(x.split()) for x in qd])

    print('- number of queries: %d' % len(qr))
    print('  - mean number of words: %.2f' % np.mean(nwords_qr))
    print('  - median number of words: %.2f' % np.median(nwords_qr))
    print('  - mean number of chars: %.2f' % np.mean(nchars_qr))
    print('  - median number of chars: %.2f' % np.median(nchars_qr))

    print('- number of distinct queries: %d' % len(qd))
    print('  - mean number of words: %.2f' % np.mean(nwords_qd))
    print('  - median number of words: %.2f' % np.median(nwords_qd))
    print('  - mean number of chars: %.2f' % np.mean(nchars_qd))
    print('  - median number of chars: %.2f' % np.median(nchars_qd))


# Zero result queries set
print_stats(parse('zero.csv', {
        'searches': np.int32,
        'search string cleaned': np.unicode,
    }))

# Popular queries set
print()
qr = parse('popular.csv', {
        'searches': np.int32,
        'search string cleaned': np.unicode,
    })
print_stats(qr)

# Find top 50 queries overall in the popular queries set

print()
qr_c = [[k, v] for k, v in Counter(qr).items()]
keys = [x[0] for x in qr_c]
counts = np.array([x[1] for x in qr_c], dtype=np.int32)
top50_idx = (np.argsort(counts)[-50:])[::-1]

for i, n in enumerate(top50_idx):
    print('%d. %s (%d)' % (i + 1, keys[n], counts[n]))
