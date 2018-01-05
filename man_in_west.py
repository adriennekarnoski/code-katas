"""Man in the west

Check if there is gold in the bucket,
and if so, return True/true. If not, return False/false

#1 Best Practices Solution by smile67 (plus 106 more warriors):

def check_the_bucket(bucket):
    return 'gold' in bucket

"""


def check_the_bucket(bucket):
    """checks bucket, returns true or false."""
    if 'gold' in bucket:
        return True
    else:
        return False
