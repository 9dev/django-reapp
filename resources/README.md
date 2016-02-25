# {{ full_app_name }}

Django app that...

## Installation

- Add `{{ safe_app_name }}` folder to Python path.
- Add `"{{ safe_app_name }}"` to your `INSTALLED_APPS`.

## Usage

...

## Demo

`{{ full_app_name }}` provides a simple demo with example usage. To install it from the console, execute `fab install` command. To run it, type ``fab runserver``.

Of course, to do that you need to have `fabric` installed on your computer.

## Tests

Tests assume that Selenium's ChromeDriver can be found at:
> /usr/bin/chromedriver

It also needs correct permissions. Make sure to run:

    $ sudo chmod a+x /usr/bin/chromedriver

To run all the tests simply type:

    $ fab install
    $ fab testall

## Notes

This package was tested with Python {{ python_version }} and Django {{ django_version }}.

## License

MIT

