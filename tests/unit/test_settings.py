#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Copyright Bernardo Heynemann <heynemann@gmail.com>

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fudge import Fake, with_fakes, with_patched_object
from fudge.inspector import arg
from fudge_extensions import clear

import skink.lib.ion.settings as sets
from skink.lib.ion import Settings

parser = Fake(callable=True).with_args().returns_fake()

@with_fakes
@with_patched_object(sets, "ConfigParser", parser)
@clear
def test_can_create_settings():
    settings = Settings("some_dir")

    assert settings

@with_fakes
@with_patched_object(sets, "ConfigParser", parser)
@clear
def test_settings_will_load_config_ini():
    settings = Settings("some_dir")
    parser.expects("__init__").expects("read").with_args(arg.endswith("config.ini"))

    settings.load()

@with_fakes
@with_patched_object(sets, "ConfigParser", parser)
@clear
def test_settings_will_load_config_ini():
    settings = Settings("some_dir")

    parser.provides("__init__").returns_fake().provides("read").with_args(arg.endswith("config.ini")).returns_fake()

    settings.load()

    assert settings.config
