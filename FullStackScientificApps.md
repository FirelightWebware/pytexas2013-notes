# Talk: Building full-stack scientific applications in Python
_Speaker: Luke Lee_

## Why Python?

* python is big in the scientific community
* python works well with other "fast" languages - flexibility
* works with other virtual machines/platforms
* has good packaging tools for easy deployment 

## What tools are available?

- number crunching: ipython, numpy, pandas, scipy, pytables
- visualization: pyqt/pyqwt, matplotlib, vtk, mayavi
  - matplotlib is a good starting tool, but not suitable for advanced use
- location: esri (arcpy/geoprocessing)
  - esri has adopted python as their scripting language for arcpy
  
## Building an app

Model: HDF5/PyTables  
View: PyQt/PyQwt  
Controller: NumPy/Pandas/Scipy  

### Model

HDF5 is a binary file format built for scientific data, designed for big data. It's portable and easy to discover/crawl the structure to figure it out on the fly instead of defining it beforehand. It has fast parallel/random access. It's  hierarchical (think dirs) as opposed to relational. The format is portable so you can read it with other languages when Python isn't the right tool for the job.

PyTables you can think of as an ORM for your HDF5 file. It uses NumPy to boost performance - you can tell it to bring the data directly into a NumPy array without creating an intermediate list.

When PyTables is overkill, you can use h5py.

```python
    for row in ro.where('pressure > 10'):
        print row['energy']
```

### View

PyQt is Python binding to Qt toolkit. Qt runs on any platform and provides a lot of generic UI widgets. In addition to GUI stuff, you can do networking, XML, SQL, etc with Qt.

There's also Pyside which matches the PyQt api so you can switch it out.

PyQwt is for plotting (for science/engineering apps). It's smaller and faster than matplotlib. The Python docs are bad, but you can use Qwt's C++ docs.

Pyqtgraph is an alternative to PyQwt. PyQwt doesn't have a lot of active development. Pyqtgraph doesn't rely on Qwt; it's pure python with PyQt/Pyside/numpy. 

### Controller

#### Numpy

NumPy -- arrays with brains! And more! Has smart memory management and copy semantics. Has fast element-wise operations. It's used everywhere. Great building block. 

```python
    # pure python
    >>> x = range(10000)
    >>> %timeit [item + 1 for item in x]
    1000 loops, best of 3: 437 us per loop
    # numpy
    >>> x = numpy.arange(10000)
    >>> %timeit x + 1
    100000 loops, best of 3: 13.9 us per loop
```

You can think of it as outsourcing your loops to C.

```python
    >>> x = numpy.arange(3)
    >>> x
    array([0, 1, 2])
    >>> x[x > 1]
    array([2])
    >>> x > 1
    array([False, False, True], dtype=bool)
    >>> x[:2][0] = 1
    >>> x
    array([1, 1, 2])
    >>> x[x > 0][0] = 10
    >>> x
    array([1, 1, 2])
    # boolean indexing makes a copy instead of changing the original
    
    >>> rand_arr = np.random.rand(2,2)
    >>> numpy.savetxt('test.out', rand_arr, delimiter=' ', fmt='%1.5f', 
                      header='a b', comments='')

```

#### Pandas

Fast read/write for SQL dbs, CSV, HDF5. For now uses NumPy (they are discussing moving away from it). "Group by" and merge large data sets. Toolkit to unify NumPy/matplotlib. "Replacement" for R.

```python
    # pretty printing
    >>> pandas.read_csv('test.out', delim_whitespace=True)
            a       b
    0 0.98979 0.78997
    1 0.12323 0.17839
```

Pandas uses Cython to do data in/out very quickly. NumPy is not optimized for that.

#### Scipy

For stats, inegration, matrices, linear algebra, natural language processing, image processing, etc.

```python
    >>> from scipy import integrate
    >>> x2 = lambda x: x**2
    >>> integrate.quad(x2, 0., 4.)
```

### Deployment

PyInstaller -- point it at your main .py file and it will figure everything out and package it for you into an executable. It has explicit support for PyQt/Django/matplotlib. It doesn't handle dynamic imports or sys.path modifications well. It also doesn't cross-compile. www.pyinstaller.com

### References

http://bit.ly/python_science_apps -- sample projects to hack on! (there are a few bugs in there on purpose, and some github issues for them)

@durden20 / github.com/durden / http://codrspace.com/durden