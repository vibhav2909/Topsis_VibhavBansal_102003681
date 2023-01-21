from distutils.core import setup
setup(
  name = 'Topsis_VibhavBansal_102003681',         # How you named your package folder (MyLib)
  packages = ['Topsis_VibhavBansal_102003681'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This package is implimentation of multi-criteria decision analysis using topsis',   # Give a short description about your library
  author = 'Vibhav Bansal',                   # Type in your name
  author_email = 'vibhav29bansal@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/vibhav2909/Topsis_VibhavBansal_102003681',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/vibhav2909/Topsis_Vibhav_102003681/archive/refs/tags/v_0.1.tar.gz',    # I explain this later on
  keywords = ['topsis'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          ''
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
