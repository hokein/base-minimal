{
  'targets': [
    {
      'target_name': 'hello',
      'type': 'executable',
      'sources': [
         'helloworld.cc',
      ],
      'include_dirs': [
         '..',
      ],
      'dependencies': [
         '../base.gyp:base',
      ],
    },
  ],
}

