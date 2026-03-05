from setuptools import setup, find_packages

HYPHON_E_DOT='-e .'
def get_requirements(file_path):
    '''
    This function reads the requirements from the specified file and returns a list of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)  
    return requirements 
    
setup(
    name="mlproject",
    version="0.1.0",
    author="Harsh Singh",
    description="A machine learning project package",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires=">=3.8",
)
