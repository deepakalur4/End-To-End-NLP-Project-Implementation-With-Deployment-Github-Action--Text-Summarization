import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="Text_summarizer",
    version="0.0.0.0",
    author="Deepak S Alur",
    author_email="deepaklaur4@gmail.com",
    packages=setuptools.find_packages(where="src"),
    long_description=long_description,
    long_description_content="text/mardown",
    url=f"https://github.com/deepakalur4/Text-Summarization-NLP-Project",
    package_dir={"":"src"},
    project_urls={"bug_tracker":"https://github.com/deepakalur4/Text-Summarization-NLP-Project/issues"},
    description="NLP Application"
)