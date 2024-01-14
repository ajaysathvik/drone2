from setuptools import setup

setup(
    name='Drone-pilot',
    version='1.0.0',
    author='Ajay Sathvik',
    author_email='ajaysathvikk@example.com',
    description='A simple drone pilot',
    packages=['drone-pilot'],
    install_requires=[
        'dronekit',
        'eel',
        'pymavlink',
        'matplotlib',
        'cv2',
        'time',
    ],
)
