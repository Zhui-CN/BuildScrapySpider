from setuptools import setup, find_packages

setup(
    name='buildspider',
    version="1.0",
    description='Build Scrapy Spider',
    packages=find_packages(exclude=[]),
    author='Zhui',
    author_email='asd4988@qq.com',
    license='MIT',
    package_data={'': ['*.*']},
    url='#',
    zip_safe=False,
    entry_points={
        'console_scripts': ['build = buildspider.cmd:cmd']
    },
    install_requires=[
        'scrapy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
