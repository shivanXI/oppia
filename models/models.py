# coding: utf-8
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Models for Oppia."""

__author__ = 'Sean Lip'

from google.appengine.ext import ndb

from exploration import Exploration


class Image(ndb.Model):
    """An image."""
    # The image itself.
    image = ndb.BlobProperty()

    @property
    def id(self):
        return self.key.id()


class Widget(ndb.Model):
    """A specific HTML/JS/CSS widget."""
    # The raw widget code.
    raw = ndb.TextProperty()

    @property
    def id(self):
        return self.key.id()


class GenericWidget(ndb.Model):
    """A generic, reusable widget that is part of the widget repo."""
    # The name of the generic widget.
    name = ndb.StringProperty(required=True)
    # The category to which this widget belongs.
    category = ndb.StringProperty(required=True)
    # The description of the generic widget.
    description = ndb.TextProperty()
    # The raw code for the generic widget.
    raw = ndb.TextProperty()
    # Parameter names, definitions, types and default arguments for this widget.
    params = ndb.JsonProperty(repeated=True)

    @property
    def id(self):
        return self.key.id()


class AugmentedUser(ndb.Model):
    """Stores information about a particular user."""
    # The corresponding user.
    user = ndb.UserProperty(required=True)
    # The list of explorations that this user has editing rights for.
    editable_explorations = ndb.KeyProperty(kind=Exploration, repeated=True)

    @property
    def id(self):
        return self.key.id()
