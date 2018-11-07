Nikola Metadata Upgrade (v7 to v8)
==================================

This plugin fulfills two purposes:

1. It upgrades old-style tags metadata (`draft`, `private`, `mathjax`)
   to new-style metadata, i.e. using the `status` and `has_math` metadata fields.
   The tags were used in Nikola v7 and earlier, and are no longer used by default
   in Nikola v8. If you are using them in your blog, **you will be warned** by
   `nikola build` — otherwise, don’t install this plugin (it won’t do a thing
   anyway and will only waste disk space and load time).

2. It converts sections to categories. If both section and category are specified
   in a post, a warning is printed and the category kept.

The plugin adds the `nikola upgrade_metadata_v8` command. Remove the plugin
manually after the upgrade.
