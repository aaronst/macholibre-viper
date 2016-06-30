# macholibre-viper
Viper module for macholibre

## Description
This is a very simple Viper module for macholibre.  It allows you to display the JSON output of macholibre in the Viper console (gross) or specify an output file.  By default it will parse the file for the currently opened session, but you can also specify a path to some other file.

## Usage
```
-o, --output [path for JSON output]
-p, --path   [path to mach-o]
```

## Isn't there already a Mach-O module for Viper?
Yes, but it's not as verbose, and is missing some things like CodeSignatures.  Hopefully we'll be able to merge these two into one, but for now this is an easy alternative for people who want to try it out.
