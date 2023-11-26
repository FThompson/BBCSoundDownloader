import csv
import encodings.idna  # avoid encoding error in distributable
import os
import re
import shutil
import sys
import urllib.request
from multiprocessing.pool import ThreadPool
from pathlib import Path

THREAD_COUNT = 10
MAX_FILENAME_LENGTH = 143  # this is the max with ecryptfs, but most systems are 255 chars max


class Downloader:
    def __init__(self, thread_count=THREAD_COUNT):
        self.thread_count = thread_count
        self.samples = self.get_samples()
        self.total_count = len(self.samples)
        self.finished = 0
        self.failed = 0

    def download_all(self):
        print('Downloading %s samples' % self.total_count)
        results = ThreadPool(self.thread_count).map(self.download, self.samples)
        print('Execution completed, reporting failures:')
        for success, filepath, e in results:
            if not success:
                print('%s failed with exception: %s' % (filepath, e))
        print('%d failures reported.' % self.failed)

    def download(self, sample):
        url, filepath = sample
        print('Starting %s => %s' % (url, filepath))
        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            temp_path, headers = urllib.request.urlretrieve(url)
            shutil.move(temp_path, filepath)
            self.finished += 1
            print('(%d/%d) Finished %s' % (self.finished, self.total_count, str(filepath)))
            return True, None, None
        except Exception as e:
            self.failed += 1
            print('FAILED ' + str(filepath), file=sys.stderr)
            print(e, file=sys.stderr)
            print('%d failed download attempts' % self.failed, file=sys.stderr)
            return False, filepath, e

    def get_samples(self):
        samples = []
        csv_path = os.path.join(os.path.dirname(__file__), 'BBCSoundEffects.csv')
        with open(csv_path, encoding='utf8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                folder = self.sanitize_path(row['CDName'])
                suffix = '.' + row['location']
                max_description_length = MAX_FILENAME_LENGTH - len(suffix)
                filename = self.sanitize_path(row['description'])[:max_description_length] + suffix
                filepath = Path('sounds') / folder / filename
                if not filepath.exists():
                    url = 'https://sound-effects-media.bbcrewind.co.uk/wav/' + row['location']
                    samples.append((url, filepath))
        return samples

    def sanitize_path(self, path):
        return re.sub(r'[^\w\-&,()\. ]', '_', path).strip()


if __name__ == "__main__":
    Downloader().download_all()
