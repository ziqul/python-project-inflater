from setuptools import setup, find_packages

setup(
    name='python-project-inflater',
    version='0.2',
    description='Simple tool for seeding basic python project',
    url='https://github.com/Ziqul/python-project-inflater.git',
    author='Maxim Sorokin',
    author_email='m.s.v.00a@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={
        'inflate.resources': [
            '.gitignore_sample',
            'sample_readme.md'
        ]
    },
    include_package_data=True,
    scripts=['bin/inflate'],
    zip_safe=False)
