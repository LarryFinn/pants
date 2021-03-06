# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import unittest

from pants.base.exceptions import BuildConfigurationError
from pants.init.options_initializer import BuildConfigInitializer, OptionsInitializer
from pants.option.errors import OptionsError
from pants.option.options_bootstrapper import OptionsBootstrapper


class OptionsInitializerTest(unittest.TestCase):
    def test_invalid_version(self):
        options_bootstrapper = OptionsBootstrapper.create(
            args=["--backend-packages=[]", "--backend-packages2=[]", "--pants-version=99.99.9999"]
        )
        build_config = BuildConfigInitializer.get(options_bootstrapper)

        with self.assertRaises(BuildConfigurationError):
            OptionsInitializer.create(options_bootstrapper, build_config)

    def test_global_options_validation(self):
        # Specify an invalid combination of options.
        ob = OptionsBootstrapper.create(
            args=["--backend-packages=[]", "--backend-packages2=[]", "--remote-execution",]
        )
        build_config = BuildConfigInitializer.get(ob)
        with self.assertRaises(OptionsError) as exc:
            OptionsInitializer.create(ob, build_config)
        self.assertIn("The `--remote-execution` option requires", str(exc.exception))
