#--- API LICENSE CONFIGURATION -----------------------------------------------------------------------
# Default license keys used by pattern.web.SearchEngine to contact different API's.
# Google and Yahoo are paid services for which you need a personal license + payment method.
# The default Google license is for testing purposes (= 100 daily queries).
# Wikipedia, Twitter and Facebook are free.
# Bing, Flickr and ProductsWiki use licenses shared among all Pattern users.

license = {}
license["Google"] = \
    "AIzaSyBxe9jC4WLr-Rry_5OUMOZ7PCsEyWpiU48"

license["Bing"] = \
    "VnJEK4HTlntE3SyF58QLkUCLp/78tkYjV1Fl3J7lHa0="

license["Yahoo"] = \
    ("", "") # OAuth (key, secret)

license["DuckDuckGo"] = \
    None

license["Wikipedia"] = \
    None

license["Twitter"] = (
    "VazSChXEQMZWwK6o81Wg8JS3y", # OAuth (key, secret, token)
    "uwgirnpnMqG6nJRA6sGsDpBOeUFnI2jUjwMjB7EghTPMq7Jq99", (
    "4796888732-hlg3ffWwuzmVWZIiRdIBV49nkA1dTVlGHYyyIWl",
    "2sJg1SxdwuMCwaFEqqudZQrUYxNVl5axJM4qN7qfCTi2U"))

license["Facebook"] = \
    "848778391910837|c766f768c3b2aadd76a1e184ad830637"

license["Flickr"] = \
    "787081027f43b0412ba41142d4540480"

license["ProductWiki"] = \
    "64819965ec784395a494a0d7ed0def32"
