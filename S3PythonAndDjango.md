# Talk: S3 Python & Django
_Speaker: Eloy Zuniga (gh: eloyz)_

Basic understanding of using Python and Django with S3

## First

`pip install boto` <-- the python package that amazon in using for all it's services

    from boto.s3.connection import S3Connection
    # conn = S3Connection(anon=True) # for public buckets
    conn = S3Connection('<aws access key>', '<aws secret key>')
    buckets = conn.get_all_buckets()
    len(buckets)
    bucket = conn.get_bucket('mybucket')
    bucket.name
    
    bucket = conn.create_bucket('someuniquebucketname') 
    bucket.list() # BucketListResultSet instance
    
    for b in bucket.list():
        print b # <Key: bucketname,path/to/item.txt>
        
    from boto.s3.key import Key
    key = Key(bucket) # <Key: bucketname,None>
    key.key = "/a/b/c/d/img.png"
    key.set_contents_from_string('this is not a png!') # returns byte size of file
    key.get_contents_as_string()
    key.delete()
    
Remember there are no folders. Keys have slashes only for the convenience of GUIs. Nothing actually exists at "/a/b/c".

boto.s3.amazonaws.com <-- good, but incomplete, documentation

    * set_contents_from_file
    * set_contents_from_filename
    * set_contents_from_stream
    
    
    conn.get_all_buckets() # gives you a nice list
    
You can manage the ACL with the boto api:

    acp = bucket.get_acl()
    for grant in acp.acl.grants:
        print grant.permission, grant.grantee
        
You can set and get metadata too.

For Django you can use S3BotoStorage.

Check out the free app 3Hub in the App Store. You can do a lot of S3 operations with it.

    