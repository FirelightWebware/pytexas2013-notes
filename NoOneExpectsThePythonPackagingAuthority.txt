# Talk: Nobody Expects the Python Packaging Authority
_Speaker: Nick Coghlan_

@ncoghlan_dev

- cpython core developer since 2005
- nominated member of the PSF
- Red Hat toolsmith

## Intro

15 years of python packaging -- it's old
- distutils was added in 1998 by someone who had only known python for 3 months
- core devs have learned a lot since then
- setuptools and easy_install 2004
- [missed one]
- pip 2008
- distribute fork 2009

virtualenv and pip solved a lot of problems by keeping 'em separated

## Where do we want to be?

Want to make it easy for people to get started. Recommended best practices. Clear instructions. 

On the backend we want the tools to be fast, reliable, secure (reasonably). Want to interoperate with other packaging systems.

### Why don't we have that

Well, who gets to be the authority? Which tools do they use? Where do they document it?

PEP doesn't work well for stuff outside the standard library. Earlier this year they tweaked the PEP process so they can see stuff work outside the standard library first, then pull it in when they see it works. "Ecosystem first, standard library later"

## setuptools vs distribute

An old debate? setuptools development was a closed process, too hard to contribute. So the distribute fork was born. Installing distribute got you setuptools and it was very confusing.

Earlier this year setuptools and distribute merged back together. Now we can just say "Use setuptools". setuptools 0.8+

### pip vs easy_install

easy_install comes with setuptools by default. setuptools's bad press was due to easy_install. Benefits of pip were pip's defaults made more sense. However pip had limitations, particularly binary egg format. But then, earlier this year, we got wheels. So now the latest version of pip can do binary installs. (How do I do this with meme?)

pip 1.4+ should be able to do everything that easy_install used to do.


## Who should newcomers believe? How do they know what's right?

The Python Packaging Authority! (PyPA)

They are working on a Python Packaging user guide. Once that stabilizes the standard library docs will be updated. It's still be worked on. Near term they are trying to fix the instructions on… [pip?]

## The "Science!" Exception

They have really hard tools to install [you may have noticed], and hard work to do. Their build dependencies are very complex. Not all their dependencies are open source. The naming conventions don't work for their software.

Being able to exactly reproduce a scientific stack is very important. They are going their own way. They have their own ecosystem, and almost like their own package manager. If you're doing scientific stuff look into Anaconda stuff, [other stuff I missed].

It's been decided that it's better for them to have different tools.

They need a cross-platform solution. They don't want to rely on system package managers.

## How do we make it easy for people to get started

Put pip in the standard library? Yes! Goal for 3.4! [awesome]

But the challenge is, pip needs to be able to upgrade itself, i.e., not owned by system package manager.

Once pip is installed, you can use it to bootstrap anything else.

## Goal 3: Fast, Reliable, (reasonably) Secure

### What prevents fast distribution?

The mirror autodiscovery system is actually quite complicated. Also there is a very strange scanning mechanism where stuff could be stored elsewhere, and it's slow. It's slow to find out what dependencies something has. The index service doesn't expose the metadata.

The Fastly CDN (donated to community) will make it faster, magically. [?]

Eliminate scanning of external links -- can't just turn it off or things will break. A PEP proposes turning it off by default and having to "opt-in". This won't work right away though, so someone has gone through and notified all projects that can turn off external links so they can update.

Binary distribution (wheel support) with pip will help speed things up. With the wheel format you can tell pip to cache the built wheel files locally. If the package author has uploaded the wheel files in the first place you can download that [instead of the whole source?]. [I don't really understand this part]

New metadata (PEP 426 & 440). -- longer term project

## What prevents reliable distribution?

External hosting and mirroring was unreliable. So hosting has been relocated to OSU/OSL [?]. Making it faster and more reliable. The CDN is set up so that even if the master server goes down it will serve stale data until it's back up.

Autodiscovery of mirrors is fundamentally unstable and insecure.

There is no SLA for PyPI, so mirrors are not going away, and support for mirrors is not going away.

You should be able to run your own cache for your projects, and fallback to PyPI.

## What prevents (reasonably) secure distribution?

Improvements:

- force https by default
- pip verifies SSL

Can PyPI mirrors be trusted? You should only talk to mirrors over https.

Can PyPI be trusted? There's no signing yet. They try to operate in a trustworthy manner, but mistakes have been made.

If you can, set up a private mirror. Audit your dependencies.

## Goal 4: Better platform interoperability

Cross platform tools rock! Language neutral tools rock! We want to support with. This is one of the things working toward with the Metadata 2.0 project.

## Questions

### Wheels vs eggs?

Eggs don't play nice with system package managers. Wheel files are named better so you can tell what platform it's for.

### When metadata publishing on PyPI?

Guessing, early to mid 2014.

## Reference

Presentation source: bitbucket.org/ncoghlan/misc/src/default/talks


