from setuptools import setup, find_packages

setup(
    name='python-project-inflater',
    version='0.3',
    description='Simple tool for seeding basic python project',
    url='https://github.com/Ziqul/python-project-inflater.git',
    author='Maxim Sorokin',
    author_email='m.s.v.00a@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={
        'inflate.resources': [
            'sample_readme.md',
            '.gitignore_sample'
        ]
    },
    include_package_data=True,
    scripts=[
        './bin/inflate',
        './bin/inflate.bat'
    ],
    zip_safe=False)
