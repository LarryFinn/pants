# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

contrib_plugin(
  name='plugin',
  dependencies=[
    ':target_types',
    'contrib/cpp/src/python/pants/contrib/cpp/targets',
    'contrib/cpp/src/python/pants/contrib/cpp/tasks',
    'contrib/cpp/src/python/pants/contrib/cpp/toolchain',
    'src/python/pants/build_graph',
    'src/python/pants/goal:task_registrar',
  ],
  distribution_name='pantsbuild.pants.contrib.cpp',
  description='C++ pants plugin (deprecated).',
  build_file_aliases=True,
  register_goals=True,
  tags = {"partially_type_checked"},
)

python_library(
  name='target_types',
  sources=['target_types.py'],
  dependencies=[
    'src/python/pants/engine:target',
  ],
  tags = {"type_checked"},
)
