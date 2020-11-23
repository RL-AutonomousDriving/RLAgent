from setuptools import setup, find_packages

setup(
    name='RLAgent',
    version='1.0.dev0',
    description='A collection of Reinforcement Learning agents',
    url='https://github.com/RL-AutonomousDriving/RLAgent',
    author='Vignesh Kumar Thangarajan',
    author_email='vigneshkumar.thangarajan@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Researchers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='reinforcement learning agents',
    packages=find_packages(exclude=['docs', 'scripts', 'tests*']),
    install_requires=['gym', 'numpy', 'pandas', 'numba', 'pygame', 'matplotlib', 'seaborn', 'six', 'docopt',
                      'torch>=1.2.0', 'tensorboardX'],
    tests_require=['pytest'],
    extras_require={
        'dev': ['scipy'],
    },
    entry_points={
        'console_scripts': [],
    },
)

