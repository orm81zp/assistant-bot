from setuptools import setup, find_namespace_packages


def get_long_description():
    """
    Return the README.
    """
    with open("README.md", encoding="utf8") as fh:
        return fh.read()


setup(name='assistant_bot',
    version='0.0.1',
    description='Assistant Bot',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/orm81zp/assistant_bot',
    author='Roman',
    author_email='orm81zp@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['assistant-bot = assistant_bot:run_bot']}
)
