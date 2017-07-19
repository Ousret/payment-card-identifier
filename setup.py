from setuptools import setup


setup(
    name='payment-card-identifier',
    version='0.1.0',
    author='Ahmed TAHRI, @Ousret',
    author_email='ahmed@tahri.space',
    description='Payment card identifier provides a useful utility method for determining a credit card type '
                'from both fully qualified and partial numbers.',
    license='MIT',
    packages=['payment_card_identifier'],
    test_suite='test',
    url='https://github.com/Ousret/payment-card-identifier',
    download_url='https://github.com/Ousret/payment-card-identifier/archive/0.1.0.tar.gz',
    install_requires=[],
    tests_require=['Faker'],
    keywords=['payment', 'credit card', 'debit card', 'visa', 'mastercard', 'merchant', 'pos', 'amex',
              'card type identifier'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
