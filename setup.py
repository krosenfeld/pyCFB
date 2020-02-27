from setuptools import setup
setup(
    name="pyCFB",
    version="0.0.1",
    author="Katherine Rosenfeld",
    author_email="krosenf@gmail.com",
    url="https://github.com/krosenfeld/pyCFB",
    description="Python implementaion of Coffrey-Feingold-Bromberg (CFB) metric",
    keywords=["CFB"],
    classifiers= [
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
         "Programming Language :: Python :: 3.6"
        ],
    packages=["pyCFB"],
    install_requires=['numpy', 'nose'],
    test_suite='nose.collector',
    tests_require=['nose']
)