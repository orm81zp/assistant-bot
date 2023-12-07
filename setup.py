from setuptools import setup, find_namespace_packages


def get_long_description():
    """
    Return the README.
    """
    with open("README.md", encoding="utf8") as fh:
        return fh.read()


setup(
    name='goit-assistant-bot',
    version='0.0.1',
    description='A personal console bot assistant that helps you manage your contacts and notes.',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/orm81zp/goit-assistant-bot',
    author='Roman',
    author_email='orm81zp@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    classifiers=[
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    entry_points={'console_scripts': ['run_bot = goit_assistant_bot.bot:run_bot']},
    install_requires=['colorama', "prettytable"],
)
