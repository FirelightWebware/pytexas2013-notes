# Talk: dtrace, Python and You
_Speaker: Mark Allen / mrallen1@yahoo.com / @bytemeorg / http://byte-me.org / github:mrallen1_

## What is DTrace?

Focused on dynamic tracing (as opposed to static tracing). No more `print "got here!"`!

DTrace can help you examine everything from application code all the way down to the kernel.

Examples:

- Trace socket accepts and debug your web application's "real" code execution pathway
- Profile why NFS gets super busy at 0430 and a directory tree traversal takes 2 hours instead of 2 minutes

Use dtrace with a profiler, and with a debugger, not instead of one. Dtrace only runs on a few OSes, including FreeBSD and OSX (as of mountain lion). What about linux? There's a dtrace4linux, but only supports kernel-level tracing. Don't install the dtrace you find for Ubuntu… it's not safe in a production environment.

## DTrace Terms

- Provider: manages probes in a subsystem, ex. the python binary itself
- Probes: DTrace instrumentation or "observables" [?]
- Consumer: a user-mode program that calls into DTrace, ex. a D script

Dtrace has it's own scripting language called "D".

## D Language

An awk-like scripting language. Define a probe, optional predicate, and optional actions. Supports `BEGIN` and `END` blocks, local variables, aggregate/associative variables (prefixed with '@').

`dtrace -n 'probe /predicate/ {action}'`

```
    $ cat subentry.d
    
    #!/usr/sbin/dtrace -qFZs
    
    function-entry,
    function-return
    {
        /* arg1 is a subroutine name */
        trace(copyinstr(arg1))
    }
```

function-entry and function-return are python-specific probes.

```
    function-entry
    {
        /* Count sub entries by package and sub name
         * arg0 = source file name
         * arg1 = function name */
        @[strjoin(strjoin(copyinstr(arg0), "-"), copinstr(arg1))] = count()
    }
    
    END
    {
        /* Give me the top 10 highest counts, throw away rest */
        trunc(@, 10)
    }
```

### Aggregate Functions

avg, count, sum, min, max, lquantize (linear), and quantize (log - power of 2)

These operate on what the '@' symbol is in front of. The quantize functions give you histograms so you can see outliers, which avg wouldn't give you.

## DTrace and Python

Python is one of the few programming languages that doesn't come with dtrace support out of the box. So you have to `brew install python --with-dtrace`.

## Python Probes

- function-entry
- function-return
- line (FILE, FUNCTION, LINE)
- gc-start (GENERATION) (similar to gc.collect())
- gc-done (OBJECTS-COLLECTED)
- instance-new-start, 
  instance-new-done, 
  instance-delete-start, 
  instance-delete-done (CLASS_NAME, FILE)
  
_in parentheses is args for that probe, i.e. (arg0, …)_

You can make your own DTrace probes _in Python_ by using: http://tmetsch.github.io/python-dtrace (also avail. on PyPI).

## Resources

- http://dtracehol.com/#Intro -- 'hol' stands for hands-on lab. Here you can get download a vbox and go through step-by-step exercises to learn dtrace.
- http://dtrace.org/guide/preface.html -- personal website/blog for a bunch of the people who created dtrace
- http://www.amazon.com/dp/0132091518 -- the dtrace book
- http://dtracebook.com/index.php/Languages#Python -- all the dscripts from the book (the book is not available online)
