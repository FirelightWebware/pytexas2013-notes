# Talk: Build Your Infrastructure - with Python!
_Speaker: Ed Leafe_

How do you keep all your app servers in sync? "I'm a software developer, I don't like dealing with hardware."

To the cloud! -- provision and configure hardware in advance and allocate resources dynamically -- **programmatically**.

APIs! Oh so tedious… enter the SDK -- pyrax -- they python SDK for OpenStack-based Clouds, and fully supported by Rackspace.

```python
    import pyrax
    import pyrax.utils as utils
    import pyrax.exceptions as exc
    
    pyrax.keyring_auth()
    # or
    pyrax.set_credential_file("/path/to/file")
    # or
    pyrax.set_credentials(username, password)
```

Ex. configuration file:

```ini
    [default]
    identity_type = rackspace
    keyring_username = myuser
    region = SYD
    custom_user_agent =
    debug = False
    verify_ssl = False
    
    [devstack]
    identity_type = keystone
    region = RegionOne
    custom_user_agent =
    debug = True
    auth_endpoint = http://...
    tenant_name = demo
    tenant_id = abcde…
    keyring_username = demo
```

You can use pyrax to:

- provision an instance for your db, create a database and database user
- create an isolated network
- define a public key
- snapshot a server [?]
- create multiple application servers from a single preconfigured image
- create a load balancer
- configure the DNS
- and more… 

Use `utils.wait_for_build(instance)` after creating an instance before doing anything else.
    
A script gluing it all together in order is available at: https://github.com/EdLeafe/pytexas2013/blob/master/pytexas.py


## Reference

https://github.com/rackspace/pyrax  
http://docs.rackspace.com/  
http://api.openstack.org/  

### Speaker

@EdLeafe or +EdLeafe  
ed.leafe@rackspace.com or ed@openstack.org   
Python developer for Rackspace. Has worked on OpenStack since before it was OpenStack. 