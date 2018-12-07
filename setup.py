from setuptools import setup

setup(
    name="masonite-cloudinary-driver",
    packages=[
        'masonite.contrib.cloudinary',
        'masonite.contrib.cloudinary.drivers',
        'masonite.contrib.cloudinary.providers',
    ],
    version='1.0.0',
    install_requires=[
        'cloudinary',
    ],
    classifiers=[],
    author='Vaibhav Mule',
    author_email='vaibhavmule135@gmail.com',
    url='https://github.com/vaibhavmule/masonite-cloudinary-driver',
    description='Cloudinary Upload Driver for the Masonite framework',
    keywords=['python web framework', 'python3', 'masonite', 'cloudinary'],
    include_package_data=True,
)